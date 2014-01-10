class FacebookFriendPicker
  constructor: (caixadetexto) ->
    @caixadetexto = caixadetexto
        
    @init()

  init: ->
    @loadFriendList()
  
  defineTokens: (friends) ->
    @caixadetexto.tokenfield({
      allowDuplicates: false
      typeahead: {
        valueKey: 'label'
        local: friends
        name: 'Friends'
      }
    })

  getNamesOfFriends: (friendList) ->
    names = []

    for friend in friendList 
      names.push(friend.label)

    return names

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
      new FacebookFriendPicker $('#fb-friendlist')

$ ->
  id = 'facebook-jssdk'
  return if $(id).length > 0
  sdk = $.getScript "http://connect.facebook.net/en_US/all.js"
  sdk.id = id
  sdk.async = true
