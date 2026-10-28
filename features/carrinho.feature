# language: pt
Funcionalidade: Carrinho de Compras
  Como um cliente da Tool Shop
  Quero gerenciar os itens no meu carrinho
  Para controlar as quantidades e prosseguir para a compra

  Contexto:
    Dado que estou na página inicial do catálogo

  Cenário: QA-CAR-01 e QA-CAR-03 - Adicionar produto e recalcular subtotal
    Quando seleciono um produto disponível no catálogo e o adiciono ao carrinho
    E navego até a tela do carrinho ("/checkout")
    E altero a quantidade do item para "3"
    Então o subtotal do item deve ser recalculado automaticamente com base na nova quantidade

  Cenário: QA-CAR-04 - Remoção de item do carrinho
    Dado que possuo um produto adicionado no carrinho
    Quando removo o item clicando no botão de exclusão
    Então o carrinho deve ficar totalmente vazio

  Cenário: QA-CAR-06 - [BUG] Alertas incorretos ao rejeitar limite de quantidade no carrinho
    Dado que possuo um produto adicionado no carrinho na tela de checkout
    Quando altero a quantidade do item para um valor inválido ou acima do limite, como "0" ou "100"
    Então o sistema deve corrigir o valor permitido e exibir apenas a restrição sem disparar o toast verde de sucesso indevido

  Cenário: QA-CAR-07 - Persistência do carrinho após nova sessão
    Dado que adicionei um produto ao carrinho com sucesso
    Quando faço o logout da minha conta e realizo login novamente
    Então os itens adicionados devem permanecer salvos no carrinho