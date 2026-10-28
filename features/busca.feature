# language: pt
Funcionalidade: Busca e Filtros de Produtos
  Como um cliente da Tool Shop
  Quero buscar, filtrar e ordenar os produtos no catálogo
  Para encontrar rapidamente as ferramentas que preciso comprar

  Contexto:
    Dado que estou na página inicial do catálogo da loja

  Esquema do Cenário: QA-FIL-01 - Ordenação de produtos do catálogo
    Quando ordeno os produtos do catálogo pela opção "<criterio_ordenacao>"
    Então os produtos devem ser exibidos corretamente ordenados conforme o critério selecionado

    Exemplos:
      | criterio_ordenacao     |
      | Name (A - Z)           |
      | Name (Z - A)           |
      | Price (High - Low)     |
      | Price (Low - High)     |

  Cenário: QA-FIL-02 - Busca por produto existente
    Quando busco pelo termo "Pliers" na barra de pesquisa
    Então o catálogo deve retornar apenas os produtos correspondentes à busca

  Cenário: QA-FIL-03 - Busca por termo inexistente
    Quando busco por um termo que não existe no catálogo, como "xyz123abc"
    Então devo ver a mensagem informando que nenhum resultado foi encontrado

  Cenário: QA-FIL-04 - Filtragem de produtos por categoria
    Quando seleciono o filtro de categoria "Hand Tools"
    Então o catálogo deve exibir exclusivamente os produtos pertencentes a essa categoria

  Cenário: QA-FIL-05 - Limpeza de filtros (Reset)
    Dado que apliquei filtros e ordenações específicas no catálogo
    Quando aciono a opção de limpar os filtros
    Então o catálogo deve ser restaurado para o seu estado completo original