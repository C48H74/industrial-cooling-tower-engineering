# Engineering quality and acceptance plan

## Roles and evidence

The owner approves process conditions, availability and contractual criteria. The process engineer establishes thermal cases. The supplier guarantees equipment performance and provides curves and loads. Mechanical, piping, civil, electrical and controls engineers verify their interfaces. Water-treatment and HSE specialists close chemical, sanitary and environmental requirements. The test agency executes the agreed test. Named personnel and approval authority must be assigned by the project; this repository does not appoint them.

For every requirement record an ID, source, exact applicable edition/clause when available, acceptance criterion, evidence artifact, checker, status and deviation. `templates/requirements-traceability.csv` contains this structure. A source link without an applicable requirement or evidence is not a compliance record.

## Independent check scope

Check units and basis; duty/simultaneity; mass/energy/solute balances; psychrometric states; positive enthalpy potential; numerical convergence; fill correlation domain; fan actual state and stable envelope; electrical power boundary; full hydraulic head and NPSH; water chemistry/materials; distribution and basin; layout and maintenance; availability; instrument uncertainty; statutory requirements and acceptance method.

Independent engineering verification by competent project reviewers is required for release decisions. Automated tests validate limited implementation behaviors; they do not provide that engineering approval.

## Design changes

Version assumptions, inputs, scripts and output together. Any change to climate, water composition, fill, fan, layout, operating cases or standards requires impact review. Do not reuse old outputs after changing inputs. Record revised results and review affected procurement guarantees and interfaces.

## Inspection and test planning

Before procurement, agree on inspection points for materials, dimensions, rotating assembly, distribution, electrical controls and civil interfaces. Before acceptance testing, agree on protocol, edition, test point, permissible conditions, stabilization, calibration, sensor placement, data handling, correction method, uncertainty and contractual disposition. Hold/witness points and tolerances must be contractual, not invented defaults.

Before startup, confirm basin/pipe cleanliness, equipment rotation, balance, guards, safe isolation, instrument calibration, distribution, pump behavior, treatment program, training and records. Confirm statutory sanitary requirements with the competent local party.

## Nonconformities

A failed test or missing evidence remains open until dispositioned. Record discrepancy, cause, risk, corrective action, owner, due date, retest evidence and approval. Do not turn an assumption into as-built data to close a hold. Do not claim compliance merely because a document name is listed.

## Evidence retention

Keep raw field measurements, instrument certificates, test calculations, vendor revisions, approvals and change records in the project's controlled document system. Do not publish proprietary facility layouts, water analyses, personal information or confidential supplier data without authorization. Public examples should be synthetic or cleared for disclosure and clearly labeled.
