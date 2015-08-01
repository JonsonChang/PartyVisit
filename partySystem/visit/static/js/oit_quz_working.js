function quz_working_init() {
    console.log("quz_working_init");
    quz_working_generate_option_list();
    quz_working_generate_FaqType_option_list();
    quz_working_generate_list();
    $("#new_CFM_TYPE").click(quz_working_new_CFM_TYPE_click);
    
    $("#quz_working_query_apply").click(quz_working_query_apply_click);
    
    $("#quz_working_update").click(function(){
    	$("#quz_working_content_form").submit();
    });

	$("#quz_working_content_form").validate({
		rules : {
			CFM_SUBJECT : {
				required : true,
				maxlength : 16
			},
			CFR_DESC : {
				minlength : 4
			}
		},
		submitHandler : quz_working_do_update
	});
	
	$("#q_date_s,#q_date_e").datepicker({
		dateFormat : "yy-mm-dd",
		changeMonth : true,
		changeYear : true
	});
}

function quz_working_query_apply_click(){
	var postData = $("#quz_working_query_form").serializeArray();
	var url = "/index.php/welcome/CFM_get_list_like";
	$.post(url, postData, function(result) {
		var data = $.parseJSON(result);
		quz_working_generate_table(data);
		
		if(data.total < 1)
			$().message("無資料");
		
	});
}

function quz_working_do_update(){
	var postData = $("#quz_working_content_form").serializeArray();
	var url = "/index.php/welcome/FAQ_update";
	$.post(url, postData, function(result) {
//		console.log(result);
		$().message(result);
		pageload_question_working();
	});
	
}

function quz_working_do_add_CFM_TYPE() {
	var postData = $("#quz_working_add_form").serializeArray();
	
	$.post("/index.php/welcome/CCC_NAME_add", postData, function(result) {
		var currentType = $("#CFM_TYPE").val().toString(); 
//		 console.log(currentType);

		$("#dialog_add_CCC_NAME").dialog("destroy");
		quz_working_generate_FaqType_option_list();
		setSelect("CFM_TYPE", currentType);
		$().message(result);
	});
}

function quz_working_new_CFM_TYPE_click() {
	$("#quz_working_add_form").validate({
		rules : {
			CCC_NAME : {
				required : true,
				maxlength : 16
			}
		},
		submitHandler: quz_working_do_add_CFM_TYPE
	});
	
	$("#dialog_add_CCC_NAME").dialog({
		minWidth : 400,
		modal: true,
		buttons : {
			"新增" : function() {
				$("#quz_working_add_form").submit()
			},
			"取消" : function() {
				$(this).dialog("destroy");
			}
		},
		close : function(event, ui) {
			$(this).dialog("destroy");
		}
	});
	
}

function quz_working_generate_list() {
	var url = "/index.php/welcome/CFM_get_list";
	$.get(url, "", function(result) {
		var data = $.parseJSON(result);
		quz_working_generate_table(data);
	});
}

function quz_working_generate_table(data) {
	var html = "";
	$.each(data.query_data, function(key, value) {
		html += "<tr style='cursor:pointer' CFM_PKEY='" + value.CFM_PKEY
				+ "'><td>" + value.CCM_ID + "</td><td>" + value.CCM_NAME
				+ "</td><td>" + value.ADD_DATE + "</td><td>"
				+ value.CFM_SUBJECT + "</td><td>" + faqcode2str(value.CFM_CODE)
				+ "</td><td>" + value.CAM_NAME + "</td></tr>";
	});

	$("#quz_working_table tbody").html(html);
	$("#quz_working_table tr").click(quz_working_list_click);
}


function quz_working_generate_FaqType_option_list(){
	var html = "";

// 問題類別
	var url = "/index.php/welcome/CFM_get_type_name";
	$.get(url, "", function(result) {
		var data = $.parseJSON(result);
		html="";
		$.each(data, function(key, value) {
			html += "<option value=\"" + value.CFM_TYPE + "\">"
					+ value.CCC_NAME + "</option>";
		});
		$("#CFM_TYPE").html(html);
	});
}

function quz_working_generate_option_list(){
	var html = "";

//指定客服 , 處理人員
	var url = "/index.php/welcome/CAM_get_list/";
	$.get(url, "", function(result) {
		var data = $.parseJSON(result);
		html="";
		$.each(data.query_data, function(key, value) {
			if (value.CAM_INACTIVE == "Y") {
				html += "<option value=\"" + value.CAM_PKEY + "\">"
				+ value.CAM_NAME + "(停用)</option>";
			}
			else{
				html += "<option value=\"" + value.CAM_PKEY + "\">"
				+ value.CAM_NAME + "</option>";
			}
		});
		$("#CAM_PKEY").html(html);
	});
}

function quz_working_generate_faq_reply_list(CFM_PKEY) {
	var url = "/index.php/welcome/CFR_get_list/" + CFM_PKEY;
	$.get(url, "", function(result) {
		var data = $.parseJSON(result);
		var html = "";
		$.each(data.query_data, function(key, value) {
//			console.log(value);
			html += "<li>" + value.ADD_DATE + "&nbsp;" + value.CFR_DESC + "</li>"
		});
		$("#faq_reply").html(html);
	});
}

function quz_working_list_click() {
	var CFM_PKEY = $(this).attr("CFM_PKEY");

	quz_working_generate_faq_reply_list(CFM_PKEY);
	var url = "/index.php/welcome/CFM_get_data/" + CFM_PKEY;
	$.get(url, "", function(result) {
		var data = $.parseJSON(result);
		// console.log(data);
		setSpan("CFM_PKEY_span", data.CFM_PKEY);
		setText("CFM_PKEY", data.CFM_PKEY);
		setSpan("CFM_ADATE", data.ADD_DATE);
		setSpan("CCM_ID", data.CCM_ID);
		setSpan("CCM_NAME", data.CCM_NAME);
		setSpan("CFM_CONTACT_NAME", data.CFM_CONTACT_NAME);
		setSpan("CFM_CONTACT_PHONE", data.CFM_CONTACT_PHONE);
		setSpan("CFM_CONTACT_EMAIL", data.CFM_CONTACT_EMAIL);
		setSelect("CAM_PKEY", data.CAM_PKEY);
		setSelect("CFM_CODE", data.CFM_CODE);
		setSelect("CFM_TYPE", data.CFM_TYPE);
		setText("CFM_SUBJECT", data.CFM_SUBJECT);
		setSpan("CFM_QDESC", nl2br(data.CFM_QDESC, true));

		$("#quz_working_content").show();
	});
}