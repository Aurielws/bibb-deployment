// Scroll.js
$(window).on('popstate',function(e){
	e.preventDefault();
	var target = window.location.href.split("#")[1];
	if(target != "" && target!=undefined && document.getElementById(target)!=null){
		$('html, body').stop().animate({'scrollTop': $("#"+target).offset().top}, 500, 'swing', function () {
			window.location.hash = target;
		});
	}
});

$(document).ready(function() {
	SF_scripts();
});

function SF_scripts(){

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

	
	// Set highest z-index for section, that has opened dropdown
	$(".dropdown").on("show.bs.dropdown", function () {
		var section = SF_dropdown_parent($(this));
		section.css("z-index",SF_highest_zIndex()[0]+1);	
	});
	
	// Remove z-index for section, where dropdown was closed
	$(".dropdown").on("hidden.bs.dropdown", function () {
		var section = SF_dropdown_parent($(this));
		section.css("z-index","auto");	
	})
	
	// Enable AOS plugin (blocks animations)
	if(typeof(AOS) !== 'undefined' && $("body").hasClass("SFG_body")===false){
		AOS.init({
			easing: 'ease-out-cubic',
			once: true,
			offset: 50
		});
		setTimeout(function(){
			if($(".slick-initialized").length>0){
				AOS.refreshHard();
			}
		},200);
	}

	// AJAX send form	
	$("form:not(.SFG)").submit(function(event){
		
		event.preventDefault();
		var form = $(this);
		submitForm(form);
	
		function submitForm(form){
		    var	term = form.serialize(),
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
						$(".alert-form-error .message").html(data);
						$(".alert-form-error").fadeIn(200).delay(10000).fadeOut(200);
					}
				})
				.fail(function(){
					$(".alert-form-error").fadeIn(200).delay(10000).fadeOut(200);
				});
			}else{
				$(".alert-form-check-fields").fadeIn(200).delay(5000).fadeOut(200);
			}
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

	// Resize Loading image/Gif/Video, saving aspect ratio
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

	/*
		Sliders
	*/
	
	var slick_slider;

	if($(".form_4 .slider").length>0){
		$(".form_4 .slider").each(function(index){
			slick_slider = $(this);
			if(slick_slider.hasClass("slick-initialized")===false){
				slick_slider.slick({
					slidesToShow: 1,
					slidesToScroll: 1,
					arrows: false,
					fade: true,
					touchMove:false,
					swipe:false,
					adaptiveHeight: true,
					asNavFor: '.form_4 .form_4_menu:eq('+index+')',
				});
				$('.form_4 .form_4_menu:eq('+index+')').slick({
					slidesToShow: 2,
					slidesToScroll: 1,
					asNavFor: '.form_4 .slider:eq('+index+')',
					dots: false,
					arrows: false,
					focusOnSelect: true,
					touchMove:false,
					swipe:false,
				});
			}
		});
	}

	if($(".form_15 .slider").length>0){
		$(".form_15 .slider").each(function(index){
			slick_slider = $(this);
			if(slick_slider.hasClass("slick-initialized")===false){
				slick_slider.slick({
					slidesToShow: 1,
					slidesToScroll: 1,
					arrows: false,
					fade: true,
					adaptiveHeight: true,
					swipe:false,
					asNavFor: '.form_15 .form_15_menu:eq('+index+')',
				});
				$('.form_15 .form_15_menu:eq('+index+')').slick({
					slidesToShow: 2,
					slidesToScroll: 1,
					asNavFor: '.form_15 .slider:eq('+index+')',
					dots: false,
					arrows: false,
					focusOnSelect: true,
				});
			}
		});
	}
	
	
}; // SF_scripts end
