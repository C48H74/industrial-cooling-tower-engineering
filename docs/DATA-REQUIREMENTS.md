# Project data requirements and hold points

Use `templates/design-input-register.csv` as the authoritative input register. A blank value means missing information, not zero or an accepted default. Every assumed value needs a reason, owner, expiry/review point and sensitivity assessment. Use `templates/scenario-register.csv` to preserve simultaneous conditions; do not mix independent maxima.

| Data group | Minimum evidence | Responsible discipline | Release affected if missing |
|---|---|---|---|
| Site/jurisdiction | Coordinates, country, pressure/altitude, authority, contractual standards list | Owner / project engineering | All project-specific releases |
| Process demand | Consumer duty/vazão, simultaneous cases, required temperatures and pressure | Process | Guaranteed thermal selection |
| Climate | Coincident design TBS/TBU, source/year/percentile, hourly envelope and wind | Process / meteorology / owner | Thermal selection and annual prediction |
| Water quality | Current and seasonal makeup/circulating analyses; contaminants and limits | Water treatment / process | Fill, materials, COC and chemical design |
| Fill performance | Transfer correlation, convention, depth, loading domain, wet pressure loss and evidence | Tower supplier | Thermal geometry and fan selection |
| Air outlet state | Validated calculation/rating at fan inlet with pressure, T and humidity | Tower supplier | Fan volume/density and power |
| Fan/drive | Curves, operating envelope, efficiencies, absorbed-power envelope, vibration/maintenance | Mechanical / electrical | Drive selection and energy guarantee |
| Hydraulic network | P&ID, elevations, pipe lengths/diameters/roughness, consumer/valve/nozzle losses | Piping / mechanical | Pump selection and distribution |
| Pump suction | Minimum basin level, temperature, atmospheric pressure, losses and NPSH evidence | Mechanical / civil | Pump and basin release |
| Availability | Required service with a cell/drive/pump unavailable, turndown and isolation | Owner / operations | N+1 or availability claims |
| Materials/structure | Chemistry, temperatures, fire policy, loads, supports and civil design basis | Materials / civil / supplier | Fabrication and foundations |
| Layout/environment | Recirculation study, air intakes, access, receptors, noise/drift/plume and permits | Layout / HSE / owner | Installation and environmental compliance |
| Controls | Cause-and-effect, instrument accuracy/location, process consequences and operating modes | I&C / operations / process | Automation release |
| Hygiene | Applicable sanitary law, accountable party, monitoring/cleaning and risk plan | Owner / water treatment / HSE | Operational readiness |
| Acceptance | Guaranteed points, protocol/edition, corrections, uncertainty, tolerances and witnesses | Owner / supplier / test agency | Contractual acceptance |

## Gate decisions

**G0: preliminary basis.** Sufficient evidence to calculate determined quantities and document uncertainties. Missing site/vendor data remain visible. This repository's reference case is at this stage.

**G1: vendor enquiry.** Process cases and conditions are owner-approved; gaps are explicit supplier questions or contract holds. A request for quotation can contain unresolved items only when clearly identified and commercially managed.

**G2: technical selection.** Supplier evidence closes thermal, hydraulic, mechanical, materials and availability requirements. Bid comparison uses common conditions and resolves deviations. Neither a badge nor a calculation script substitutes for this evidence.

**G3: construction release.** Discipline drawings, checks, permits, interfaces and responsible approval are complete. Required field measurements and vendor loads are available.

**G4: operating acceptance.** Commissioning, hygiene readiness, contracted tests, training and final documentation are complete, with open deviations formally dispositioned.

Record gate, decision, evidence references, unresolved holds, approver and date in `templates/review-record.csv`. The toolkit does not automatically approve any gate.

## Input completeness is a reviewed decision

The templates are starter registers, not a universal assurance that no information is missing. Extend them for seawater, contaminated service, hybrid/plume-abatement systems, seismic conditions, extreme weather, hazardous areas, proprietary specifications and unusual legal requirements. Run an interdisciplinary review for each actual project.
