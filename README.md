# Project-Playwright-SwagLabs

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Automation-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reports-FF6E00?style=for-the-badge&logo=qameta&logoColor=white)
![Tests](https://github.com/indhrradvs/Project-Playwright-SwagLabs/actions/workflows/tests.yml/badge.svg)

A Playwright + Python test automation framework built using the Page Object Model (POM), targeting the SwagLabs demo site ([saucedemo.com](https://www.saucedemo.com)).

## Table of Contents

- [Highlights](#highlights)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Running Tests](#running-tests)
  - [Parallel Execution](#parallel-execution)
  - [Handling Flaky Tests](#handling-flaky-tests)
- [Code Quality](#code-quality)
- [Allure Reports](#allure-reports)
- [Running with Docker](#running-with-docker)
- [CI/CD](#cicd)
- [Branching Workflow](#branching-workflow)
- [Glossary](#glossary)

## Highlights

- 🧩 **Page Object Model** — one class per screen, clean separation of locators and actions
- 🌐 **Cross-browser** — Chromium, Firefox, WebKit
- ⚡ **Parallel execution** — full suite in ~1 minute via `pytest-xdist`
- 📊 **Allure reporting** — rich, browsable test reports, locally and in CI
- 🐳 **Dockerized** — runs identically on any machine with Docker installed
- 🔁 **CI/CD** — GitHub Actions, running on every push, PR, schedule, and on demand
- ✅ **Code quality enforced** — `black` + `flake8` via pre-commit hooks

## Tech Stack

- **Language:** Python 3
- **Test runner:** pytest
- **Browser automation:** Playwright (via `pytest-playwright`)
- **Reporting:** Allure (`allure-pytest`, `allure-pytest-auto`)
- **CI/CD:** GitHub Actions
- **Design pattern:** Page Object Model (POM)

## Project Structure

```
Project-Playwright-SwagLabs/
├── pages/ # Page objects (locators + actions, one class per screen)
├── tests/ # Test files
├── config/ # Environment settings (reads .env)
├── utils/ # Shared helpers (e.g. logger)
├── conftest.py # pytest fixtures (login, cart, checkout chains)
├── pytest.ini # pytest configuration
├── requirements.txt # Python dependencies
├── allure_pytest_auto.toml # Allure report configuration
└── .github/workflows/ # CI pipeline (GitHub Actions)
```
## Setup

```bash
# Clone and enter the project
git clone <repo-url>
cd Project-Playwright-SwagLabs

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install
```

## Environment Variables

Create a `.env` file in the project root (not committed to git):

BASE_URL=https://www.saucedemo.com
SWAGLABS_USERNAME=standard_user
SWAGLABS_PASSWORD=secret_sauce


## Running Tests

```bash
# Run the full suite
pytest

# Run a specific file
pytest tests/test_login.py

# Run with a visible browser
pytest --headed

# Slow down actions, to watch execution
pytest --headed --slowmo 500
```

### Parallel Execution

Tests run in parallel by default (`pytest-xdist`), splitting the suite across multiple workers to reduce total run time.

```bash
pytest              # runs with the configured default (-n 8, set in pytest.ini)
pytest -n 4          # override: run with a specific number of workers
pytest -n auto       # override: auto-detect available CPU cores
```

**Local benchmark** (102 tests, 3 browsers):

| Mode | Time |
|---|---|
| Sequential (no `-n`) | ~124s |
| Parallel (`-n 8`) | ~56-93s |

**Note:** CI uses `-n auto` instead of a hardcoded number, since GitHub's runners may have a different core count than your local machine. Command-line flags override `pytest.ini` defaults.

### Handling Flaky Tests

`pytest-rerunfailures` automatically retries failed tests (configured via `--reruns 2` in `pytest.ini`), absorbing transient issues like network blips without masking genuine bugs — a real failure still fails after all retries are exhausted.

## Code Quality

This project uses `black` and `flake8` to keep code style consistent, enforced automatically via pre-commit hooks.

```bash
# Format code
black .

# Check for lint issues
flake8 .

# Install the git hook (one-time setup)
pre-commit install

# Manually run hooks against all files
pre-commit run --all-files
```

Once installed, `black` and `flake8` run automatically before every `git commit` — formatting issues are auto-fixed, lint issues block the commit until resolved.

## Allure Reports

```bash
# Run tests and generate Allure results
pytest --alluredir=allure-results --allure-pytest-auto-config=allure_pytest_auto.toml

# Open the generated report
allure open allure-report
```

**Requirements:** Allure CLI must be installed separately (Mac: `brew install allure`).

## Running with Docker

The framework can run inside a Docker container — same environment (Python, packages, browsers) on any machine (Mac, Windows, Linux), no manual setup needed beyond Docker itself.

### Prerequisites

- Docker Desktop installed and running ([docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/))
- A `.env` file in the project root (same as local setup — not committed to git, must be created fresh on each machine)

### Build the image

```bash
docker build -t swaglabs-tests .
```

### Run the tests

```bash
docker run --env-file .env swaglabs-tests
```

### Run and save the Allure report to your local machine

By default, anything generated inside a container (like the Allure report) is lost once the container stops. To persist the report on your actual machine, mount a local folder into the container:

```bash
docker run --env-file .env -v $(pwd)/allure-report:/app/allure-report swaglabs-tests
```

The report will then be available locally at `allure-report/<timestamp>/`, viewable via:

```bash
allure open allure-report/<timestamp-folder>
```

### Notes

- The image is based on `mcr.microsoft.com/playwright/python`, version-matched to the `playwright` version in `requirements.txt` (versions must match, or Playwright cannot locate browser executables)
- Java (`default-jre`) and `wget`/`unzip` are installed in the image, required for the Allure CLI
- `.dockerignore` excludes `venv/`, `.git/`, `.env`, and other local-only files from the image

## CI/CD

Tests run automatically via GitHub Actions on:
- Every push
- Every pull request
- A daily schedule
- Manual trigger (`workflow_dispatch`, via the Actions tab)

Credentials are provided via GitHub Secrets (`BASE_URL`, `SWAGLABS_USERNAME`, `SWAGLABS_PASSWORD`).

### Workflow steps, explained

1. **Checkout code** — pulls this repo onto GitHub's temporary runner
2. **Set up Python** — installs Python 3.11
3. **Install dependencies** — installs pip packages + Playwright browser binaries
4. **Install Allure CLI** — downloads the Allure command-line tool (not a pip package; Ubuntu runners have no Homebrew, so it's fetched directly from Maven)
5. **Run tests** — runs the full suite (Chromium, Firefox, WebKit, in parallel) with credentials from GitHub Secrets
6. **Generate Allure Report** — builds the browsable HTML report from raw results
7. **Upload Allure Report** — attaches the report to this run as a downloadable artifact (auto-expires after 7 days)

## Branching Workflow

- `main` — always in a working, tested state
- `feature/<name>` — one branch per page/feature, merged via PR after CI passes

## Glossary

- **Faker** — a Python library that generates realistic fake data (names, addresses, emails, etc.) for tests, instead of using fixed hardcoded values.
- **Linting** — automated static analysis that flags style issues, unused code, and potential bugs without running the code (this project uses `flake8`).
- **Formatting** — automatically rewriting code to a consistent style (spacing, quotes, line breaks) — this project uses `black`, which fixes style issues rather than just flagging them.
- **Pre-commit hooks** — scripts that run automatically before a `git commit` completes, used here to enforce linting/formatting on every commit without relying on remembering to run the tools manually.
- **Rerun failures (`pytest-rerunfailures`)** — a pytest plugin that automatically retries failed tests a set number of times, absorbing transient/flaky failures (e.g. network blips) while still reporting genuine, reproducible bugs as failures.
