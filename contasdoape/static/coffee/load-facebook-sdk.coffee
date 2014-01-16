class FacebookFriendPicker
  constructor: (botaosalvar) ->
    @botaosalvar = botaosalvar
        
    @init()

  init: ->
    $(@botaosalvar).click @salvarLista
    @loadFriendList()

  salvarLista: (e) ->
    e.preventDefault()
    
    $.ajax({
      type: "POST"
      url: "/salvaramigos"
      success: -> window.location.href = '/'
      contentType: "application/json; charset=utf-8"
      data: JSON.stringify($('#fb-friendlist').tokenfield('getTokens'))
    })

  defineTokens: (friends) ->
    $('#fb-friendlist').tokenfield({
      allowDuplicates: false
      typeahead: {
        valueKey: 'label'
        local: friends
        name: 'Friends'
      }
    })

  loadFriendList: ->
    friends = []
   
    FB.api '/me/friends/?fields=name', (response) =>
      for friend, i in response.data
        friends.push({
          value: friend.id
          label: friend.name
        })
    
      @defineTokens(friends)

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
