# Exemplo de 30 m³/h e auditoria das três imagens

## Entradas fornecidas

Vazão 30 m³/h; quente 42 °C; fria 32 °C; TBU 28 °C; tiro induzido. Hipóteses de reprodução: rho=1000 kg/m³, cp=4,18 kJ/(kg K). Logo L=8,3333 kg/s, Q=348,3333 kW, range=10 K, approach=4 K, efetividade=71,43%. Propriedades reais à temperatura média mudam ligeiramente a carga; registrar método em vez de esconder a diferença.

## Auditoria quantitativa

| Afirmação da referência | Avaliação | Como tratar |
|---|---|---|
| 348 kW | Coerente com as hipóteses | Reproduzir e declarar propriedades |
| G/L=1,5 | Hipótese, não resultado de seleção | Distinguir ar seco e úmido; validar transferência |
| G=45.000 kg/h | Aritmeticamente correto se G/L=1,5 de ar seco | G=12,5 kg/s; Q/G=27,87 kJ/kg ar seco |
| 37.500 m³/h usando rho_air=1,20 | Aritmética correta, estado e base de massa insuficientes | Recalcular por volume específico e estado no ventilador; não transformar em garantia |
| Área 1,07 m² por A=Vw/[K*(Th-TBU-A)] | Correlação e dimensões de K não demonstradas | Não usar como dimensionamento validado |
| Área comercial 0,05 m² por 30/(60*10) | Coeficiente e interpretação não sustentados | Não selecionar torre com esse critério |
| Selecionar área ≥1,0 m² | Não decorre de método térmico demonstrado | Exigir carga hidráulica, velocidade e característica térmica |
| Perda de água 0,5 mca | Pode ser hipótese de componente, insuficiente para rede | Balanço de energia completo e distribuição |
| 80 mmca≈784 Pa | Aproximação coerente, 80*9,80665≈784,53 Pa | Não confundir com perda da água |
| Ventilador≈13,6 kW | 37.500/3600*784/0,60=13,611 kW | Potência de eixo sob eficiência definida; motor e eletricidade requerem outras perdas |

**Teste geométrico de plausibilidade:** se ar de 37.500 m³/h atravessasse área livre de 1,07 m², velocidade média seria aproximadamente 9,74 m/s. Isso exige checagem rigorosa contra curva do enchimento e arraste; não equivale a uma prova automática de impossibilidade. Área livre pode diferir da área em planta.

**Água de reposição ilustrativa:** Q totalmente latente e hfg=2400 kJ/kg produzem E=0,5225 m³/h. Com COC=4 e d=0,001%=0,00001, D=0,0003 m³/h, B≈0,17387 m³/h e M≈0,69667 m³/h. Esses resultados dependem das hipóteses; química, clima e estado de saída não foram fornecidos.

## Referência images (1).jpg

A imagem mistura carcaça de tiro natural e componentes de sistema industrial. Não usar a forma hiperbólica para inferir capacidade. Válvula de segurança no topo não é item genérico de torre atmosférica aberta; dispositivos de alívio podem existir em circuitos pressurizados associados. Um trocador interno não pertence necessariamente a uma torre aberta convencional; distinguir circuito fechado. Distribuição, enchimento, bacia, reposição, tratamento e bombas são conceitos úteis, mas desenho ilustrativo não comprova conectividade ou dimensionamento.

## Referência images.jpg

O corte mostra ventilador superior compatível com tiro induzido. Contudo a seta de eliminadores de gotas aparece na região inferior do enchimento: em contracorrente convencional, situar eliminadores acima da distribuição, antes de plenum/descarga. A descarga livre para o piso é recurso ilustrativo; saída operacional deve ligar à rede/bomba ou destino projetado. Não deduzir diâmetros, volume da bacia ou posição de motor apenas da figura.

## Esquema funcional coerente

Ar: ambiente → louvers/entrada inferior → enchimento em contracorrente → distribuição → eliminadores → plenum → ventilador superior → descarga quente e úmida.

Água: retorno quente → coletor/distribuição → enchimento → bacia → sucção da bomba → consumidores → retorno quente. Reposição entra em ponto compatível com controle de nível e tratamento; purga sai para destino autorizado. A posição relativa distribuição/eliminador deve ser confirmada no desenho do modelo selecionado.
