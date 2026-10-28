from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CatalogoPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-test='search-query']")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    SORT_SELECT = (By.CSS_SELECTOR, "select[data-test='sort']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".card")
    NO_RESULTS_MSG = (By.CSS_SELECTOR, "div[data-test='search-caption']")

    def buscar_produto(self, termo):
        self.preencher(self.SEARCH_INPUT, termo)
        self.clicar(self.SEARCH_BTN)

    def ordenar_por(self, opcao):
        # Mapeia a opção visual para a ação
        select_elem = self.encontrar_elemento(self.SORT_SELECT)
        select_elem.send_keys(opcao)

    def obter_quantidade_produtos(self):
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))