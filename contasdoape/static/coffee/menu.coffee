$(document).ready ->
    link = 'ul.nav > li a[href^="' + window.location.pathname + '"]'
    $(link).parent().addClass 'active'
