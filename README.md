This is a vary basic example of mobile test automation framework.
This architecture scales pretty good and allows us to write clean and straightforward test cases.
`conftest.py` file contains couple page fixtures and corresponding classes
Element class is basically a collection of methods for screen elements like `click`, `type`, `is_enabled`, etc.
Every application screen is also a class that holds screen elements. Each element should be initialized with a locator, this small example supports only accessability_id.
Page fixture yealds initialized screen class.
Driver class is out of scope, but it should establish Appium connection