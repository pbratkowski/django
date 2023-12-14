"""A Selenium ActionChains implementation that automatically scrolls to elements."""

from selenium.webdriver.common.action_chains import ActionChains


class ElementChains(ActionChains):
    """Implementation that automatically scrolls to elements."""

    def move_to_element(self, element):
        """Fix that works in Firefox."""
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return super().move_to_element(element)
