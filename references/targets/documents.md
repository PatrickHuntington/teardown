# Documents, publications and recorded media

Treat a document as a first-class target. It may embody a method, calculation,
information architecture, argument, design system or operating workflow.
The requested output determines which of these to reverse-engineer.

## Inspect in the right representation

Identify title, author/publisher, date/version, format, pages/sheets/slides, and
whether the material is complete. Preserve locators throughout extraction:

- PDF/scanned publication: extract text and render relevant pages; inspect tables,
  equations, legends, footnotes and layout. OCR scanned pages, marking uncertain
  readings. A failed text extraction is not an empty document.
- Spreadsheet: inspect cells, formulas, named ranges, hidden sheets, validation,
  external links and units; distinguish formulas from cached displayed values.
  Work on a copy and keep macros/external refresh disabled unless requested.
- Slide deck/report/design: inspect hierarchy, typography, grids, charts, master
  patterns, assets and narrative structure according to the goal.
- Paper/technical manual: extract definitions, assumptions, algorithm steps,
  equations, required data, evaluation method and stated limitations.
- Images/screenshots/video/audio: record image/frame/timestamp locators, visible
  or audible behavior, and missing context. Transcription and OCR have uncertainty;
  verify consequential labels/numbers against the source.

Use format-aware parsers and visual inspection together when layout carries
meaning. Record producer metadata as a clue, not proof of the author's toolchain.

## Reconstruct the mechanism or pattern

Identify inputs -> transformations/rules -> outputs -> intended use. For a
methodology, trace one worked example with units and intermediate steps. For a
document design, distinguish reusable layout/communication principles from the
specific content. For an operating procedure, map actors, decisions, handoffs,
exceptions and acceptance conditions. For an argument, separate assertions,
evidence, assumptions and conclusions.

Label an author's claims as documented until independently reproduced. When
calculations or experiments are requested, check them on a representative sample
and distinguish reproduced results from untested assertions. Missing datasets,
appendices, formulas or supplementary files are explicit dependencies.

## Adapt to the outcome

- Explain: a mechanism/methodology map with page/cell references and a worked
  trace. A non-software document need not acquire an invented tech stack.
- Catalog: sections, methods, rules, requirements, templates and exceptions.
- Assess: repeatability, scarce expertise/data, validation quality and distribution
  where those matter; avoid forcing a commercial moat onto an ordinary paper.
- Recreate: an original template, reproducible calculation, software implementation
  of the method, or report pipeline as requested. Specify inputs and acceptance
  criteria before building; preserve attribution and source constraints.
- Improve: correct factual/calculation errors, expose assumptions, strengthen
  reproducibility, or improve the document's usability/design, with validation
  appropriate to the requested changes.

Screenshots and recordings can support app investigation without granting live
access. Document visible states and demonstrated transitions; hidden screens,
error paths and backend implementation remain unknown.
