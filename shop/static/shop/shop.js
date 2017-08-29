$(window).on("load", function() {
  $('.carousel-item').slick({
    accessibility: true,
    lazyLoad: "progressive",
    adaptiveHeight: true,
    dots: true,
    infinite: true,
    speed: 500,
    cssEase: 'cubic-bezier(0.215, 0.61, 0.355, 1)',
    slidesToShow: 2,
    slidesToScroll: 2,
    mobileFirst: true,
    autoplay: true,
    autoplaySpeed: 5000,
    arrows: true,
    draggable: false
  });


    $('.slick-active').focus();

  $('.js-slick').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
    $(slick.$slides).removeClass('is-animating');
  });

  $('.js-slick').on('afterChange', function(event, slick, currentSlide, nextSlide) {
    $(slick.$slides.get(currentSlide)).addClass('is-animating');
  });
  if (!( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) ) {
    $("#navbarDropdownMenuLink").hover(function()
     {
       $(this).css("cursor", "pointer");
     });
  }


});

    //$('.carousel-item').slick('slickAdd',"<div></div>");

window.onload = function() {
  document.querySelector('.js-slideout-toggle').addEventListener('click', function() {
    slideout.toggle();
  });

  document.querySelector('.menu').addEventListener('click', function(eve) {
    if (eve.target.nodeName === 'A') { slideout.close(); }
  });

  //var runner = mocha.run();
};