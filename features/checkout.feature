# language: pt
Funcionalidade: Processo de Checkout e Pagamento
  Como um cliente da Tool Shop
  Quero preencher os dados de pagamento e finalizar o pedido
  Para concluir a compra das ferramentas escolhidas

  Contexto:
    Dado que possuo itens no carrinho e avancei até a etapa de pagamento (Step 4)

  Esquema do Cenário: QA-CKT-01 - Finalização de pedido com sucesso utilizando diferentes métodos de pagamento
    Quando seleciono o método de pagamento "<metodo_pagamento>"
    E preencho os dados obrigatórios correspondentes com informações válidas
    E clico no botão "Confirm"
    Então o pedido deve ser concluído com sucesso e o comprovante com o ID do pedido deve ser exibido na tela

    Exemplos: Métodos de Pagamento Válidos
      | metodo_pagamento |
      | Credit Card      |
      | Bank Transfer    |
      | Cash on Delivery |

  Cenário: QA-CKT-02 - Checkout via Cartão de Crédito com campos vazios exibe Unknown error
    Dado que seleciono o método de pagamento "Credit Card"
    Quando deixo todos os campos obrigatórios em branco (Credit Card Number, Expiration Date, CVV e Card Holder Name)
    E clico no botão "Confirm"
    Então o sistema deve bloquear o envio destacando visualmente os campos obrigatórios em vermelho em vez de exibir um erro genérico "Unknown error"

  Cenário: QA-CKT-05 - Checkout via Bank Transfer desabilita botão sem feedback visual
    Dado que seleciono o método de pagamento "Bank Transfer"
    Quando mantenho os campos obrigatórios vazios (Bank Name, Account Name e Account Number)
    E tento interagir com o formulário
    Então o sistema deve fornecer feedback visual de validação nos campos obrigatórios em vez de apenas desativar o botão Confirm sem aviso