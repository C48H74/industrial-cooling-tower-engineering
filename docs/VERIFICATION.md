# Verification scope

The executable includes self-checks for the heat-duty and fan arithmetic, water/solute balance, Merkel numerical convergence at the reference point, demand monotonicity, inverse-temperature solution and invalid physical inputs. The unittest suite adds a latent-water balance cross-check, fan-efficiency boundary, an enthalpy-pinch rejection case and generated-artifact parsing.

These are implementation checks. They do not validate fill correlations, psychrometric approximation accuracy against an independent property package, equipment selection, sanitary compliance, structural design or real-world thermal performance. Those remain explicit project/vendor tasks.

Run:

```bash
python skills/torres-resfriamento-industriais/scripts/calcular.py --self-test
python -m unittest discover -s tests -v
python skills/torres-resfriamento-industriais/scripts/calcular.py --out output
```

The GitHub Actions workflow repeats the self-checks and unittest suite on Python 3.10 and 3.12 and uploads generated calculations as artifacts. A committed workflow is not evidence of a successful remote run: inspect the actual run status.

The skill package is also checked with the Codex skill validator where available. That validator checks format/frontmatter, not engineering adequacy. Numeric example outputs can vary slightly if properties, integration or the reference case are deliberately revised; document such changes and regenerate charts.
