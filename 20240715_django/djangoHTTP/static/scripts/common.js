$(function(){
    $('.table tr:not(:first)').hover(
        function(){
            $(this).addClass('success').css('cursor','pointer')
        },
        function(){
                $(this).removeClass('success')
        }
    );
});