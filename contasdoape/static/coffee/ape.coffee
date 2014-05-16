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

class DiaDoAcerto
  constructor: (@botaoSalvar, @caixaDeTexto) ->
    @botaoSalvar.click @salvar

  salvar: =>
    if @caixaDeTexto.valid()
      $.post '/ape/mudar-dia-do-acerto', { dia: @caixaDeTexto.val() }
        .done -> window.location.reload true

convidados = new Convidados $('.convidados .pessoa')
do convidados.obterDadosDosConvidados

new DiaDoAcerto $('#alterar_dia'), $('#dia')

$(document).ready ->
  do $('form').validate

  $.validator.addMethod 'between', (value, element, data) ->
    @optional(element) || value >= data.start && value <= data.end

  $('#dia').rules 'add',
    required: true
    digits: true
    between: { start: 1, end: 31 }
    messages:
      required: 'Você deve informar o novo dia de acerto'
      between: 'O dia deve estar entre 1 e 31'
      digits: 'Por favor digite um dia'
