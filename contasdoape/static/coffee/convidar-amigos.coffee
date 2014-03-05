class FacebookFriendPicker
  constructor: (botaosalvar) ->
    @botaosalvar = botaosalvar
    do @init

  init: ->
    $(@botaosalvar).click @salvarLista
    $('#fb-friendlist').on 'afterCreateToken', @afterCreateToken
    do @loadFriendList

  afterCreateToken: (dados) ->
    if not isFinite(dados.token.value) or dados.token.value == dados.token.label
      $('#fb-friendlist').data('bs.tokenfield').$input.val ''
      do $(dados.relatedTarget).remove

  salvarLista: (e) ->
    do e.preventDefault

    $.ajax
      type: "POST"
      url: "/salvar-amigos"
      success: -> window.location.href = '/'
      contentType: "application/json; charset=utf-8"
      data: JSON.stringify($('#fb-friendlist').tokenfield 'getTokens')

  defineTokens: (friends) ->
    $('#fb-friendlist').tokenfield
      allowDuplicates: false
      typeahead:
        valueKey: 'label'
        local: friends
        name: 'Friends'

  loadFriendList: ->
    friends = []

    FB.api '/me/friends/?fields=name', (response) =>
      for friend, i in response.data
        friends.push
          value: friend.id
          label: friend.name

      do @defineTokens friends

window.fbAsyncInit = ->
  FB.init
    appId: $('#fb-root').data('app-id')
    status: true
    cookie: true
    xfbml: true
    oauth: true

  FB.getLoginStatus (response) ->
    if response.status == 'connected'
      new FacebookFriendPicker '#salvar_convites'

$ ->
  id = 'facebook-jssdk'
  return if $(id).length > 0
  sdk = $.getScript "http://connect.facebook.net/en_US/all.js"
  sdk.id = id
  sdk.async = true
