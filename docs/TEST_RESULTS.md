# Week 6 Automated Test Execution & Coverage Report

## Environment Specifications

- **Local Python Version:** Python 3.13.3
- **CI Python Version:** Python 3.11
- **Test Framework:** `pytest` 9.1.1 + `pytest-cov` 7.1.0
- **Linter:** `flake8`
- **Execution Command:** `pytest tests/ -v --cov=src/ml_pipeline --cov-report=term-missing --cov-fail-under=95`
- **Dependencies:** Installed with `pip install -r requirements.txt`

---

## Flake8 Linting Verification Log

    $ flake8 src tests
    # Output: 0 errors / 0 warnings (100% PEP 8 Compliant)

---

## Pytest Execution Terminal Log

    ==================================== test session starts ====================================
    platform win32 -- Python 3.13.3, pytest-9.1.1, pluggy-1.6.0
    rootdir: D:\INTERNSHIP\YUVA_INTERN\week6_ci_project
    plugins: anyio-4.14.2, cov-7.1.0
    collected 10 items

    tests/test_pipeline.py::TestFeatureScaler::test_standard_scale_constant_values PASSED      [ 10%]
    tests/test_pipeline.py::TestFeatureScaler::test_standard_scale_empty_list PASSED           [ 20%]
    tests/test_pipeline.py::TestFeatureScaler::test_standard_scale_invalid_element PASSED      [ 30%]
    tests/test_pipeline.py::TestFeatureScaler::test_standard_scale_invalid_type PASSED         [ 40%]
    tests/test_pipeline.py::TestFeatureScaler::test_standard_scale_success PASSED              [ 50%]
    tests/test_pipeline.py::TestModelEvaluator::test_evaluate_binary_classification_success PASSED [ 60%]
    tests/test_pipeline.py::TestModelEvaluator::test_evaluate_empty_dataset PASSED             [ 70%]
    tests/test_pipeline.py::TestModelEvaluator::test_evaluate_invalid_label_values PASSED      [ 80%]
    tests/test_pipeline.py::TestModelEvaluator::test_evaluate_mismatched_lengths PASSED        [ 90%]
    tests/test_pipeline.py::TestMLPipelineIntegration::test_pipeline_end_to_end_success PASSED [100%]

    ===================================== tests coverage =====================================
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    src\ml_pipeline\__init__.py       0      0   100%
    src\ml_pipeline\core.py          52      1    98%   40
    -----------------------------------------------------------
    TOTAL                            52      1    98%
    ================================= 10 passed in 0.50s =================================

---

## Execution Metrics Summary

| Metric | Result |
|---|---:|
| **Total Tests Executed** | 10 |
| **Passed** | 10 |
| **Failures / Errors** | 0 |
| **Code Coverage** | 98% |
| **Flake8 Lint Errors** | 0 |
| **Overall Status** | **PASS** |

---

## Conclusion

The automated test suite completed successfully with **10 out of 10 tests passing** and no failures or errors. The project achieved **98% code coverage**, exceeding the enforced CI minimum of 95%, while Flake8 reported **zero linting errors or warnings**. CI generates `coverage.xml` and uploads it as the `coverage-report` artifact. These results confirm that the tested functionality is working as expected and meets the defined code-quality and testing requirements.

## CI Verification

The final GitHub Actions workflow verifies checkout, Python 3.11 setup, dependency installation from `requirements.txt`, Flake8 linting, pytest execution, coverage generation, the 95% threshold, and coverage artifact upload. A failed lint, test, or coverage check causes the workflow to fail.