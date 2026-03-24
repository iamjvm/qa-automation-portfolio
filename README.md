# QA Automation Portfolio — Janhavi Morajkar

Selenium WebDriver + Python + pytest automation framework
built from scratch on 24th March 2026.

## Tech Stack
- Python 3.12.6
- Selenium WebDriver 4.41.0
- pytest + pytest-html
- webdriver-manager
- Page Object Model design pattern

## Test Coverage
- 10 automated test cases for guru99 Bank Login module
- Tests run in Chrome via ChromeDriver
- HTML reports generated automatically

## How to Run
pip install -r requirements.txt
pytest tests/ -v --html=reports/reports.html --self-contained-html

## Structure
tests/       → test files
pages/       → Page Object classes
reports/     → HTML test reports
conftest.py  → shared fixtures
