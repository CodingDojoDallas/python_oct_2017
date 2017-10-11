$(document).ready(function(){
    $('form').submit(function(){
        var val = $("input[type=submit][clicked=true]").val();
        $.post('/process', {'color' : val}, function(data){
            $('img').attr('src', data.url);
            $('img').attr('alt', data.alt);
            $('p').text(data.message);
        }, 'json');
        return false;
    });
    $("form input[type=submit]").click(function() {
        $("input[type=submit]", $(this).parents("form")).removeAttr("clicked");
        $(this).attr("clicked", "true");
    });
});