from behave import given, when, then
from pages.catalogo_page import CatalogoPage

@given('que estou na página inicial do catálogo da loja')
def step_pagina_inicial(context):
    context.driver.get("https://practicesoftwaretesting.com/#/")
    context.catalogo_page = CatalogoPage(context.driver)

@when('busco pelo termo "{termo}" na barra de pesquisa')
def step_buscar_termo(context, termo):
    context.catalogo_page.buscar_produto(termo)

@then('o catálogo deve retornar apenas os produtos correspondentes à busca')
def step_validar_busca_sucesso(context):
    assert context.catalogo_page.obter_quantidade_produtos() > 0

@when('busco por um termo que não existe no catálogo, como "{termo}"')
def step_buscar_termo_inexistente(context, termo):
    context.catalogo_page.buscar_produto(termo)

@then('devo ver a mensagem informando que nenhum resultado foi encontrado')
def step_validar_sem_resultados(context):
    assert context.catalogo_page.obter_quantidade_produtos() == 0