# Integração em refinaria e verificação dos equipamentos

## Tipologia e interfaces

Começar comparando torre aberta de tiro induzido, circuito fechado evaporativo e solução seca/híbrida conforme processo, consumo hídrico, contaminação, pluma e manutenção. Refinaria não implica torre hiperbólica: conjuntos retangulares multicélulas de tiro mecânico são referência visual pertinente. Uma torre aberta contém água em contato com ar, distribuição, enchimento, eliminadores, entradas e bacia. Serpentina separando fluido de processo caracteriza outra arquitetura; trocadores podem ficar externos no circuito.

Preparar diagrama funcional com consumidores, retorno quente, alimentação da distribuição, bacia fria, sucção das bombas, reposição, purga, overflow, dreno, amostragem, filtração lateral e tratamento. Marcar limites de bateria, níveis, pressões, temperaturas, vazões e destinos. Não conectar purga automaticamente à drenagem pluvial.

## Ventilação e acionamento

Montar orçamento de pressão por entradas/louvers, enchimento molhado, eliminadores, distribuição, suportes, plenum, fan stack, telas e efeitos de instalação. Usar curvas do fornecedor, distinguindo pressão estática e total. A pressão de 784 Pa da referência é uma hipótese a conferir, não valor típico universal.

`P_air=V_actual*dp` [W]. `P_shaft=P_air/eta_fan`; `P_motor_out=P_shaft/eta_trans`; `P_grid=P_motor_out/(eta_motor*eta_vfd)`. Definir fronteira de cada eficiência para não duplicar perdas. Tiro induzido exige volume e densidade na entrada do ventilador com ar quente/úmido; volume normalizado não serve diretamente.

Confrontar curva ventilador/sistema em densidade de serviço. Conferir estabilidade, stall, rotação, passo, velocidade periférica, potência absorvida em toda a faixa, partida, temperatura, corrosão, vibração, caixa redutora, alinhamento e proteção. Selecionar motor pela condição limitante e contrato; 13,6 kW calculados não significam motor de placa de 13,6 kW.

Leis de semelhança para geometria/densidade constantes e região válida: V∝N, dp∝N², P∝N³. Alterações de densidade, passo, rendimento, fouling e controle da rede alteram comparação. A redução de rotação não preserva necessariamente temperatura fria. Medir ruído por bandas e condições; não converter potência acústica em pressão sonora sem modelo de propagação.

## Hidráulica e bombeamento

Definir caminho completo do ponto de sucção até retorno, incluindo consumidores. `H=Δz+Δp/(rho*g)+Σhf+ΣK*v²/(2g)+Δ(v²/2g)` com limites coerentes. Em circuito que retorna à bacia aberta, a energia de elevação até distribuição não é automaticamente recuperada como em um circuito totalmente fechado.

Darcy-Weisbach: `hf=f*(ell/D)*v²/(2g)`, fator Darcy, Reynolds e rugosidade explícitos. Não misturar fator Fanning. Incluir válvulas, strainers sujos, trocadores, medidor, bocais e distribuição. Verificar rede mínima/normal/máxima, velocidades, golpes de aríete, transientes e balanceamento por célula.

`P_hyd=rho*g*Vw_s*H`; `P_shaft=P_hyd/eta_pump`. NPSHa a partir de pressão absoluta na superfície da bacia, cota mínima, pressão de vapor à temperatura de sucção e perdas de sucção; comparar à NPSHr com margem definida pela aplicação e fornecedor. Avaliar submergência, vórtices, entrainment de ar, peneiras, acesso e operação com célula isolada. Não aplicar 0,5 mca da imagem ao circuito completo.

## Distribuição, bacia e civil

Exigir cobertura uniforme dos bocais nas vazões permitidas, pressão mínima/máxima, tamanho de orifício, resistência a entupimento, orientação, sobreposição, acesso e isolamento. Verificar q por bocal e ramal; não adotar quantidade de bocais exclusivamente por área.

Bacia: volume operacional, reserva de reposição, volume drenável das linhas/enchimento na parada, borda livre, overflow, níveis de alarme, proteção contra sucção de ar, lavagem, sedimentos e isolamento. Tempo de residência não determina sozinho volume total. Dimensionar fundação para peso seco, molhado, água acumulada, manutenção, vento, sismo e dinâmica conforme base civil local. Conferir carga nos bocais e movimentos térmicos das tubulações.

## Implantação e materiais

Estudar ventos dominantes e adversos, recirculação do ar úmido, interferência de edifícios, proximidade entre células, admissão de ar de prédios, áreas ocupadas, corrosão de instalações vizinhas, rotas de manutenção e içamento. Distâncias de afastamento precisam de manual do fabricante e exigências locais; não inventar distância universal. Em geometria congestionada, avaliar CFD com condições de contorno verificadas, calibração e critérios claros.

Materiais: compatibilizar aço galvanizado, inox, FRP, concreto e PVC/PP com temperatura, química, UV, abrasão e incêndio. Cloretos, pH, biocidas e concentração afetam corrosão; inox não é imunidade. Pedir resina, fibras, comportamento ao fogo e propriedades estruturais pertinentes. Definir pares galvânicos, fixadores, reparos de revestimento e proteção de partes submersas. Normas Petrobras/proprietárias só entram com código, revisão e texto fornecidos ou acesso autorizado; não inventar designação.

## Confiabilidade e controle

N+1 deve ser demonstrado por desempenho com uma célula/acionamento indisponível e no clima contratual, incluindo distribuição, vazão mínima e rede hidráulica. Dividir nominal por N não prova redundância térmica. Definir isolamento seguro e manutenção com outras células operando.

Instrumentos: temperaturas quente/fria por célula e cabeçalhos; TBS/TBU de entrada representativas; vazão e pressão; nível; condutividade compensada; parâmetros de tratamento especificados pelo especialista; vibração; velocidade; potência elétrica e estado de válvulas. Criar folha de instrumentos com faixa, precisão, localização, calibração e amostragem.

Lógica indicativa a confirmar em HAZOP: nível baixo-baixo protege bombas; vibração alta-alta protege ventilador; falha de ventilador gera redistribuição/alarme; temperatura fria alta sinaliza limitação de processo; condutividade comanda purga conforme química e válvulas; prevenção de partida durante manutenção por bloqueio físico e elétrico. Não prescrever automaticamente desligamento de toda a utilidade por um alarme isolado.

Em clima frio: avaliar congelamento de louvers/enchimento, distribuição mínima, ciclos de ventilador, bypass e aquecimento apropriado. Reversão de ventilador só quando permitida pelo fabricante. Sistemas com hidrocarbonetos exigem avaliação de vazamento, detecção, destino da água, classificação de áreas e fontes de ignição.

## Comissionamento e operação

Inspecionar montagem, limpeza, bacia, estanqueidade, sentido de rotação, balanceamento, aperto, proteções, instrumentação, curva das bombas e cobertura dos bocais. Validar tratamento e plano microbiológico antes de operação conforme jurisdição. Registrar linha de base limpa em condições estáveis e plano de teste acordado.

Operação: tendências de approach corrigido por clima/carga, dp do enchimento, vibração por rotação, kWh, reposição, purga, condutividade, corrosão e depósitos. Alteração no approach bruto isolado não diagnostica fouling. Ações dependem de causa confirmada e procedimentos de operação e manutenção.
