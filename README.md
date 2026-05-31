# eBay UI Automation Suite

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.57.0-000000)
![Pytest](https://img.shields.io/badge/Pytest-8.4.2-000000)
![Allure](https://img.shields.io/badge/Allure-2.16.0-blue)

## Project Overview

This repository contains an end-to-end UI automation suite for eBay built with Python, Playwright, and Pytest.

The tests are organized around page objects, reusable flow modules, and data-driven execution to validate core shopping functionality.

## Tech Stack

- Python
- Playwright
- Pytest
- Allure Test Reporting
- dotenv for environment configuration

## Prerequisites

Before running the suite, make sure you have the following installed:

- Python 3.11 or higher
- Node.js and npm (required for Allure CLI)
- `pip` package manager

## Installation

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:

```bash
playwright install
```

3. Install Allure command-line tool (required for serving reports):

Windows (via Scoop):

```bash
scoop install allure
```

macOS (via Homebrew):

```bash
brew install allure
```

Alternative (via Node.js/npm - Cross-Platform):
If you already have Node.js installed, you can use npm:

```bash
npm install -g allure-commandline
```

## Environment Variables Setup

This repository includes an `env.example` file at the project root.

1. Copy `env.example` to `.env` using the terminal:

```bash
cp env.example .env
```

2. Update the `.env` file with your personal eBay credentials and site configuration.

Example contents:

```env
EMAIL=your_email@example.com
PASSWORD=your_password
BASE_URL=https://www.ebay.com
```

> Note: The project currently reads the `EMAIL` and `PASSWORD` variables from `.env`. If you prefer `EBAY_EMAIL` / `EBAY_PASSWORD`, update your test configuration accordingly.

## Assumptions & Technical Decisions

The suite is designed with the following assumptions in mind:

- **Cart Cleanup**: A teardown process automatically clears the shopping cart at the end of the test execution.
- **Manual CAPTCHA Intervention**: eBay frequently presents CAPTCHA challenges. The test is intentionally designed to pause and require manual CAPTCHA resolution before it continues.
- **Default Quantity**: The tested product quantity remains at the default value of `1` throughout the flow.

## Running Tests

Execute the suite and generate raw Allure results with:

```bash
pytest --alluredir=allure-results
```

## Viewing Allure Reports

Serve and open the Allure HTML report locally with:

```bash
allure serve allure-results
```

## Demo & Proof of Execution

A sample demo video is available for reference:

- [ebay_automation_demo.mp4](./ebay_automation_demo.mp4)

This video demonstrates a successful test execution and can help troubleshoot local execution issues.

## Project Structure

- `src/pages/` — Page object implementations
- `src/flows/` — Reusable business flows for login, search, product interaction, and checkout
- `src/utils/` — Utility helpers and data loaders
- `tests/e2e/` — End-to-end test scenarios
- `allure-results/` — Generated Allure raw results


## Bug Fixing & Analysis Task

As part of the assignment requirements, a static code analysis was performed on a sample test script provided by a colleague.

- **Task Reference**: See the full analysis, identified issues, and suggested improvements in the ReadMeAIBugs.md file.