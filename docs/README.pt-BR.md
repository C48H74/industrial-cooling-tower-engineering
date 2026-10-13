# Engenharia de torres de resfriamento industriais

Pacote para estudos preliminares, especificação e revisão técnica de torres de resfriamento, com foco em utilidades de refinarias. Inclui skill em português, seis referências técnicas, registro normativo, cálculo reproduzível, seis gráficos vetoriais, dados CSV/JSON, painel HTML, imagens conceituais e modelos de coleta de dados.

O exemplo de 30 m³/h, 42→32 °C e TBU de 28 °C resulta em **348,33 kW**, range de 10 K e approach de 4 K. A área de enchimento e a vazão de ar do material de referência não foram convertidas em seleção garantida: faltam correlação do enchimento, condições completas do ar e dados do fabricante.

## Executar

```bash
python skills/torres-resfriamento-industriais/scripts/calcular.py --self-test
python -m unittest discover -s tests -v
python skills/torres-resfriamento-industriais/scripts/calcular.py --out output
```

Abrir `output/painel.html`. A curva de evolução representa degradação **sintética**, explicitamente assumida. O modelo de histórico permanece vazio até existirem medições.

## Aplicação profissional

1. Preencher registros de dados, cenários, requisitos e pendências em `templates`.
2. Conferir país, contrato, versões normativas e texto integral aplicável.
3. Calcular carga e balanços com hipóteses rastreáveis.
4. Solicitar curvas, geometria e garantias ao fabricante.
5. Revisar interfaces e fechar pendências antes da liberação correspondente.
6. Executar aceitação segundo protocolo acordado e documentado.

O pacote não elimina a necessidade de dados de projeto ou responsabilidade técnica. Expõe essas necessidades e evita tratá-las como dados conhecidos. Normas pagas não foram integralmente consultadas; as imagens são sintéticas. Ver [README principal](../README.md), [requisitos de dados](DATA-REQUIREMENTS.md) e [plano de qualidade](QUALITY-PLAN.md).
