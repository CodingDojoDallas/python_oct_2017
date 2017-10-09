$(document).ready(function(){
    $("body").on("click", "button", function(){
        var color = $(this).attr("value");
        var ninja_url = "http://localhost:5000/" + color;
        $.get(ninja_url, function(res){
            $("img").attr("src", res.img_url);
        });
    });
});