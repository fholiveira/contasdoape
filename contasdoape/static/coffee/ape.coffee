class Convidados
  url_base = 'http://graph.facebook.com/'
  
  constructor: (convidados) ->
    @convidados = convidados

  preencher: (convidado, dados) ->
    convidado.children('p').text dados.name
    imagem = convidado.children('img')
    imagem.attr 'alt', dados.name
    imagem.attr 'src', "http://graph.facebook.com/#{dados.id}/picture?type=square"
  
  obterDadosDosConvidados: =>
    for item in @convidados
      convidado = $(item)
      
      $.get url_base + convidado.data 'id'
      .done (data) =>
        @preencher convidado, data

convidados = new Convidados $('.convidados .pessoa')
do convidados.obterDadosDosConvidados
