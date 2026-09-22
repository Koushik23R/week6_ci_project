# GitHub Actions Continuous Integration (CI) Pipeline Guide

## 1. Pipeline Overview

This document details the CI pipeline setup using GitHub Actions for the `week6_ci_project` repository. The workflow uses Python 3.11 to automate code linting, testing, coverage enforcement, and coverage artifact upload on every push and on pull requests targeting `main`.

---

## 2. GitHub Actions Workflow Configuration (`.github/workflows/ci.yml`)

The following GitHub Actions workflow automatically checks code quality and runs the complete automated test suite:

    name: Continuous Integration Pipeline

    on:
      push:
      pull_request:
        branches: [ "main" ]

    jobs:
      build-and-test:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout Source Code Repository
          uses: actions/checkout@v4

        - name: Set up Python 3.11 Environment
          uses: actions/setup-python@v5
          with:
            python-version: "3.11"

        - name: Install Dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - name: Step 1 - Code Quality & Linting Check (flake8)
          run: |
            flake8 src tests --count --select=E9,F63,F7,F82 --show-source --statistics
            flake8 src tests --count --max-complexity=10 --max-line-length=100 --statistics

        - name: Step 2 - Execute Automated Test Suite & Coverage Report
          run: |
            pytest tests/ -v --cov=src/ml_pipeline --cov-report=term-missing --cov-report=xml --cov-fail-under=95

        - name: Step 3 - Upload Coverage Report
          if: always()
          uses: actions/upload-artifact@v4
          with:
            name: coverage-report
            path: coverage.xml

---

## 3. How to Trigger and Verify Pipeline

1. **Trigger via Git Commit:** Push any commit to any branch. GitHub Actions will automatically initiate a workflow run under the **Actions** tab. Pull requests targeting `main` also trigger the workflow.

2. **Pipeline Pass Criteria:**
   - Flake8 checks return 0 syntax or PEP 8 style errors.
   - All 10 pytest cases pass.
   - Test coverage is at least 95%.
   - `coverage.xml` is uploaded as the `coverage-report` artifact.

---

## 4. CI Pipeline Process

The CI pipeline follows these automated stages:

**Code Push / Pull Request → Checkout Repository → Setup Python → Install Dependencies → Flake8 Linting → Pytest Execution → Coverage Report → Pipeline Result**

---

## 5. Expected Outcome

A successful workflow run verifies that the project can be tested automatically in a clean Ubuntu environment. The pipeline fails if linting, tests, or coverage requirements fail, and generates and uploads a coverage report for the `ml_pipeline` source code.

## Reproducing the Environment Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flake8 src tests
pytest tests/ -v --cov=src/ml_pipeline --cov-report=term-missing --cov-fail-under=95
```

## CI Verification and Troubleshooting

The CI workflow was verified through GitHub Actions runs. Initial setup required review of the project structure, dependencies, and workflow configuration so local commands and the CI environment matched. Successful runs confirmed Python 3.11 setup, dependency installation from `requirements.txt`, Flake8, pytest, the 95% coverage threshold, `coverage.xml` generation, and `coverage-report` artifact upload.

To review logs, open the repository, select **Actions**, choose **Continuous Integration Pipeline**, open a workflow run and the `build-and-test` job, then inspect each step. Download the `coverage-report` artifact from the run's **Artifacts** section.