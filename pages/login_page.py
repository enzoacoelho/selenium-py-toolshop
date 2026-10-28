from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, '[data-test="email"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '[data-test="password"]')
    BTN_LOGIN = (By.CSS_SELECTOR, '[data-test="login-submit"]')
    VISIBILIDADE_SENHA = (By.CSS_SELECTOR, '.input-group-append > .btn')
    LINK_CADASTRAR = (By.CSS_SELECTOR, '[data-test="register-link"]')
    LINK_REDEFINIR_SENHA = (By.CSS_SELECTOR, '[data-test="forgot-password-link"]')

    ALERTA_EMAIL = (By.CSS_SELECTOR, '[data-test="email-error"] > div')
    ALERTA_SENHA = (By.CSS_SELECTOR, '[data-test="password-error"] > div')
    ALERTA_ERRO = (By.CSS_SELECTOR, '.help-block')

    BTN_MENU = (By.CSS_SELECTOR, "button[data-test='nav-menu']")
    LINK_SIGN_OUT = (By.CSS_SELECTOR, "a[data-test='nav-sign-out']")

    def preencher_email(self, email):
        self.preencher(self.INPUT_EMAIL, email)

    def preencher_senha(self, senha):
        self.preencher(self.INPUT_PASSWORD, senha)

    def clicar_login(self):
        self.clicar(self.BTN_LOGIN)

    def fazer_logout(self):
        self.clicar(self.BTN_MENU)
        self.clicar(self.LINK_SIGN_OUT)

    def obter_mensagem_erro(self):
        return self.obter_texto(self.ALERTA_ERRO)

    def validar_alertas_campos_vazios(self):
        email_vazio = self.encontrar(self.ALERTA_EMAIL).is_displayed()
        senha_vazia = self.encontrar(self.ALERTA_SENHA).is_displayed()
        return email_vazio and senha_vazia