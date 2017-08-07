$(document).ready(function () {

        $('span').click(function() {
            $('.overlay').toggleClass('anim');
        });

        $('.animation').click(function(){
            $('.anim').toggleClass('reverse-animation');
        })

        $("[data-toggle]").click(function() {
            var toggle_el = $(this).data("toggle");
            $(toggle_el).toggleClass("open-sidebar");
          });
});

