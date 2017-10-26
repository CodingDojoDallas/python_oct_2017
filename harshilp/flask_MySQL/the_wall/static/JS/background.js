$(document).ready(function(){
    var images = [     
        'static/img/the_wall.jpg',
        'static/img/the_wall1.png',
        'static/img/the_wall2.jpg'
    ];
    
    var index = 0;
    
    setInterval(change_up, 5000);
    
    function change_up(){
    
        index = (index + 1 < images.length) ? index + 1 : 0;
    
        $('body.container').css('background-image', 'url('+ images[index] + ')')
        };
});