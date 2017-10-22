$(document).ready(function(){
    $('a.delete').click(function(){
        if(confirm('Are you sure?') == true) {
            url = $(this).data('href');
            window.location.replace(url);
        }
    });
})
