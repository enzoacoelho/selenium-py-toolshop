# language: pt
Funcionalidade: Cadastro de Usuário
  Como um novo cliente da Tool Shop
  Quero me cadastrar na plataforma preenchendo meus dados
  Para poder realizar compras e acompanhar meus pedidos

  Contexto:
    Dado que estou na página de cadastro de nova conta

  Cenário: QA-CAD-01 - Cadastro de novo usuário com sucesso
    Quando preencho o formulário de cadastro com dados pessoais válidos e um e-mail dinâmico
    E submeto o formulário clicando em Register
    Então o sistema deve registrar a conta com sucesso e permitir o login subsequente

  Cenário: QA-CAD-02 - Tentativa de cadastro com e-mail já existente
    Quando preencho o formulário utilizando um e-mail que já está cadastrado na base
    E submeto o formulário clicando em Register
    Então devo ver uma mensagem informando que o e-mail já existe

  Cenário: QA-CAD-03 - Submissão de cadastro com campos obrigatórios em branco
    Quando deixo os campos obrigatórios em branco
    E tento submeter o formulário
    Então o sistema deve exibir os alertas de preenchimento obrigatório em cada campo correspondente

  Cenário: QA-CAD-04 - Validação de data de nascimento no futuro
    Quando preencho os dados obrigatórios de cadastro com valores válidos
    E informo no campo Date of Birth uma data no futuro, como "2099-01-01"
    E submeto o formulário clicando em Register
    Então o sistema deve bloquear o cadastro exibindo erro de validação temporal

  Cenário: QA-CAD-05 - Validação de senha numérica fraca
    Quando preencho os dados obrigatórios de cadastro com valores válidos
    E informo no campo Password uma senha numérica fraca, como "123456"
    E submeto o formulário clicando em Register
    Então o sistema deve barrar o cadastro exibindo mensagens sobre os requisitos de complexidade pendentes

  Cenário: QA-CAD-06 - Validação de senha contendo apenas letras
    Quando preencho os dados obrigatórios de cadastro com valores válidos
    E informo no campo Password uma senha contendo 8 letras, como "Abcdefgh"
    E submeto o formulário clicando em Register
    Então o sistema deve exigir que a senha inclua números e símbolos

  Cenário: QA-CAD-07 - Validação de tamanho mínimo da senha
    Quando preencho os dados obrigatórios de cadastro com valores válidos
    E informo no campo Password uma senha de 7 caracteres atendendo a complexidade, como "U!Doi@1"
    E submeto o formulário clicando em Register
    Então o sistema deve exibir uma mensagem informando o tamanho mínimo exigido para a senha