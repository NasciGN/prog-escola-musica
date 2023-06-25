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
		


	// Function to add style to form, when user clicks to input inside it

	function focusForm(formID){
		var form = $("#"+formID);
		if(form.hasClass("focused")){
			form.removeClass("focused");
		}else{
			form.addClass("focused");
		}
	}

	// Resize video, saving aspect ratio

	function resizeVideo(){
		var width, height, ratio;
		$(".video").each(function(){
			ratio = $(this).data("ratio");
			ratio = ratio.split("/");
			ratio = ratio[0]/ratio[1];
			width = $(this).width();
			height = width/ratio;
			$(this).height(height);
		});
	}

	resizeVideo();

	// Play video

	$(".video .play").click(function(){
		var video = $(this).parent().parent().find("video");
		$(this).closest(".poster").fadeOut(300,function(){
			video.fadeIn(300,function(){
				video[0].play();
				video[0].onended = function() {
					$(this).parent().find(".poster").delay(100).fadeIn(300);
				};
			});
		});
	});
	 
	// Open video in popup

	$(".js-play-popup-video").click(function(event){
		event.preventDefault();
		var url = $(this).attr("href");
		$(".video_popup .iframe_container").html('<iframe src="'+url+'" allowfullscreen></iframe>');
		$(".video_popup, .overlay").fadeIn(300);
	});

	// Close video popup

	$(".video_popup .close, .overlay").click(function(e){
		$(".video_popup, .overlay").fadeOut(300);
		setTimeout(function() {
			$(".video_popup .iframe_container").html('');
		},300);
	});
	
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

	// Copy text from block

	if($("#copy_from_me").length > 0){
		function copyStringToClipboard (str) {
		   var el = document.createElement('textarea');
		   el.value = str;
		   el.setAttribute('readonly', '');
		   el.style = {position: 'absolute', left: '-9999px'};
		   document.body.appendChild(el);
		   el.select();
		   document.execCommand('copy');
		   document.body.removeChild(el);
		}
		$('.js-copy-btn').click(function(){
			copyStringToClipboard ($("#copy_from_me").text());
		});
	}

	// Add mask to inputs in Forms

	if($(".js-card-mask").length > 0){
		$(".js-card-mask").mask("9999 9999 9999 9999");
	}
	if($(".js-expiration-mask").length > 0){
		$(".js-expiration-mask").mask("99 / 9999");
	}
	if($(".js-expiration-short-mask").length > 0){
		$(".js-expiration-short-mask").mask("99 / 99");
	}
	if($(".js-cvv-mask").length > 0){
		$(".js-cvv-mask").mask("999");
	}
	
	// Disable / enable blocks in Form 13

	$(".form_13 input[type=radio]").change(function(){
		var choosenBlock = $(".form_13 input[type=radio]:checked").closest(".js-form-block");
		$(".js-form-block").removeClass("active");
		choosenBlock.addClass("active");
	});
	
	// Ecommerce: Quantity selector
	
	$(".quantity_selector .control").click(function(event){
		event.preventDefault();
		var _this = $(this);
		var input = _this.parent().find("input");
		var input_val = parseInt(input.val());
		if(_this.hasClass("greater")){
			if(input_val<parseInt(input.attr("max"))){
				input.val(input_val+1);
				input.trigger("change");
			}
		}
		if(_this.hasClass("less")){
			if(input_val>parseInt(input.attr("min"))){
				input.val(input_val-1);
				input.trigger("change");
			}
		}
	});
	
}); // document.ready end
