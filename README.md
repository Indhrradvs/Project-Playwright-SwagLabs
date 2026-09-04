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

## Branching Workflow

- `main` — always in a working, tested state
- `feature/<name>` — one branch per page/feature, merged via PR after CI passes

## Planned Enhancements

- Cross-browser testing (Chromium, Firefox, WebKit)
- Dynamic price calculation (replace hardcoded checkout totals)
- CSS/visual styling checks
- Fixture scoping for faster test runs (session-level login reuse)
- Docker support (cross-platform runs, including Windows)
- BDD/Cucumber-style tests (exploratory, separate learning project)
