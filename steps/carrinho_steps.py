from behave import given, when, then
from pages.carrinho_page import CarrinhoPage

@when('seleciono um produto disponível no catálogo e o adiciono ao carrinho')
def step_adicionar_produto(context):
    context.carrinho_page = CarrinhoPage(context.driver)
    context.carrinho_page.adicionar_primeiro_produto()

@then('navego até a tela do carrinho ("{rota}")')
def step_ir_para_carrinho(context, rota):
    context.carrinho_page.ir_para_carrinho()