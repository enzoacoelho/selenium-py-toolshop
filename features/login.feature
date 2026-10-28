# language: pt
Funcionalidade: Autenticação e Sessão
  Como um cliente da Tool Shop
  Quero fazer login e gerenciar minha sessão
  Para acompanhar meus pedidos e realizar compras

  Contexto:
    Dado que estou na página de login da aplicação

  Cenário: QA-LOG-01 - Login com credenciais válidas
    Quando preencho o campo de e-mail com "customer@practicesoftwaretesting.com"
    E preencho o campo de senha com "welcome01"
    E clico no botão de login
    Então devo ser redirecionado para a página da minha conta "/account"

  Cenário: QA-LOG-02 - Tentativa de login com campos vazios
    Quando deixo os campos de e-mail e senha em branco
    E clico no botão de login
    Então devo ver as mensagens de obrigatoriedade abaixo dos campos de e-mail e senha

  Esquema do Cenário: QA-LOG-06 - Tentativa de login com credenciais incorretas ou inválidas
    Quando preencho o campo de e-mail com "<email>"
    E preencho o campo de senha com "<senha>"
    E clico no botão de login
    Então devo ver a mensagem de erro de autenticação "Invalid email or password"

    Exemplos:
      | email                                | senha     |
      | customer@practicesoftwaretesting.com | errada123 |
      | usuario_inexistente@test.com         | welcome01 |

Cenário: QA-LOG-12 - Encerramento de sessão 
    Dado que estou na página de login da aplicação
    Dado que estou autenticado no sistema com credenciais válidas
    Quando aciono a opção de encerramento de sessão "Sign out"
    Então devo ser redirecionado para a tela de login
 