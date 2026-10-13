# Base de projeto e métodos

## 1. Dados mínimos e rastreabilidade

Usar uma linha por variável: identificador; valor; unidade; fonte; data; cenário; qualidade (medido/fornecido/hipótese/garantia); incerteza; dono; situação. Para vazão especificar temperatura de referência e se é total ou por célula. Para temperaturas indicar ponto e instrumento. Usar a temperatura de entrada do ar na torre, que pode diferir da estação meteorológica por recirculação.

**Processo:** carga por consumidor, simultaneidade, água quente/fria exigida, vazão mínima/normal/máxima, pressão de retorno, contaminação potencial, temperatura máxima de enchimento, transientes e restrição de parada. Separar carga de processo de calor de bombas e outros equipamentos efetivamente dissipado no circuito.

**Clima:** coordenadas, altitude, pressão barométrica, temperatura de bulbo seco e úmido coincidentes, umidade, distribuição horária, vento e direção, congelamento, poeira, salinidade e eventos extremos. Selecionar percentil de projeto com o proprietário conforme consequência de excedência; não impor universalmente 0,4%, 1% ou 2%. Não combinar máximos independentes de TBS/TBU.

**Água:** análise de reposição e circulação com pH, condutividade, alcalinidade, dureza, sílica, cloretos, sulfatos, sólidos suspensos, ferro, matéria orgânica e microbiologia; disponibilidade, preço, descarga permitida e variação sazonal. A qualidade condiciona enchimento, metalurgia e ciclos.

**Local e contrato:** país/município, limites de ruído diurno/noturno, emissões/aerossóis, outorga, efluentes, cargas civis, classificação de áreas, garantia térmica, arraste, energia, disponibilidade, acesso e critério de ensaio.

Sem dados do fabricante é possível calcular carga, demanda, sensibilidades e requisitos de consulta. Não fechar geometria térmica, curva garantida, seleção de ventilador ou estrutura executiva.

## 2. Carga, range, approach e efetividade

`L = rho_w * Vw / 3600` [kg/s], Vw em m³/h.

`Q = L * cp_w * (Th-Tc)` [kW], cp em kJ/(kg K).

Preferir `Q=L*(h_w(Th)-h_w(Tc))` com propriedades dependentes de temperatura quando relevante. Declarar concentração de glicol, sal ou contaminantes; água pura não representa qualquer solução.

`R=Th-Tc`; `A=Tc-Twb`; `epsilon=R/(Th-Twb)`.

Efetividade térmica não é eficiência elétrica, capacidade certificada ou fração de calor evaporativo. Range decorre de carga e vazão; approach depende do conjunto torre/ar/clima. Especificar quais parâmetros permanecem constantes ao comparar cenários.

## 3. Psicrometria

Com pressão p e TBS/UR: `pv=UR*pws(Tbs)`; `w=0.621945*pv/(p-pv)`; `h=1.006*Tbs+w*(2501+1.86*Tbs)` [kJ/kg ar seco]. UR é fração; p e pv devem estar na mesma unidade. Volume específico por kg de ar seco: `v=0.287042*(Tbs+273.15)*(1+1.607858*w)/p`, com p em kPa. Então `Vair=G*v`, e densidade do ar úmido é `(1+w)/v`.

Para TBS/TBU usar relação de saturação adiabática/psicrômetro apropriada ao método de medição; não converter TBU diretamente em TBS. A aproximação `h_in≈h_sat(Twb,p)` é útil para Merkel preliminar, porém omite dependência residual da condição real de entrada. Em altitude, recalcular pressão e propriedades, não reutilizar densidade de 1,20 kg/m³.

No script, pws usa aproximação exponencial de Magnus para 0–60 °C: `0.61094*exp(17.625*T/(T+243.04))` kPa. Não é implementação certificada ASHRAE/IAPWS. Verificar contra biblioteca de propriedades validada antes de projeto detalhado. Essa escolha não substitui os métodos normativos de medição.

## 4. Balanço ar/água

`Q≈G*(h_out-h_in)`, desprezando variação da vazão líquida e termos secundários. `G` em kg/s de ar seco. Se `G/L=1.5` for hipótese, isso não prova vazão necessária; apenas determina incremento entálpico aproximado. A condição de saída deve ser fisicamente possível e compatível com transferência e saturação. Não assumir automaticamente saída saturada e não usar simultaneamente estados incompatíveis.

Balanço rigoroso do volume de controle: massa de ar seco constante; `E=G*(w_out-w_in)`; `Lout=Lin-E`; `Lin*h_w,in+G*h_air,in=Lout*h_w,out+G*h_air,out`, com perdas/ganhos externos incluídos quando relevantes. Reposição e purga devem ter volumes de controle claramente definidos.

## 5. Método de Merkel para contracorrente

Sob hipóteses de Lewis aproximadamente unitário, interface saturada à temperatura da água, resistência líquida desprezada e L constante:

`Me_dem = integral[Tc,Th] cp_w*dT/(h_sat(T,p)-h_air(T))`.

`h_air(T)=h_in+(L/G)*cp_w*(T-Tc)`.

Integrar numericamente com refinamento de malha, verificando potencial positivo em todo o enchimento. O pinch pode ocorrer no interior, não apenas nos extremos. Comparar Me com a característica de oferta do fabricante na mesma definição de K, a, V, L e base de unidades. Uma correlação `Me_oferta=C*(L/G)^(-n)` pode existir para enchimento e altura específicos; C e n nunca devem ser inventados como dados de seleção.

Resolver `Me_dem(Tc)=Me_oferta` por busca delimitada dentro do domínio físico, repetindo para cada cenário. Característica de oferta depende de carga hidráulica, vazão de ar, altura, tipo de enchimento, distribuição e condição de limpeza. Me constante em uma sensibilidade é uma hipótese, não uma lei de operação.

Merkel não prevê rigorosamente umidade de saída ou evaporação. Para balanço acoplado de massa, não saturação de descarga, Lewis variável e pluma, considerar Poppe ou modelo validado equivalente; exigir equações, propriedades, calibração e validação. Torres de fluxo cruzado exigem tratamento geométrico adequado, não aplicar a linha 1D de contracorrente como solução universal.

## 6. Área, altura e enchimento

`A_plan=Vw/q_L` com q_L em m³/(m² h) é apenas verificação de carga hidráulica. `A_plan=Vair/u` é verificação aerodinâmica no estado definido, m³/s e m/s. Atender ambas não garante transferência térmica. Área frontal, área em planta e área de superfície molhada são diferentes.

Altura térmica deriva da correlação de transferência do enchimento e sua integração; verificar perda de carga molhada, inundação, distribuição, capacidade estrutural, temperatura admissível, fouling, resistência ao fogo e acesso. Film fill pode reduzir volume com água adequada; splash/trickle podem melhorar tolerância à sujeira. Obter ensaios em cargas de água e ar compatíveis e fator de degradação justificado.

Registrar margens separadas para carga, clima, degradação e disponibilidade. Recalcular desempenho com cada margem; não multiplicar porcentagens sem explicar consequência.

## 7. Água, sais e reposição

Para estimativa energética: `E=f_lat*Q/hfg` [kg/s], onde f_lat é fração de calor latente explicitamente assumida. `f_lat=1` serve como cenário de referência de calor totalmente latente, não como previsão psicrométrica universal. Em certas condições o calor sensível do ar pode entrar no balanço e invalidar essa interpretação como limite superior.

Arraste: `D=d*Vw`, d em fração volumétrica. Não confundir 0,001% com 0,001. Garantia deve indicar método e condições. Arraste é água líquida com sais; evaporação idealmente não carrega sólidos dissolvidos.

Em regime permanente sem vazamentos e com soluto conservativo: `M=E+B+D`; `M*c_m=(B+D)*c_c`; `COC=c_c/c_m`; `B=E/(COC-1)-D`; `M=E*COC/(COC-1)`. Aplicar unidades consistentes. Se B calculada <0, o COC alvo não pode ser mantido por purga positiva com aquele arraste: recalcular concentração real ou rever perdas, não truncar silenciosamente e manter o mesmo COC.

Com vazamento F que leva concentração da circulação: substituir B+D por B+D+F. Dosagem, precipitação, filtração e volatilização tornam certos constituintes não conservativos. Condutividade só aproxima COC quando química e temperatura permitem. Definir ciclos pela espécie limitante, corrosão, incrustação, tratamento e licença de descarga, não pelo maior número economicamente atraente.

## 8. Incerteza

Para variáveis independentes: `(uQ/Q)^2≈(uL/L)^2+(ucp/cp)^2+(uΔT/ΔT)^2`, `uΔT²=uTh²+uTc²`. Se sensores compartilham calibração, considerar covariância. `uA²=uTc²+uTwb²` sob independência. Pequeno approach exige melhor instrumentação, posicionamento e avaliação de recirculação. A incerteza final de desempenho precisa do modelo de correção e protocolo de teste.
