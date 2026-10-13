"""Modelo preliminar de torre contracorrente. Python 3.10+, somente stdlib."""
import argparse, csv, html, json, math
from pathlib import Path

CP = 4.18

def hsat(t, p):
    if not all(math.isfinite(x) for x in (t,p)):
        raise ValueError('Propriedades exigem entradas finitas')
    if not 0 <= t <= 60:
        raise ValueError('Aproximacao psicrometrica limitada a 0..60 C')
    ps = .61094 * math.exp(17.625 * t / (t + 243.04))
    if p <= ps:
        raise ValueError('Pressao menor ou igual a pressao de saturacao')
    w = .621945 * ps / (p - ps)
    return 1.006 * t + w * (2501 + 1.86 * t)

def merkel(cold, hot, wb, p, gas_water, n=800):
    if not all(math.isfinite(x) for x in (cold,hot,wb,p,gas_water)) or not isinstance(n,int) or n<2:
        raise ValueError('Entradas finitas e pelo menos dois intervalos exigidos')
    if not (0 <= wb < cold < hot <= 60 and gas_water > 0):
        raise ValueError('Exigir 0 <= TBU < fria < quente <= 60 e G/L > 0')
    hi = hsat(wb, p)
    step = (hot - cold) / n
    total = 0.
    for i in range(n + 1):
        t = cold + i * step
        delta = hsat(t, p) - hi - CP * (t - cold) / gas_water
        if delta <= 0:
            raise ValueError('Potencial entalpico nao positivo: ponto inviavel no modelo')
        total += CP / delta * (.5 if i in (0, n) else 1.)
    return total * step

def cold_for_me(target, hot, wb, p, ratio):
    # Find a feasible lower bound first; avoid crossing an interior pinch.
    upper = hot - .0001
    lower = None
    for i in range(1, 1000):
        c = wb + (hot - wb) * i / 1000
        try:
            m = merkel(c, hot, wb, p, ratio, 300)
        except ValueError:
            continue
        if m >= target:
            lower = c
            break
        raise ValueError('Raiz nao delimitada: oferta excede dominio pesquisado')
    if lower is None:
        raise ValueError('Nao foi encontrado intervalo fisico para a raiz')
    for _ in range(45):
        mid = (lower + upper) / 2
        if merkel(mid, hot, wb, p, ratio, 500) > target:
            lower = mid
        else:
            upper = mid
    return (lower + upper) / 2

def water(q, flow, cycles, drift):
    if not all(math.isfinite(x) for x in (q,flow,cycles,drift)) or q<0 or flow<=0:
        raise ValueError('Balanco exige entradas finitas, carga nao negativa e vazao positiva')
    if cycles <= 1 or not 0 <= drift < 1:
        raise ValueError('COC deve ser >1 e arraste fracao em [0,1)')
    e = q / 2400 * 3.6  # rho=1000, calor totalmente latente
    d = drift * flow
    b = e / (cycles - 1) - d
    if b < 0:
        raise ValueError('Purga negativa: COC alvo incompativel com arraste')
    return e, d, b, e + d + b

def csvwrite(path, headings, rows):
    with path.open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(headings); w.writerows(rows)

def chart(path, title, xlabel, ylabel, series, note):
    colors = ['#007f8b', '#e87b23', '#7255a3', '#bd3548']
    points = [v for _, data in series for v in data if all(math.isfinite(z) for z in v)]
    if not points:
        path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="150"><text x="20" y="50">Sem pontos viaveis no dominio desta demonstracao</text></svg>',encoding='utf-8')
        return
    xmin, xmax = min(x for x,y in points), max(x for x,y in points)
    ymin, ymax = min(y for x,y in points), max(y for x,y in points)
    pad = max((ymax-ymin)*.08, .01); ymin -= pad; ymax += pad
    def sx(x): return 95+(x-xmin)/(xmax-xmin or 1)*780
    def sy(y): return 390-(y-ymin)/(ymax-ymin or 1)*290
    esc = html.escape
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="530" viewBox="0 0 1000 530">',
       '<rect width="1000" height="530" fill="#f7fafc"/>',
       '<g font-family="Arial,sans-serif" fill="#172f43">',
       f'<text x="40" y="35" font-size="21" font-weight="bold">{esc(title)}</text>',
       '<text x="40" y="62" font-size="13">SIMULACAO PRELIMINAR — nao e curva garantida de fabricante</text>']
    for i in range(6):
        x=xmin+(xmax-xmin)*i/5; y=ymin+(ymax-ymin)*i/5
        s += [f'<path d="M95 {sy(y):.2f} H875" stroke="#dce5eb"/>',
              f'<text x="85" y="{sy(y)+4:.2f}" text-anchor="end" font-size="12">{y:.3g}</text>',
              f'<text x="{sx(x):.2f}" y="412" text-anchor="middle" font-size="12">{x:.3g}</text>']
    s += ['<path d="M95 100 V390 H875" fill="none" stroke="#172f43"/>',
          f'<text x="485" y="440" text-anchor="middle">{esc(xlabel)}</text>',
          f'<text transform="translate(22 250) rotate(-90)" text-anchor="middle">{esc(ylabel)}</text>']
    for j,(name,data) in enumerate(series):
        pts=' '.join(f'{sx(x):.2f},{sy(y):.2f}' for x,y in data)
        color=colors[j%len(colors)]
        s += [f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3"/>',
              f'<text x="{95+j*215}" y="472" fill="{color}" font-size="13">{esc(name)}</text>']
    s += [f'<text x="40" y="510" font-size="12">{esc(note)}</text>','</g></svg>']
    path.write_text('\n'.join(s),encoding='utf-8')

def self_test():
    assert abs(1000*30/3600*CP*10-348.3333333333)<1e-7
    assert abs(37500/3600*784/.6/1000-13.6111111111)<1e-7
    e,d,b,m=water(348.3333333333,30,4,.00001)
    assert abs(m-e-b-d)<1e-12 and abs(m-4*(b+d))<1e-12
    x=merkel(32,42,28,101.325,1.5)
    assert abs(x-merkel(32,42,28,101.325,1.5,1600))/x<1e-5
    assert merkel(31,42,28,101.325,1.5)>x
    assert abs(cold_for_me(x,42,28,101.325,1.5)-32)<.002
    for fn in [lambda:water(348,30,1,.00001),lambda:merkel(27,42,28,101.325,1.5),lambda:water(1,30,100,.1)]:
        try: fn()
        except ValueError: pass
        else: raise AssertionError('Entrada invalida aceita')
    print('PASS: carga, potencia, massa, sais, convergencia, monotonicidade, inversao e rejeicao de entradas invalidas')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',default='resultado-torre')
    for name,default,helptext in [('flow',30.,'m3/h agua'),('hot',42.,'C'),('cold',32.,'C'),('wb',28.,'C'),('pressure',101.325,'kPa absoluto'),('gas-water',1.5,'G ar seco/L agua kg/kg'),('dp',784.,'Pa hipotese'),('eta-fan',.6,'rendimento ar/eixo'),('cycles',4.,'ciclos concentracao'),('drift',.00001,'fracao recirculacao, 0.00001 = 0.001%')]:
        p.add_argument('--'+name,type=float,default=default,help=helptext)
    p.add_argument('--self-test',action='store_true')
    a=p.parse_args()
    if a.self_test: self_test(); return
    values=(a.flow,a.hot,a.cold,a.wb,a.pressure,a.gas_water,a.dp,a.eta_fan,a.cycles,a.drift)
    if not all(math.isfinite(x) for x in values):
        p.error('Todas as entradas numericas devem ser finitas')
    if a.flow<=0 or a.dp<0 or not 0<a.eta_fan<=1:
        p.error('Exigir vazao positiva, dp nao negativa e eficiencia em (0,1]')
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    me=merkel(a.cold,a.hot,a.wb,a.pressure,a.gas_water)
    q=a.flow*1000/3600*CP*(a.hot-a.cold)
    e,d,b,m=water(q,a.flow,a.cycles,a.drift)
    result={'status':'PRELIMINAR; sem selecao comercial','flow_m3_h':a.flow,'hot_C':a.hot,'cold_C':a.cold,'wetbulb_C':a.wb,'pressure_kPa':a.pressure,'range_K':a.hot-a.cold,'approach_K':a.cold-a.wb,'duty_kW':q,'L_kg_s':a.flow/3.6,'G_dry_kg_s':a.flow/3.6*a.gas_water,'merkel_demand':me,'evaporation_all_latent_m3_h':e,'drift_m3_h':d,'blowdown_m3_h':b,'makeup_m3_h':m,'reference_fan_volume_m3_h':37500,'reference_fan_shaft_kW':37500/3600*a.dp/a.eta_fan/1000,'assumptions':['rho agua=1000 kg/m3','cp=4.18 kJ/kgK','h entrada aproximado por h saturado(TBU)','G/L assumido','volume ventilador 37500 m3/h fixo da referencia, nao derivado de G','hfg=2400 kJ/kg e calor totalmente latente','curvas evolucao sao sinteticas; oferta Me fixa apenas para demonstracao']}
    (out/'resultados.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    specs=[]
    def emit(slug,title,xlabel,ylabel,headings,rows,series,note):
        csvwrite(out/(slug+'.csv'),headings,rows)
        chart(out/(slug+'.svg'),title,xlabel,ylabel,series,note)
        specs.append((slug,title,note))
    rows=[]
    for i in range(21):
        f=a.flow*(.5+i*.05); duty=f/3.6*CP*(a.hot-a.cold);rows.append((f,duty))
    emit('01-carga-vazao','Carga termica versus vazao','Vazao de agua (m3/h)','Carga (kW)',['flow_m3_h','duty_kW'],rows,[('Range constante',rows)],f'Range={a.hot-a.cold:g} K; rho=1000; cp=4.18')
    rows=[]
    for i in range(31):
        approach=1.5+i*.2; cold=a.wb+approach
        if cold>=a.hot: continue
        try: value=merkel(cold,a.hot,a.wb,a.pressure,a.gas_water)
        except ValueError: continue
        rows.append((approach,value))
    emit('02-merkel-approach','Demanda Merkel versus approach','Approach (K)','Me demanda (-)',['approach_K','Me'],rows,[('Demanda calculada',rows)],'T quente, TBU e G/L fixos; range varia; nao e curva de tamanho da torre')
    rows=[]
    for i in range(25):
        wb=max(0,a.wb-8)+i/24*(min(a.hot-2, a.wb+3)-max(0,a.wb-8))
        try: cold=cold_for_me(me,a.hot,wb,a.pressure,a.gas_water)
        except ValueError: continue
        rows.append((wb,cold))
    emit('03-fria-clima','Resposta a variacao climatica — oferta fixa','TBU (C)','Agua fria (C)',['wetbulb_C','cold_C'],rows,[('Me oferta fixo',rows)],'Me calibrado no exemplo; G/L e T quente fixos; nao representa curva validada')
    rows=[]
    for i in range(29):
        c=2+i*.25
        try: ev,dr,bl,mk=water(q,a.flow,c,a.drift)
        except ValueError: continue
        rows.append((c,ev,bl,mk))
    emit('04-agua-ciclos','Balanco de agua versus ciclos','COC (-)','Vazao (m3/h)',['cycles','evap_m3_h','blowdown_m3_h','makeup_m3_h'],rows,[(name,[(r[0],r[idx]) for r in rows]) for name,idx in [('Evaporacao',1),('Purga',2),('Reposicao',3)]],'Calor totalmente latente; hfg=2400; sem vazamento; arraste constante')
    rows=[(s/100,37500*s/100,a.dp*(s/100)**2,result['reference_fan_shaft_kW']*(s/100)**3) for s in range(50,101,2)]
    emit('05-ventilador-rotacao','Potencia de eixo versus rotacao relativa','N/Nref (-)','Potencia eixo (kW)',['speed_ratio','air_m3_h','dp_Pa','shaft_kW'],rows,[('Lei cubica ideal',[(r[0],r[3]) for r in rows])],'Geometria, densidade e rendimento constantes; nao garante capacidade termica')
    rows=[]
    for day in range(0,181,6):
        offer=me*(1-.25*day/180)
        cold=cold_for_me(offer,a.hot,a.wb,a.pressure,a.gas_water)
        rows.append((day,offer,cold,cold-a.wb))
    emit('06-evolucao-sintetica','Evolucao simulada de degradacao do enchimento','Tempo sintetico (dias)','Approach (K)',['day','Me_supply_assumed','cold_C','approach_K'],rows,[('Perda assumida de 25% Me',[(r[0],r[3]) for r in rows])],'SIMULACAO: perda linear arbitraria; nao e previsao de vida nem historico medido')
    body=''.join(f'<section><h2>{html.escape(title)}</h2><img src="{slug}.svg" alt="{html.escape(title)}"><p>{html.escape(note)}</p><a href="{slug}.csv">Dados CSV</a> · <a href="{slug}.svg">Grafico vetorial</a></section>' for slug,title,note in specs)
    page=f'''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Torre — desempenho e evolucao</title><style>body{{font:17px system-ui;background:#eaf0f4;color:#173047;margin:auto;max-width:1100px;padding:28px}}section,header{{background:white;border-radius:14px;padding:24px;margin:24px 0}}img{{width:100%;height:auto}}a{{color:#006978}}.tag{{color:#9d390b}}pre{{white-space:pre-wrap}}</style><header><h1>Torre de resfriamento: calculos e curvas</h1><p class="tag">Estudo preliminar reproduzivel · Curvas simuladas · Sem garantia comercial</p><p>Q={q:.2f} kW · Range={a.hot-a.cold:.2f} K · Approach={a.cold-a.wb:.2f} K · Me={me:.4f}</p><p>As imagens de refinaria sao conceituais e nao representam necessariamente este equipamento de 30 m3/h.</p><a href="resultados.json">Resultados e hipoteses</a></header>{body}<section><h2>Condicoes de reproducao</h2><pre>{html.escape(json.dumps(result,ensure_ascii=False,indent=2))}</pre></section></html>'''
    (out/'painel.html').write_text(page,encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
