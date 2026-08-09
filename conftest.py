import pytest

@pytest.fixture(scope='session')
def url():
    return 'https://www.saucedemo.com/'

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, 'rep_' + report.when, report)

@pytest.fixture(autouse=True, scope='function')
def attach_screenshot_on_failure(request, page):
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name='screenshot_on_failure',
            attachment_type=allure.attachment_type.PNG,
        )
