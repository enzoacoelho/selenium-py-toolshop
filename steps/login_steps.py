from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from urllib.parse import urlparse
import time

@given('que estou na página de login da aplicação')
def step_que_estou_na_pagina_de_login(context):
    context.driver.get("https://practicesoftwaretesting.com/#/")
    context.login_page = LoginPage(context.driver)
    context.login_page.clicar((By.CSS_SELECTOR, "a[data-test='nav-sign-in']"))

@when('preencho o campo de e-mail com "{email}"')
def step_preencho_email(context, email):
    context.login_page.preencher_email(email)

@when('preencho o campo de senha com "{senha}"')
def step_preencho_senha(context, senha):
    context.login_page.preencher_senha(senha)

@when('deixo os campos de e-mail e senha em branco')
def step_deixo_campos_em_branco(context):
    pass

@when('clico no botão de login')
def step_clico_login(context):
    context.login_page.clicar_login()

@then('devo ser redirecionado para a página da minha conta "{url_esperada}"')
def step_validar_redirecionamento(context, url_esperada):
    from selenium.webdriver.support.ui import WebDriverWait
    
    # Aguarda a URL conter o caminho esperado (ex: /account)
    WebDriverWait(context.driver, 5).until(
        lambda driver: url_esperada in driver.current_url
    )
    assert url_esperada in context.driver.current_url, \
        f"Esperado redirecionamento para {url_esperada}, mas estava em {context.driver.current_url}"
@then('devo ver a mensagem de erro de autenticação "{msg_esperada}"')
def step_validar_mensagem_erro(context, msg_esperada):
    msg_obtida = context.login_page.obter_mensagem_erro()
    assert msg_esperada in msg_obtida, f"Esperado '{msg_esperada}', mas obteve '{msg_obtida}'"

@then('devo ver as mensagens de obrigatoriedade abaixo dos campos de e-mail e senha')
def step_validar_alertas_obrigatoriedade(context):
    assert context.login_page.validar_alertas_campos_vazios(), "Alertas de campos obrigatórios não exibidos."

@given('que estou autenticado no sistema com credenciais válidas')
def step_autenticado_validas(context):
    context.driver.get("https://practicesoftwaretesting.com/#/")
    context.login_page = LoginPage(context.driver)
    context.login_page.clicar((By.CSS_SELECTOR, "a[data-test='nav-sign-in']"))
    context.login_page.preencher_email("customer@practicesoftwaretesting.com")
    context.login_page.preencher_senha("welcome01")
    context.login_page.clicar_login()

@when('aciono a opção de encerramento de sessão "{opcao}"')
def step_fazer_logout(context, opcao):
    context.login_page.fazer_logout()

@then('devo ser redirecionado para a tela de login')
def step_redirecionado_tela_login(context):
    time.sleep(2)  # Dá o respiro para o SPA processar a rota
    current_url = context.driver.current_url
    assert "account" not in current_url, f"Ainda preso na área logada! URL atual: {current_url}"
