# AI/ML Machine Learning Pipeline with Continuous Integration (CI)

A Python ML feature processing and evaluation engine integrated with GitHub Actions for automated linting, testing, coverage enforcement, and coverage artifact upload.

---

## Quick Evidence Links

- **Primary Project Report:** [`WEEK6_REPORT.md`](./WEEK6_REPORT.md)
- **CI Setup & Architecture Guide:** [`docs/CI_PIPELINE_GUIDE.md`](./docs/CI_PIPELINE_GUIDE.md)
- **Terminal Execution & Coverage Logs:** [`docs/TEST_RESULTS.md`](./docs/TEST_RESULTS.md)
- **GitHub Actions Workflow File:** [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)

---

## Repository Structure

    week6_ci_project/
    ├── WEEK6_REPORT.md             # Machine-readable project summary
    ├── README.md                   # Repository overview and index
    ├── requirements.txt            # Dependencies (flake8, pytest, pytest-cov)
    ├── report.docx                 # Generated Word report
    ├── .gitignore
    ├── .github/
    │   └── workflows/
    │       └── ci.yml              # GitHub Actions CI Workflow pipeline
    ├── src/
    │   └── ml_pipeline/
    │       ├── __init__.py
    │       └── core.py             # FeatureScaler, ModelEvaluator, MLPipelineRunner
    ├── tests/
    │   ├── __init__.py
    │   └── test_pipeline.py        # 10 unit and integration tests
    └── docs/
        ├── CI_PIPELINE_GUIDE.md    # Comprehensive CI configuration guide
        └── TEST_RESULTS.md         # Terminal output & 98% coverage metrics

---

## How to Execute Pipeline Steps Locally

### Code Quality Linting

    flake8 src tests

### Create and Reproduce the CI Environment

    python -m venv venv

On Windows, activate it with:

    venv\Scripts\activate

Install the same declared dependencies used by CI:

    pip install -r requirements.txt

### Test Suite & Coverage

    pytest tests/ -v --cov=src/ml_pipeline --cov-report=term-missing --cov-fail-under=95

---

## CI Pipeline Summary

The project uses GitHub Actions with Python 3.11 to automate the following development workflow:

**Every Push / Pull Request to main → Repository Checkout → Python 3.11 Setup → requirements.txt Installation → Flake8 Linting → Pytest and Coverage → Coverage Artifact Upload**

The workflow runs on every push and on pull requests targeting `main`. Flake8, pytest, and pytest-cov are installed from `requirements.txt`. The pipeline fails when linting, tests, or the minimum 95% coverage threshold fails. The generated `coverage.xml` file is uploaded as the `coverage-report` artifact.

---

## Testing and Quality Metrics

| Metric | Result |
|---|---:|
| **Automated Tests** | 10 |
| **Tests Passed** | 10 |
| **Test Failures** | 0 |
| **Code Coverage** | 98% (minimum enforced: 95%) |
| **Flake8 Errors** | 0 |
| **CI Status** | **PASS** |

## Viewing CI Logs and Artifacts

1. Open the repository on GitHub and select the **Actions** tab.
2. Select the **Continuous Integration Pipeline** workflow and open a run.
3. Open the `build-and-test` job to review checkout, Python setup, dependency installation, linting, testing, coverage, and artifact-upload steps.
4. Download `coverage-report` from the workflow run's **Artifacts** section.

## CI Verification and Troubleshooting

The workflow was verified through GitHub Actions runs. During initial setup, the project structure, dependencies, and CI configuration were reviewed after the first verification run. Subsequent runs confirmed successful Python 3.11 setup, installation from `requirements.txt`, Flake8 checks, automated tests, coverage enforcement, `coverage.xml` generation, and artifact upload.

## CI Verification

The GitHub Actions CI pipeline was successfully verified after the final CI configuration update.