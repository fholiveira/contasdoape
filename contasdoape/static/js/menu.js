$(document).ready(function () {
    link = 'ul.nav > li a[href^="' + window.location.pathname + '"]'        
    $(link).parent().addClass('active');
});
