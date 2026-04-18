# Elements of AIML (CSAI2018)

This folder contains lecture slides (Beamer) and detailed teaching notes for **Elements of AIML**, along with lab experiment notes.

GitHub: `https://github.com/tali7c/Elements-of-AIML`

## Structure

- `Unit-xx/Lecture-yy/latex/`
  - `slides.tex` — Beamer slides (UPES theme)
  - `notes.tex` — Detailed lecture notes (article class)
- `Miscellaneous/Lecture-yy/latex/`
  - `slides.tex` — Supplementary Beamer slides for revision or deeper treatment
  - `notes.tex` — Supplementary detailed notes
- `Unit-xx/Lecture-yy/`
  - `slides.pdf` and `notes.pdf` — compiled outputs (when available)
- `Lab/Experiment-xx/latex/notes.tex` — experiment notes (LaTeX)
- `Lab/Experiment-xx/notes.pdf` — compiled experiment notes
- `_shared/` — common LaTeX components shared across lectures and labs

Notes:
- Large datasets are not stored here; use links or small sampled CSVs.
- Internal planning documents and local syllabus files are stored under `../admin/` (not inside this public material).

## Recommended Reading Order

- Read the theory lectures in unit order: `Unit-01` -> `Unit-02` -> `Unit-03` -> `Unit-04` -> `Unit-05`.
- Inside each unit, read `Lecture-01`, then `Lecture-02`, then `Lecture-03`; later lectures assume the earlier notation and examples.
- `Unit-02/Lecture-03` works best only after `Unit-02/Lecture-01` and `Unit-02/Lecture-02` because it assumes entailment, CNF, quantifiers, and substitution.
- `Unit-03/Lecture-03` should be read only after `Unit-03/Lecture-02` because PCA and scaling must follow the train-only / no-leakage rule from the evaluation lecture.
- `Unit-04/Lecture-03` is a survey lecture. Read it after `Unit-04/Lecture-01` and `Unit-04/Lecture-02`, and treat it as three short paradigms rather than one long method chain.
- `Unit-05/Lecture-03` is best used as a wrap-up and revision lecture after all previous theory packs.
- `Miscellaneous/Lecture-01` is a supplementary comparison lecture for `PCA`, `LDA`, and `ICA`; read it after `Unit-03/Lecture-03`.
- `Miscellaneous/Lecture-02` is a derivation lecture for eigenvalues/eigenvectors from raw sample data; read it after `Miscellaneous/Lecture-01` or alongside `Unit-03/Lecture-03`.
