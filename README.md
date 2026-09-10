# Project-Playwright-SwagLabs

A Playwright + Python test automation framework built using the Page Object Model (POM), targeting the SwagLabs demo site ([saucedemo.com](https://www.saucedemo.com)).

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

## Allure Reports

```bash
# Run tests and generate Allure results
pytest --alluredir=allure-results --allure-pytest-auto-config=allure_pytest_auto.toml

# Open the generated report
allure open allure-report
```

**Requirements:** Allure CLI must be installed separately (Mac: `brew install allure`).

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
5. **Run tests** — runs the full suite (Chromium, Firefox, WebKit) with credentials from GitHub Secrets
6. **Generate Allure Report** — builds the browsable HTML report from raw results
7. **Upload Allure Report** — attaches the report to this run as a downloadable artifact (auto-expires after 7 days)

## Branching Workflow

- `main` — always in a working, tested state
- `feature/<name>` — one branch per page/feature, merged via PR after CI passes

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

## Planned Enhancements
- BDD/Cucumber-style tests (exploratory, separate learning project)
