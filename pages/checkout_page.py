from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Seletores de navegação do Checkout (Step 3 e 4)
    PROCEED_BUTTON = (By.CSS_SELECTOR, "button[data-test='proceed-3']")
    PAYMENT_METHOD_SELECT = (By.CSS_SELECTOR, "select[data-test='payment-method']")
    
    # Campos de Cartão de Crédito
    CREDIT_CARD_NUMBER = (By.CSS_SELECTOR, "input[data-test='credit_card_number']")
    EXPIRATION_DATE = (By.CSS_SELECTOR, "input[data-test='expiration_date']")
    CVV = (By.CSS_SELECTOR, "input[data-test='cvv']")
    CARD_HOLDER_NAME = (By.CSS_SELECTOR, "input[data-test='card_holder_name']")
    
    # Campos de Bank Transfer
    BANK_NAME = (By.CSS_SELECTOR, "input[data-test='bank_name']")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "input[data-test='account_name']")
    ACCOUNT_NUMBER = (By.CSS_SELECTOR, "input[data-test='account_number']")
    
    # Botão de Confirmação e Comprovante
    CONFIRM_PAYMENT_BTN = (By.CSS_SELECTOR, "button[data-test='finish']")
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, "div[data-test='order-confirmation']")
    
    # Mensagens de Erro / Alertas
    UNKNOWN_ERROR = (By.CSS_SELECTOR, ".alert-danger")

    def avancar_para_pagamento(self):
        self.clicar(self.PROCEED_BUTTON)

    def selecionar_metodo_pagamento(self, metodo):
        select_elem = self.encontrar_elemento(self.PAYMENT_METHOD_SELECT)
        select_elem.send_keys(metodo)

    def preencher_cartao_credito(self):
        self.preencher(self.CREDIT_CARD_NUMBER, "1234567812345678")
        self.preencher(self.EXPIRATION_DATE, "12/28")
        self.preencher(self.CVV, "123")
        self.preencher(self.CARD_HOLDER_NAME, "Enzo Coelho")

    def preencher_bank_transfer(self):
        self.preencher(self.BANK_NAME, "Banco do Brasil")
        self.preencher(self.ACCOUNT_NAME, "Enzo Coelho")
        self.preencher(self.ACCOUNT_NUMBER, "98765-4")

    def confirmar_pagamento(self):
        self.clicar(self.CONFIRM_PAYMENT_BTN)

    def validar_pedido_sucesso(self):
        return self.encontrar_elemento(self.ORDER_CONFIRMATION).is_displayed()