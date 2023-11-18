$(window).scroll(function() {
    var target = $(this).scrollTop();
    if(target < 350) {
       $('.fixed').css('position', 'sticky');
       $('.fixed').css('transition', 'all .2s');
       $('.fixed').css('top', '-100px');
       $('.fixed').css('visibility', 'hidden');
    }
    else {
       $('.fixed').css('position', 'sticky');
       $('.fixed').css('top', '-1px');
       $('.fixed').css('transition', 'all .5s');
       $('.fixed').css('visibility', 'visible');
    }
 })

$(document).ready(function(){
    $('.scroll-top a').click(function (){
        $('body,html').animate({
            scrollTop:0
        }, 20);
        return false;
    });
})