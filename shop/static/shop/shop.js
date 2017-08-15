$(document).ready(function(){
  $('.carousel-item').slick({
    adaptiveHeight: true,
    dots: true,
    infinite: true,
    speed: 500,
    fade: true,
    cssEase: 'linear',
    mobileFirst: true,
    autoplay: true,
    autoplaySpeed: 5000,
    draggable: false,
    speed: 500,
    arrows: true
  });

  $('.slick-slide').focus();

  $('.js-slick').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
    $(slick.$slides).removeClass('is-animating');
  });

  $('.js-slick').on('afterChange', function(event, slick, currentSlide, nextSlide) {
    $(slick.$slides.get(currentSlide)).addClass('is-animating');
  });
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
