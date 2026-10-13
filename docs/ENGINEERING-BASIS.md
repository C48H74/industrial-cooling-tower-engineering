# Engineering basis and model boundaries

## System definition

The executable model represents a preliminary counterflow, open, evaporative cooling tower with constant liquid mass flow and heat capacity. It evaluates Merkel demand; it does not solve a vendor fill rating or determine tower dimensions. The worked example uses induced mechanical draft, but the integral itself does not size the fan or account for installation recirculation.

Define the control volume and battery limits before using results. An open cooling tower exposes circulating water to air. A closed evaporative fluid cooler separates process fluid inside a coil from spray water. A dry cooler transfers heat without the same evaporative mechanism. A refinery location does not make these technologies interchangeable.

## Thermal calculation

Water mass flow is `L = rho * V / 3600`. Heat duty is `Q = L * cp * (Th - Tc)`, with cp in kJ/(kg K) yielding kW. Range is `Th - Tc`; approach is `Tc - Twb`. The temperature effectiveness `range/(Th-Twb)` is not electrical efficiency or certified capacity.

The example deliberately uses constant rho=1000 kg/m³ and cp=4.18 kJ/(kg K) to reproduce the provided calculation. For a real project, select a validated fluid-property source, temperature basis, dissolved-solids/glycol composition and uncertainty. Aggregate simultaneous loads rather than summing unrelated maxima; account for auxiliary heat within the actual control volume.

## Psychrometric approximation

The code approximates inlet air enthalpy by saturated-air enthalpy at wet-bulb and specified absolute pressure. Saturation pressure uses the Magnus approximation within 0–60 °C. Humidity ratio and moist-air enthalpy are calculated on a dry-air mass basis. This is not a complete dry-bulb/wet-bulb psychrometer implementation or a certified property package.

A real fan selection requires actual volume and density at its inlet. For induced draft, that inlet is normally warm, humid discharge air. The example's 37,500 m³/h is retained as an independent assumption for auditing fan arithmetic; it is not inferred from the assumed dry-air mass flow. Normalized volume, ambient moist-air density and dry-air mass cannot be mixed without conversion.

## Merkel demand and supply

The numerical integral is `Me = integral cp dT / (hs(T)-ha(T))`, using `ha(T)=hin+(L/G)*cp*(T-Tc)`. G is dry-air mass flow. The model neglects change of liquid mass through evaporation, assumes a saturated interface and approximately unit Lewis factor, and uses a one-dimensional counterflow operating line.

The code rejects nonpositive enthalpy potential at sampled points. Trapezoidal integration is checked for convergence at the reference point. Such checks do not prove the approximation matches any real fill or every possible pinch. Final analyses should resolve the operating envelope and use a validated correlation and adequate integration/adaptive checks.

Supply must come from representative fill testing and vendor correlations at the relevant liquid/gas loading, fill depth, distribution and condition. A fitted or constant supply characteristic used for a demonstration is not vendor evidence. Geometry needs both thermal and hydraulic/aerodynamic verification; a hydraulic plan area does not establish thermal capability.

For scenarios with a fixed illustrative Me supply, the program inversely solves cold-water temperature. The supply is calibrated only to the reference example. No claim is made that actual fill supply stays constant with changing fan speed, liquid flow or operating condition. Crossflow geometry, detailed evaporation and plume calculations require suitable models beyond this implementation.

## Water and solute balance

The illustrative evaporation estimate assumes all rejected heat is latent and hfg=2400 kJ/kg. It is not a prediction from a full air-outlet calculation. Depending on the sensible heat balance, it is not a universal upper bound. A coupled dry-air, water-vapor and liquid energy/mass model is needed for more rigorous loss estimates.

For steady state and a conservative solute, `M=E+B+D`, `M*cm=(B+D)*cc`, `COC=cc/cm`, hence `B=E/(COC-1)-D`. Negative blowdown means the stated target and losses are inconsistent; the code rejects it. Include leaks and nonconservative species explicitly when present. Conductivity ratios need temperature compensation and chemistry review. Highest affordable COC is not necessarily chemically permissible.

## Mechanical interfaces

Fan power in air is volume times pressure rise. Shaft and electrical power require clearly bounded efficiencies. Select a fan using the system curve, wet-fill pressure loss, actual density, stable operating region, power envelope and installation effects. Select a motor against the governing absorbed power and service requirements, not a rounded example value.

Pump head must include static and pressure terms and complete circuit losses within coherent endpoints. A tower component loss cannot stand for the entire circulation system. Check suction at minimum basin level, operating temperature, absolute pressure, suction losses, NPSH requirement and appropriate margin. Review vortex formation, submergence and air entrainment.

Structural loading, seismic/wind design, hydrocarbon contamination, electrical classification, materials, hygienic operation and environmental permits remain project interfaces. Their absence is an engineering hold, not permission to insert generic default values.

## Release and acceptance

This repository is suitable for preliminary analysis and preparation of a vendor enquiry. Technical selection needs guaranteed vendor results across the required operating cases and resolved interfaces. Issued-for-construction documents need discipline checks, regulatory evidence and responsible approval. Acceptance needs an agreed protocol, complete instrument/calibration records, correction method, uncertainty analysis and documented contractual criteria.

The standards register is a routing and evidence register. Public identification of a standard does not prove full-text requirements were reviewed or met. Sources and edition status must be rechecked on the project date.
