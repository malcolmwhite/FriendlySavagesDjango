function ajaxifyLinks(){
    // Capture all the links to push their url to the history stack and trigger the StateChange Event
    $('a').not('.external_link').click(function(evt) {
        // do not execute the actual link behaviour
        evt.preventDefault();
        History.pushState(null, $(this).text(), $(this).attr('href'));
    });
}
 
function setActiveLink(selector){
    $('#menu a').removeClass('active');
    if (selector){
        $(selector).addClass('active');
    }
}