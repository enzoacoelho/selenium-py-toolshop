from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CarrinhoPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='add-to-cart']")
    NAV_CART_BTN = (By.CSS_SELECTOR, "a[data-test='nav-cart']")
    CART_QUANTITY_INPUT = (By.CSS_SELECTOR, "input[data-test='product-quantity']")
    PROCEED_CHECKOUT_BTN = (By.CSS_SELECTOR, "button[data-test='proceed-1']")

    def adicionar_primeiro_produto(self):
        # Entra no primeiro produto disponível e adiciona ao carrinho
        self.clicar((By.CSS_SELECTOR, ".card-img-top"))
        self.clicar(self.ADD_TO_CART_BTN)

    def ir_para_carrinho(self):
        self.clicar(self.NAV_CART_BTN)