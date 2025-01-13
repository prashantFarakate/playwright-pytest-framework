# playwright-pytest-framework
Scalable Web Automation framework using Playwright and Pytest for robust end-to-end testing.

Key Features:
------------
- Page Object Model (POM) implementation for better maintainability
- Pytest fixtures for common setup/teardown operations
- Parallel test execution support
- Detailed HTML reports 
- Custom pytest markers for test categorization
- Data-driven testing

Tech Stack:
----------
- Python 3.12
- Playwright
- Pytest
- pytest-xdist (parallel execution)
- pytest-html (reporting)

Project Structure:
----------------
tests/
├── conftest.py          # Pytest configurations and fixtures
├── pages/               # Page Object Model implementations
│   ├── __init__.py
│   ├── base_page.py     # Base page with common methods
│   └── login_page.py    # Page specific implementations
├── tests/               # Test implementations
│   ├── __init__.py
│   └── test_login.py    # Test cases
├── data/                # Test data files
│   └── test_data.json
├── utils/               # Helper functions and utilities
│   ├── __init__.py
│   └── config_reader.py
├── configurations/      # Configuration files
│   └── config.ini
└── reports/report.html  # Test execution reports


