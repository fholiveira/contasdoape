class Despesas
  constructor: (modal, confirmarExclusao, despesaAExcluir) ->
    @confirmarExclusao = confirmarExclusao
    @despesaAExcluir = despesaAExcluir
    @modal = modal
    do @_init

  _init: =>
    $(document).on 'click', 'a.remover', @_questionarExclusao
    @confirmarExclusao.click @_excluirDespesa

  _excluirDespesa: =>
    id = @despesaAExcluir.data 'id'
    $.post "/despesas/excluir/#{id}", @_quandoExcluir

  _quandoExcluir: =>
    @modal.modal 'hide'
    do window.location.reload

  _questionarExclusao: (evento, dados) =>
    despesa = $($(evento.target).parents 'li')

    @despesaAExcluir.data 'id', despesa.data 'id'

    @_copiar despesa, @despesaAExcluir, '.valor'
    @_copiar despesa, @despesaAExcluir, '.data'
    @_copiar despesa, @despesaAExcluir, '.descricao'

    do @modal.modal

  _copiar: (origem, destino, selector) ->
    destino.find(selector).text origem.find(selector).text()

$(document).ready ->
  new Despesas $('#excluir_despesa'),
    $('#confirmar_exclusao'),
    $('#despesa_a_excluir')
