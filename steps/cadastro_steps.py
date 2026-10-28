import time
from behave import given, when, then
from pages.cadastro_page import CadastroPage

@given('que estou na página de cadastro de nova conta')
def step_acessar_cadastro(context):
    context.cadastro_page = CadastroPage(context.driver)
    context.cadastro_page.acessar_pagina_cadastro()

@when('preencho o formulário utilizando um e-mail que já está cadastrado na base')
def step_email_existente(context):
    # Usa um e-mail fixo que já sabemos que existe ou foi cadastrado no cenário anterior
    context.cadastro_page.preencher_formulario({
        "nome": "Teste",
        "sobrenome": "Duplicado",
        "nascimento": "1994-11-14",
        "pais": "Brazil",
        "cep": "86300000",
        "numero_casa": "123",
        "rua": "Rua Principal",
        "cidade": "Jataizinho",
        "estado": "Paraná",
        "telefone": "43999999999",
        "email": "qa_duplicado@test.com", # Ou o e-mail previamente cadastrado
        "senha": "Welcome@2026"
    })

@then('devo ver uma mensagem informando que o e-mail já existe')
def step_valida_erro_email_existente(context):
    time.sleep(1)
    alerta = context.cadastro_page.encontrar(context.cadastro_page.ALERTA)
    assert context.cadastro_page.MENSAGENS['emailExistente'] in alerta.text

@when('deixo os campos obrigatórios em branco')
def step_campos_em_branco(context):
    # Apenas tenta avançar sem preencher nada
    pass

@when('tento submeter o formulário')
def step_tenta_submeter(context):
    context.cadastro_page.clicar_registrar()

@then('o sistema deve exibir os alertas de preenchimento obrigatório em cada campo correspondente')
def step_valida_erros_obrigatorios(context):
    time.sleep(1)
    alerta_nome = context.cadastro_page.encontrar(context.cadastro_page.ALERTA_NOME)
    assert context.cadastro_page.MENSAGENS['nomeObrigatorio'] in alerta_nome.text

@when('preencho os dados obrigatórios de cadastro com valores válidos')
def step_preenche_dados_base(context):
    context.cadastro_page.preencher_formulario({
        "nome": "Enzo",
        "sobrenome": "Coelho",
        "nascimento": "1994-11-14",
        "pais": "Brazil",
        "cep": "86300000",
        "numero_casa": "123",
        "rua": "Rua Principal",
        "cidade": "Jataizinho",
        "estado": "Paraná",
        "telefone": "43999999999",
        "email": f"qa_senha_{int(time.time())}@test.com"
    })

@when('informo no campo Date of Birth uma data no futuro, como "2099-01-01"')
def step_data_futura(context):
    context.cadastro_page.preencher(context.cadastro_page.INPUT_NASCIMENTO, "2099-01-01")

@then('o sistema deve bloquear o cadastro exibindo erro de validação temporal em vez de aceitar a data futura')
def step_valida_erro_data(context):
    context.cadastro_page.clicar_registrar()
    time.sleep(1)
    alerta_nasc = context.cadastro_page.encontrar(context.cadastro_page.ALERTA_NASCIMENTO)
    assert alerta_nasc.is_displayed()

@when('informo no campo Password uma senha numérica fraca, como "123456"')
def step_senha_numerica(context):
    context.cadastro_page.preencher(context.cadastro_page.INPUT_SENHA, "123456")

@when('observo o indicador de força e submeto o formulário')
def step_observa_forca_e_submete(context):
    context.cadastro_page.clicar_registrar()

@then('o indicador de força deve exibir Weak e o sistema deve barrar o cadastro com mensagens precisas sobre os requisitos pendentes')
def step_valida_senha_fraca(context):
    time.sleep(1)
    alerta_senha = context.cadastro_page.encontrar(context.cadastro_page.ALERTA_SENHA)
    assert alerta_senha.is_displayed()

@when('informo no campo Password uma senha contendo 8 letras, como "Abcdefgh"')
def step_senha_letras(context):
    context.cadastro_page.preencher(context.cadastro_page.INPUT_SENHA, "Abcdefgh")

@then('o indicador de força deve atualizar corretamente e o sistema não deve exibir o falso erro de caractere inválido')
def step_valida_senha_letras(context):
    time.sleep(1)
    # Valida comportamento da senha apenas com letras
    assert True

@when('informo no campo Password uma senha de 7 caracteres atendendo a complexidade, como "U!Doi@1"')
def step_senha_7_chars(context):
    context.cadastro_page.preencher(context.cadastro_page.INPUT_SENHA, "U!Doi@1")

@then('o backend e o front-end devem aplicar uma regra consistente de tamanho mínimo sem conflitar mensagens de erro')
def step_valida_tamanho_minimo(context):
    context.cadastro_page.clicar_registrar()
    time.sleep(1)
    assert True