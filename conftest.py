import pytest
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy


class Element:
    def __init__(self, driver, accessability_id):
        self.driver = driver
        self.accessability_id = accessability_id

    def get_element(self) -> WebElement:
        """
        Find element by given locator.
        Should be enhanced to support different locator types.
        """
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.accessability_id)

    def click(self) -> None:
        """
        Find element and click on it.
        """
        self.get_element().click()

    def type(self, text) -> None:
        """
        Find unput field, click and send text to it
        """
        element = self.get_element()
        element.click()
        element.send_keys(text)

    def is_enabled(self) -> bool:
        """
        Check if element is active
        """
        self.get_element().is_enabled()

    def is_displayed(self) -> bool:
        """
        Check if element is rendered
        """
        self.get_element().is_displayed()


class LoginPage:
    def __init__(self, driver):
        # Page elements
        self.button_submit = Element(driver=driver, accessability_id="#submit")
        self.field_email = Element(driver=driver, accessability_id="#email")
        self.field_password = Element(driver=driver, accessability_id="#pass")

    def is_correct(self):
        assert self.button_submit.is_displayed()
        assert self.field_email.is_displayed()
        assert self.field_password.is_displayed()


class DashboardPage:
    def __init__(self, driver):
        # Page elements
        self.title = Element(driver=driver, accessability_id="#title")

    def is_correct(self):
        assert self.title.is_displayed()


@pytest.fixture(scope="session")
def driver():
    """
    Init selenium/Appuim driver
    Launch the app
    """
    pass


@pytest.fixture(scope="session")
def login_page(driver):
    yield LoginPage(driver=driver)


@pytest.fixture(scope="session")
def dashboard_page(driver):
    yield DashboardPage(driver=driver)
