function add_quz_init() {
    console.log("add_quz_init");
    
	var url = "/index.php/welcome/CCM_get_data/" + g_user_id;
	var data = syncJsonRequest(url, "");
	
	$("#CCM_ID").html(data.CCM_ID);
	$("#CCM_NAME").html(data.CCM_NAME);
	setText("CCM_PKEY", data.CCM_ID);
	
	add_quz_generate_contact_list();
	$("#btm_from_contacts").click(add_quz_from_contacts_click);
	
	$("#add_question_form").validate({
		rules : {
			CFM_CONTACT_NAME : {
				required : true,
				maxlength : 30
			},
			CFM_CONTACT_EMAIL : {
				email : true
			},
			CFM_SUBJECT : {
				required : true,
				minlength : 4
			},
			CFM_QDESC : {
				required : true,
				minlength : 5
			}
		},
		submitHandler: add_quz_do_add
	});
}

function add_quz_from_contacts_click(){
	
	$("#contact_list").dialog({
		minWidth : 600,
		modal: true,
		buttons : {
			"取消" : function() {
				$(this).dialog("destroy");
			}
		},
		close : function(event, ui) {
			$(this).dialog("destroy");
		}
	});
}

function add_quz_generate_contact_list(){
	var url = "/index.php/welcome/CCR_get_list_by_CCMPKEY/" +  g_user_id;
	$.get(url, "", function(result) {
		var data = $.parseJSON(result);
		var html = "";
		$.each(data.query_data, function(key, value) {
			html += "<tr id='"+value.CCR_PKEY+"'><td><span id='CCR_NAME'>"+ value.CCR_NAME +"</span></td><td><span id='CCR_PHONE'>"+ value.CCR_PHONE +"</span></td><td><span id='CCR_EMAIL'>"+ value.CCR_EMAIL +"</span></td>"
			html += "<td><button CCR_PKEY='"+value.CCR_PKEY+"' type='button' class=\"btn btn-primary\">選擇</button></td></tr>"
		});
		$("#contact_list tbody").html(html);
		$("#contact_list button").click(add_quz_contact_click);
	});
}

function add_quz_contact_click(){
	var CCR_PKEY = $(this).attr("CCR_PKEY");
	var CCR_NAME = $(id(CCR_PKEY)).find("#CCR_NAME").text();
	var CCR_PHONE = $(id(CCR_PKEY)).find("#CCR_PHONE").text();
	var CCR_EMAIL = $(id(CCR_PKEY)).find("#CCR_EMAIL").text();
	
	setText("CFM_CONTACT_NAME", CCR_NAME);
	setText("CFM_CONTACT_PHONE", CCR_PHONE);
	setText("CFM_CONTACT_EMAIL", CCR_EMAIL);
	$("#contact_list").dialog("destroy");
}

function add_quz_do_add(){
	console.log("add_quz_do_add");

	var postData = "CCM_PKEY=" + $("#CCM_PKEY").val() + "&";
	postData += "CCR_NAME=" + $("#CFM_CONTACT_NAME").val() + "&";
	postData += "CCR_PHONE=" + $("#CFM_CONTACT_PHONE").val() + "&";
	postData += "CCR_EMAIL=" + $("#CFM_CONTACT_EMAIL").val();

	$.post("/index.php/welcome/CCR_add", postData, function(result) {
		var postData = $("#add_question_form").serializeArray();
		$.post("/index.php/welcome/CFM_add", postData, function(result) {
			// console.log(result);
			$().message(result);
			pageload_add_question();
		}).fail(function() {
			$().message("失敗");
		});
	});
}