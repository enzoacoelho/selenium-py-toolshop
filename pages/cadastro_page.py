from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CadastroPage(BasePage):
    BTN_NAV_SIGN_IN = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")
    LINK_REGISTER = (By.CSS_SELECTOR, "[data-test='register-link']")
    
    INPUT_NOME = (By.CSS_SELECTOR, '[data-test="first-name"]')
    INPUT_SOBRENOME = (By.CSS_SELECTOR, '[data-test="last-name"]')
    INPUT_NASCIMENTO = (By.CSS_SELECTOR, '[data-test="dob"]')
    SELECT_PAIS = (By.CSS_SELECTOR, '[data-test="country"]')
    INPUT_CEP = (By.CSS_SELECTOR, '[data-test="postal_code"]')
    INPUT_NUMERO_CASA = (By.CSS_SELECTOR, '[data-test="house_number"]')
    INPUT_RUA = (By.CSS_SELECTOR, '[data-test="street"]')
    INPUT_CIDADE = (By.CSS_SELECTOR, '[data-test="city"]')
    INPUT_ESTADO = (By.CSS_SELECTOR, '[data-test="state"]')
    INPUT_TELEFONE = (By.CSS_SELECTOR, '[data-test="phone"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, '[data-test="email"]')
    INPUT_SENHA = (By.CSS_SELECTOR, '[data-test="password"]')
    BTN_CADASTRAR = (By.CSS_SELECTOR, '[data-test="register-submit"]')

    # Alertas e mensagens mapeadas
    ALERTA = (By.CSS_SELECTOR, '.alert, .invalid-feedback, div[role="alert"]')
    ALERTA_NOME = (By.CSS_SELECTOR, '[data-test="first-name-error"], div:has(> [data-test="first-name"]) .invalid-feedback')
    ALERTA_NASCIMENTO = (By.CSS_SELECTOR, '[data-test="dob-error"], div:has(> [data-test="dob"]) .invalid-feedback')
    ALERTA_SENHA = (By.CSS_SELECTOR, '[data-test="password-error"], div:has(> [data-test="password"]) .invalid-feedback')

    MENSAGENS = {
        'emailExistente': 'E-mail already exists',
        'nomeObrigatorio': 'First name is required',
        'senhaMinCaracteres': 'password'
    }

    def acessar_pagina_cadastro(self):
        self.driver.get("https://practicesoftwaretesting.com/")
        self.clicar(self.BTN_NAV_SIGN_IN)
        self.clicar(self.LINK_REGISTER)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.INPUT_NOME)
        )

    def preencher_formulario(self, dados):
        if "nome" in dados: self.preencher(self.INPUT_NOME, dados["nome"])
        if "sobrenome" in dados: self.preencher(self.INPUT_SOBRENOME, dados["sobrenome"])
        if "nascimento" in dados: self.preencher(self.INPUT_NASCIMENTO, dados["nascimento"])
        if "pais" in dados:
            Select(self.encontrar(self.SELECT_PAIS)).select_by_visible_text(dados["pais"])
        if "cep" in dados: self.preencher(self.INPUT_CEP, dados["cep"])
        if "numero_casa" in dados: self.preencher(self.INPUT_NUMERO_CASA, dados["numero_casa"])
        if "rua" in dados: self.preencher(self.INPUT_RUA, dados["rua"])
        if "cidade" in dados: self.preencher(self.INPUT_CIDADE, dados["cidade"])
        if "estado" in dados: self.preencher(self.INPUT_ESTADO, dados["estado"])
        if "telefone" in dados: self.preencher(self.INPUT_TELEFONE, dados["telefone"])
        if "email" in dados: self.preencher(self.INPUT_EMAIL, dados["email"])
        if "senha" in dados: self.preencher(self.INPUT_SENHA, dados["senha"])

    def clicar_registrar(self):
        self.clicar(self.BTN_CADASTRAR)