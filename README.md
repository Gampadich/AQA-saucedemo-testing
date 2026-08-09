# SauceDemo UI Test Automation

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Sync%20API-2EAD33?logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reporting-FF6E00?logo=qameta&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

A compact UI test automation project for the [SauceDemo](https://www.saucedemo.com/) demo store, built with **Playwright** and **Pytest**, structured around the **Page Object Model (POM)** pattern, with test reporting via **Allure**.

---

## About the Project

This suite automates key user flows on SauceDemo — login (positive and negative), product sorting, and adding items to the cart. Each page of the application is represented as a separate class (`LoginPage`, `ProductsPage`) encapsulating its locators and actions, keeping the test files focused purely on assertions and scenario logic.

Every test step is wrapped with `@allure.step`, and each test is annotated with `@allure.feature`, `@allure.story`, and `@allure.severity`, producing a clean, readable Allure report.

---

## Tech Stack

- **Python** — core language
- **Playwright (Sync API)** — browser automation
- **Pytest** — test runner and fixtures
- **Allure Framework** (`allure-pytest`) — test reporting
- **Page Object Model** — architecture pattern for maintainable page interactions

---

## Test Coverage

| Test | Feature | Story | Severity |
|------|---------|-------|----------|
| `test_login_and_visible_title` | Authorization | Successful user login | 🔴 Critical |
| `test_check_first_product_after_sort` | Products page | Verifying the lowest product price after sorting | 🟢 Minor |
| `test_negative_login` | Authorization | Login with invalid credentials | 🟡 Normal |
| `test_adding_product_to_cart` | Products page | Product successfully appears in the cart | 🔴 Critical |

**What's verified:**
1. **Login & title check** — logs in with valid credentials (`standard_user` / `secret_sauce`) and asserts the `Products` page title is visible.
2. **Sorting by price** — selects the "low to high" sort option and asserts the first product's price equals `$7.99`.
3. **Negative login** — attempts login with invalid credentials and asserts the error message (`h3[data-test="error"]`) is visible.
4. **Add to cart** — adds the Sauce Labs Backpack to the cart and asserts the cart badge becomes visible.

---

## Project Structure

```
.
├── classes/
│   ├── login.py            # LoginPage — locators & login() action
│   └── products_page.py    # ProductsPage — locators & page actions
├── tests/
│   └── test_saucedemo.py   # Test scenarios
├── conftest.py              # Shared fixtures (e.g. base `url`)
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Project dependencies
└── README.md
```

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers**

```bash
playwright install
```

---

##  Running the Tests

Run the whole suite:

```bash
pytest
```

Run with Allure results collection:

```bash
pytest --alluredir=allure-results
```

Generate and open the Allure report (requires [Allure Commandline](https://allurereport.org/docs/gettingstarted-installation/) installed separately):

```bash
allure serve allure-results
```

---

## Configuration Notes

- `pytest.ini` sets `pythonpath = .` so `classes/` can be imported directly in tests without extra path hacks.
- The `url` fixture (session-scoped) provides the base SauceDemo URL (`https://www.saucedemo.com/`) to every test, keeping the target environment configurable in one place.
- No API keys, secrets, or local backend are required — all tests run against the live public SauceDemo demo site.

---

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.