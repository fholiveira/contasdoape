$(document).ready ->
  do $('form').validate

  $.validator.addMethod 'regex',
    (value, element, regexp) ->
      @optional(element) || new RegExp(regexp).test value

  $.validator.addMethod 'ehData',
    (value, element, formats) ->
      ehData = formats.some (format) -> new RegExp(format).test value
      @optional(element) || ehData
  
  $('#data').rules 'add',
    ehData: ['^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$', '^[0-9]{4}-[0-9]{2}-[0-9]{2}$']
    date: true
    messages:
      required: 'Você deve informar a data da despesa'
      date: 'Você deve informar uma data válida'
      ehData: 'Você deve informar uma data válida'

  $('#valor').rules 'add',
    regex: '^([0-9]+(\.|,)[0-9]|[0-9]+)+$'
    messages:
      required: 'Você deve informar o valor da despesa'
      regex: 'Você deve informar um valor válido'
  
  $('#descricao').rules 'add',
    messages:
      required: 'Você deve descrever a despesa'
