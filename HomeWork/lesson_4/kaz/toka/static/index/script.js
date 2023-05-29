$(window).scroll(function() {
  var target = $(this).scrollTop();
  if(target < 100) {
     $('nav').css('background-color', 'rgba(255, 255, 255, 0.5)');
     $('nav').css('height', '100px');
     $('#button').css('opacity', '0');
  }
  else {
     $('nav').css('background-color', 'rgba(0, 0, 0, 0.5)');
     $('nav').css('height', '80px');
     $('#button').css('opacity', '1');
  }
})

$(".navbar a").on("click", function () {
    let href = $(this).attr("href");

    $("html, body").animate({
        scrollTop: $(href).offset().top
    }, {
        duration: 370,
        easing: "swing"
    });

    return false;
});

$("#button a").on("click", function () {
    let href = $(this).attr("href");

    $("html, body").animate({
        scrollTop: $(href).offset().top
    }, {
        duration: 370,
        easing: "swing"
    });

    return false;
});