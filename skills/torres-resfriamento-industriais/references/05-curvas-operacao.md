# Curvas de desempenho e evolução

## Arquivos reproduzíveis incluídos

Executar `scripts/calcular.py --out output`. O painel HTML abre localmente e contém seis gráficos vetoriais com dados CSV e resultados JSON. Não depende de internet ou bibliotecas externas. Eixos, hipóteses e natureza simulada aparecem no gráfico e no painel.

| Curva | Variáveis mantidas | Uso e limite |
|---|---|---|
| Carga versus vazão | Temperaturas e propriedades | Verificar proporcionalidade e cenários de processo; não mede capacidade da torre |
| Demanda Merkel versus approach | T quente, TBU, pressão e G/L | Demonstra esforço de transferência; range varia e não se afirma curva de tamanho/custo |
| Água fria versus TBU | Me oferta assumido fixo, T quente e G/L | Sensibilidade ilustrativa; falta característica do fornecedor para previsão comercial |
| Água versus COC | Carga, hfg, fração latente e arraste | Mostra purga/reposição e retorno decrescente de COC; não avalia limite químico |
| Potência versus rotação | Geometria/densidade/rendimento | Leis de semelhança; não garante temperatura ou controle estável |
| Approach versus tempo sintético | Clima, T quente e G/L; oferta Me cai 25% em 180 dias fictícios | Ilustra degradação; não é histórico, tendência comprovada nem vida prevista |

Não inventar crescimento de eficiência, economia de energia ou deterioração real com datas se não existir histórico. Para demonstrar restauração após limpeza, utilizar evento assumido e claramente rotulado ou dados reais; nunca indicar benefício comprovado por simulação.

## Curvas exigidas do fabricante

Solicitar família de temperatura fria para faixas de TBU, vazão, temperatura quente, rotações e número de células. Definir faixa de validade, altitude/pressão, qualidade da água, carga mínima de molhamento, estado de limpeza e envelope de controle. Exigir oferta térmica e perda de carga do enchimento nas mesmas cargas líquida/gasosa; curvas de ventilador com potência e estabilidade; curva de bomba com rendimento e NPSHr; garantia de arraste e ruído nas condições contratuais. Identificar interpolação e impedir extrapolação silenciosa.

## Evolução com dados de campo

Schema em `assets/historico-modelo.csv`, apenas cabeçalho para não confundir exemplos com medições: timestamp ISO com fuso; célula; Th; Tc; TBU; TBS; p; vazão água; rotação; potência elétrica; dp ar; reposição; purga; condutividade reposição/circulação; vibração; evento; qualidade. Definir unidade e ponto de medição no dicionário de instrumentos. Registrar lacunas, sensor em falha, mudança de calibração, limpeza e troca de enchimento.

1. Sincronizar relógios e definir período de agregação conforme dinâmica; não interpolar grandes falhas sem indicação.
2. Selecionar períodos estáveis e comparáveis; separar partida, chuva, célula parada, alteração de processo e manutenção.
3. Calcular Q, R, A, kW elétrico/kW térmico (fronteira explícita), m³ de reposição/MWh térmico, COC por espécie conservativa e disponibilidade.
4. Corrigir performance por TBU, vazão, Th, rotação e células mediante modelo calibrado/curva do fornecedor. Residual `Tc_medida-Tc_prevista` é mais informativo que approach bruto isolado.
5. Mostrar sinal bruto e corrigido, incerteza, quantidade de pontos e exclusões. Ajuste regressivo deve separar treino e validação temporal; não usar a mesma amostra para afirmar capacidade preditiva.
6. Correlacionar residual crescente com dp, vazão, distribuição, recirculação, qualidade e inspeção. Não concluir que todo residual é enchimento sujo.
7. Após intervenção, comparar janelas equivalentes e energia total (bombas+ventiladores+tratamento), incluindo efeitos no processo. Reportar economia com intervalo e fronteiras.

## Ensaio e aceitação

Escolher protocolo CTI ATC-105 ou ASME PTC 23 conforme contrato e escopo; obter texto integral. Acordar pontos, carga, estabilidade, condições admissíveis, instrumentos, correção climática, incerteza, responsabilidades e critérios antes do teste. Não apresentar tolerâncias de ensaio inventadas como normativas. Guardar certificados de calibração, posições, fotos reais, leituras brutas, condições por célula, cálculos e relatório assinado. Certificação de linha CTI e teste de aceitação em campo têm funções distintas.

## Economia e otimização

Integrar séries horárias para kWh e água anuais, com tarifas e horas verificadas. Somar investimento, energia, água, produtos, descarte, manutenção e indisponibilidade em horizonte/taxa explícitos. Variar preço de água/energia, COC viável, clima, fouling e redundância. Não otimizar só ventilador: água mais quente pode afetar processo e energia em outras máquinas. Pareto de custo/água/energia exige alternativas tecnicamente viáveis com mesma carga, clima e disponibilidade.
