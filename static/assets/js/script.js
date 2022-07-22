var i = 0;
var txt = document.getElementById("heading_desc").innerHTML; /* The text */
var speed = 50; /* The speed/duration of the effect in milliseconds */
document.getElementById("heading_desc").innerHTML = "";

function typeWriter() {
		
	if (i < txt.length) {
		document.getElementById("heading_desc").innerHTML += txt.charAt(i);
		i++;
		setTimeout(typeWriter, speed);
	}
}
typeWriter();


$(function(){
    // header height
	var header_h = $('.index_header');
    header_h.height($(window).height());
    $(window).resize(function(){
        header_h.height($(window).height());
	});
	
	// on click in link go to this
	$('.nav-link, .navbar-brand, .new-button,#learn-more').click(function() {
		var sectionTo = $(this).attr('href');
		$('html, body').animate({
		  	scrollTop: $(sectionTo).offset().top
		}, 700);
	});

	// active link
	$('.navbar-light .navbar-nav .link-nav').click(function(){
		//$(this).parent().find( 'nav ul li a .active' ).removeClass('active');
		$(".navbar-light .navbar-nav .link-nav").removeClass('active');
        $(this).addClass('active');
	});

});