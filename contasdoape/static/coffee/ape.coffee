class Convidados
  url_base: 'http://graph.facebook.com/'

  constructor: (@convidados) ->

  obterConvidado: (id) =>
    return $(c) for c in @convidados when id == $(c).data('id').toString()

  preencher: (dados) =>
    convidado = @obterConvidado dados.id
    convidado.children('p').text dados.name

    imagem = convidado.children('img')
    imagem.attr 'alt', dados.name
    imagem.attr 'src', "#{@url_base}#{dados.id}/picture?type=square"

  obterDadosDosConvidados: =>
    for convidado in @convidados
      $.get @url_base + $(convidado).data 'id'
      .done @preencher

convidados = new Convidados $('.convidados .pessoa')
do convidados.obterDadosDosConvidados
