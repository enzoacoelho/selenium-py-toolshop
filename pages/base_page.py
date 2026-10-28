from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def encontrar(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def clicar(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def preencher(self, locator, text):
        element = self.encontrar(locator)
        element.clear()
        element.send_keys(text)

    def obter_texto(self, locator):
        element = self.encontrar(locator)
        return element.text