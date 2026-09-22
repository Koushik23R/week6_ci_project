# AI/ML Machine Learning Pipeline with Continuous Integration (CI)

An enterprise-ready Python ML feature processing and evaluation engine integrated with a GitHub Actions CI pipeline for automated code linting, unit testing, and 98% coverage tracking.

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

### Test Suite & Coverage

    pytest tests/ -v --cov=src/ml_pipeline --cov-report=term-missing

---

## CI Pipeline Summary

The project uses GitHub Actions to automate the following development workflow:

**Code Push / Pull Request → Repository Checkout → Python Environment Setup → Dependency Installation → Flake8 Linting → Automated Testing → Coverage Analysis**

The CI pipeline helps ensure that code quality and automated tests are verified consistently before changes are accepted into the main branch.

---

## Testing and Quality Metrics

| Metric | Result |
|---|---:|
| **Automated Tests** | 10 |
| **Tests Passed** | 10 |
| **Test Failures** | 0 |
| **Code Coverage** | 98% |
| **Flake8 Errors** | 0 |
| **CI Status** | **PASS** |