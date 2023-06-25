// Scroll.js

$(window).on('popstate',function(e){
	e.preventDefault();
	var target = window.location.href.split("#")[1];
	if(target != "" && target!=undefined){
		$('html, body').stop().animate({'scrollTop': $("#"+target).offset().top}, 500, 'swing', function () {
			window.location.hash = target;
		});
	}
});

$(document).ready(function(){

	$(window).resize(function(){
		resizeVideo();
		showMenuBtn();
	});

	$(window).trigger("resize");

	// open menu on mobile

	function showMenuBtn(){
		if($(window).width()<1199.98){
			$(".open_menu").addClass("d-block");
			$("header nav").addClass("d-none");
			$(".navigation_mobile").removeClass("opened");
		}else{
			$(".open_menu").removeClass("d-block");
			$("header nav").removeClass("d-none");
			$(".navigation_mobile").removeClass("opened");
		}
	}

	$(".open_menu").click(function(event){
		event.preventDefault();
		$(".navigation_mobile").addClass("opened");
	});

	$(".close_menu, header, section, footer, .navigation_mobile .inner a").click(function(event){
		$(".navigation_mobile").removeClass("opened");
	});

	// Enable AOS plugin (blocks animations)

	if(typeof(AOS) !== 'undefined'){
		AOS.init({
			easing: 'ease-out-cubic',
			offset: 50
		});
		setTimeout(function(){
			if($(".slick-initialized").length>0){
				AOS.refreshHard();
			}
		},200);
	}

	// AJAX send form
		
	$("form").submit(function(event){
		event.preventDefault();
	 
		var form = $(this),
			term = form.serialize(),
			url = form.attr("action"),
			required_fields_filled = true;
			
		form.find("input, textarea, select").each(function(){
			if($(this).prop("required") && $(this).val()==""){
				required_fields_filled = false;
			}
		});

		if(required_fields_filled){
			var posting = $.post(url, term);
			posting
			.done(function(data){
				if(data=="ok"){
					$(".alert-form-success").fadeIn(200).delay(5000).fadeOut(200);
				}else{
					$(".alert-form-error").fadeIn(200).delay(5000).fadeOut(200);
				}
			})
			.fail(function(){
				$(".alert-form-error").fadeIn(200).delay(5000).fadeOut(200);
			});
		}else{
			$(".alert-form-check-fields").fadeIn(200).delay(5000).fadeOut(200);
		}
	});

	// Function to add style to form, when user clicks to input inside it

	function focusForm(formID){
		var form = $("#"+formID);
		if(form.hasClass("focused")){
			form.removeClass("focused");
		}else{
			form.addClass("focused");
		}
	}

		// Opening tabs

		function openTab(tab){
			if(tab.hasClass("opened")){
				$(".tab_text").animate({height:0},300);
				tab.removeClass("opened");
			}else{
				var nextTabHeight = tab.next().find("div").outerHeight(true);
				$(".tab_text").not(tab.next()).animate({height:0},300);
				tab.next().animate({height:nextTabHeight},300);
				$(".tab_opener").removeClass("opened");
				tab.addClass("opened");
			}
		}
	
		$(".tab_opener").click(function(){
			openTab($(this));
		});
	
		if($(".opening_tabs").length > 0){
			$(".tab_opener").each(function(){
				if($(this).hasClass("opened")){
					$(this).removeClass("opened").trigger("click");
				}
			});
		}



}); // document.ready end
