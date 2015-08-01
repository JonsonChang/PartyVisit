$(function(){
	console.log("main");
	init_menu();
	$("#menu_my_village").click();
});


function init_menu(){
	$("#menu_my_village").click(pageload_my_village);
	$("#menu_my_intro").click(pageload_my_intro);
	$("#menu_import").click(pageload_import);
	$("#menu_logout").click(pageload_logout);
	//------
	$("#menu_person").click(pageload_person);
	$("#menu_test").click(pageload_test);
	
}


function pageload_person() {
	$("#navbar li").removeClass("active");
	$(this).parent().addClass("active");
	load_page("#content_div", "page_person.html", function() {
		console.log("");
		person_init();
		
	});
}


function pageload_test() {
	$("#navbar li").removeClass("active");
	$(this).parent().addClass("active");
	load_page("#content_div", "page_test.html", function() {
		console.log("");
		
	});
}

function pageload_my_village() {
	$("#navbar li").removeClass("active");
	$(this).parent().addClass("active");
	load_page("#content_div", "page_my_village.html", function() {
		console.log("");

	});
}

function pageload_my_intro() {
	$("#navbar li").removeClass("active");
	$(this).parent().addClass("active");
	load_page("#content_div", "page_my_intro.html", function() {
		console.log("");

	});
}
function pageload_import() {
	$("#navbar li").removeClass("active");
	$(this).parent().addClass("active");
//	load_page("#content_div", "page_auth.html", function() {
//		console.log("");
//
//	});
}
function pageload_logout() {
	$("#navbar li").removeClass("active");
	$(this).parent().addClass("active");
//	load_page("#content_div", "page_auth.html", function() {
//		console.log("");
//
//	});
}
