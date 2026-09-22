# GitHub Actions Continuous Integration (CI) Pipeline Guide

## 1. Pipeline Overview

This document details the CI pipeline setup using GitHub Actions for the `week6_ci_project` repository. The workflow automates code linting, automated testing, coverage tracking, and build verification on every commit pushed to `main`.

---

## 2. GitHub Actions Workflow Configuration (`.github/workflows/ci.yml`)

The following GitHub Actions workflow automatically checks code quality and runs the complete automated test suite:

    name: Continuous Integration Pipeline

    on:
      push:
        branches: [ "main" ]
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
            pip install flake8 pytest pytest-cov

        - name: Step 1 - Code Quality & Linting Check (flake8)
          run: |
            flake8 src tests --count --select=E9,F63,F7,F82 --show-source --statistics
            flake8 src tests --count --max-complexity=10 --max-line-length=100 --statistics

        - name: Step 2 - Execute Automated Test Suite & Coverage Report
          run: |
            pytest tests/ -v --cov=src/ml_pipeline --cov-report=term-missing --cov-report=xml

---

## 3. How to Trigger and Verify Pipeline

1. **Trigger via Git Commit:** Push any commit to the `main` branch. GitHub Actions will automatically initiate a workflow run under the **Actions** tab of the repository.

2. **Pipeline Pass Criteria:**
   - Flake8 checks return 0 syntax or PEP 8 style errors.
   - All 10 pytest cases pass.
   - Test coverage exceeds 95%.

---

## 4. CI Pipeline Process

The CI pipeline follows these automated stages:

**Code Push / Pull Request → Checkout Repository → Setup Python → Install Dependencies → Flake8 Linting → Pytest Execution → Coverage Report → Pipeline Result**

---

## 5. Expected Outcome

A successful workflow run verifies that the project can be tested automatically in a clean Ubuntu environment. The pipeline ensures consistent code quality, validates the automated test suite, and generates a coverage report for the `ml_pipeline` source code.