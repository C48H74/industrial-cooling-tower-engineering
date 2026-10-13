import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills/torres-resfriamento-industriais/scripts/calcular.py'
spec=importlib.util.spec_from_file_location('tower',SCRIPT)
tower=importlib.util.module_from_spec(spec)
spec.loader.exec_module(tower)

class EngineeringChecks(unittest.TestCase):
    def test_latent_and_solute_balance(self):
        # Independent reference: 360 kW / 2400 kJ/kg = .15 kg/s = .54 m3/h.
        e,d,b,m=tower.water(360,40,5,.00002)
        self.assertAlmostEqual(e,.54)
        self.assertAlmostEqual(d,.0008)
        self.assertAlmostEqual(m,.675)
        self.assertAlmostEqual(m,5*(b+d))

    def test_merkel_grid_convergence_and_inverse(self):
        coarse=tower.merkel(32,42,28,101.325,1.5,400)
        fine=tower.merkel(32,42,28,101.325,1.5,3200)
        self.assertLess(abs(coarse-fine)/fine,1e-4)
        self.assertAlmostEqual(tower.cold_for_me(fine,42,28,101.325,1.5),32,places=3)

    def test_interior_or_endpoint_pinch_rejected(self):
        with self.assertRaises(ValueError):
            tower.merkel(32,42,28,101.325,.1)

    def test_pressure_changes_demand(self):
        sea=tower.merkel(32,42,28,101.325,1.5)
        altitude=tower.merkel(32,42,28,85,1.5)
        self.assertTrue(math.isfinite(altitude))
        self.assertNotAlmostEqual(sea,altitude,places=3)

    def test_inconsistent_water_target_rejected(self):
        with self.assertRaises(ValueError):
            tower.water(1,30,100,.1)

    def test_report_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable,str(SCRIPT),'--out',tmp],check=True,capture_output=True)
            dest=Path(tmp)
            r=json.loads((dest/'resultados.json').read_text(encoding='utf-8'))
            self.assertAlmostEqual(r['duty_kW'],348.3333333333,places=6)
            self.assertAlmostEqual(r['reference_fan_shaft_kW'],13.6111111111,places=6)
            self.assertEqual(len(list(dest.glob('*.csv'))),6)
            svgs=list(dest.glob('*.svg'))
            self.assertEqual(len(svgs),6)
            for svg in svgs:
                ET.parse(svg)
            self.assertTrue((dest/'painel.html').is_file())

    def test_invalid_fan_efficiency_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=subprocess.run([sys.executable,str(SCRIPT),'--eta-fan','1.2','--out',tmp],capture_output=True)
            self.assertNotEqual(r.returncode,0)
            self.assertFalse((Path(tmp)/'resultados.json').exists())

    def test_nonfinite_inputs_rejected(self):
        for fn in [lambda:tower.merkel(32,42,28,101.325,float('nan')), lambda:tower.water(float('inf'),30,4,.00001),lambda:tower.hsat(28,float('nan'))]:
            with self.assertRaises(ValueError): fn()
        with tempfile.TemporaryDirectory() as tmp:
            r=subprocess.run([sys.executable,str(SCRIPT),'--flow','nan','--out',tmp],capture_output=True)
            self.assertNotEqual(r.returncode,0)
            self.assertFalse((Path(tmp)/'resultados.json').exists())

if __name__=='__main__': unittest.main()
