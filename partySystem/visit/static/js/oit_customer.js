var g_cus_selected_ccmid = "";

function cus_init() {
    console.log("cus_init");
    cus_generate_option_list();
    
	var html = "";
	var cuslist = syncJsonRequest("/index.php/welcome/CCM_get_list", "");
	cus_generate_table(cuslist);
	
    $("#cus_new").click(cus_auth_new_click);
    $("#cus_query_apply").click(cus_query_click);

	$("#CCM_BDATE").datepicker({
		dateFormat : "yy-mm-dd",
		changeMonth : true,
		changeYear : true
	});
	$("#CCM_EDATE").datepicker({
		dateFormat : "yy-mm-dd",
		changeMonth : true,
		changeYear : true
	});
	$("#q_bdate").datepicker({
		dateFormat : "yy-mm-dd",
		changeMonth : true,
		changeYear : true
	});
	$("#q_edate").datepicker({
		dateFormat : "yy-mm-dd",
		changeMonth : true,
		changeYear : true
	});
	
	$("#cus_update_form").validate({
		rules : {
			CCM_ID : {
				required : true,
				minlength : 4,
				maxlength : 16,
				generic_format : true
			},
			CCM_PWD : {
				required : true,
				minlength : 4,
				maxlength : 16,
				generic_format : true
			},
			CCM_NAME : {
				required : true,
				maxlength : 16
			}
		},
		submitHandler: cus_do_update
	});
}

var test;
function cus_query_click() {
	var postData = $("#cus_query_form").serializeArray();

	$.post("/index.php/welcome/CCM_get_list_like", postData, function(result) {
		var r = $.parseJSON(result);
		cus_generate_table(r);
		if (r.total < 1)
			$().message("查無資料");
	});
}

function cus_do_update() {
	var postData = $("#cus_update_form").serializeArray();

	$.post("/index.php/welcome/CCM_update", postData, function(result) {
//		console.log(result);
		$().message(result);
		pageload_add_customer();
	});

}

function cus_generate_table(cuslist){
	var html="";
	$.each(cuslist.query_data, function(key, value) {
		if(is_null(value.CAM_EMAIL)==true)
			value.CAM_EMAIL = "";
		if(is_null(value.CAM_INACTIVE)==false && value.CAM_INACTIVE=="Y")
			value.CAM_NAME += "(停用)";

				html += "<tr ccm_id='" + value.CCM_ID + "' style='cursor:pointer'><td>"
				+ value.CCM_ID + "</td><td>" 
				+ value.CCM_NAME + "</td><td>"
				+ value.BDATE + " - " + value.EDATE + "</td><td>"
				+ (value.CCM_INACTIVE == 'Y' ? "是" : '否') + "</td><td>"
				+ value.CAM_NAME + "</td></tr>";
				
	});
	$("#cus_table tbody").html(html);
	
	$("#cus_table tr").click(function(){
		var ccmid= $(this).attr("ccm_id");
		g_cus_selected_ccmid = ccmid;
		cus_feed_data(ccmid);
		cus_feed_contacts_list(ccmid);
	});
}
function cus_feed_contacts_list(ccmid){
	if (is_null(ccmid) == true)
		return;
	var url = "/index.php/welcome/CCR_get_list_by_CCMPKEY/" +  ccmid;
	$.get(url, "", function(result) {
		var data = $.parseJSON(result);
		var html = "";
		$.each(data.query_data, function(key, value) {
//			console.log(value);
			html += "<tr id='"+value.CCR_PKEY+"'><td><span id='CCR_NAME'>"+ value.CCR_NAME +"</span></td><td><span id='CCR_PHONE'>"+ value.CCR_PHONE +"</span></td><td><span id='CCR_EMAIL'>"+ value.CCR_EMAIL +"</span></td>"
			html += "<td><button CCR_PKEY='"+value.CCR_PKEY+"' type='button' class=\"btn btn-primary\">刪除</button></td></tr>"
		});
		$("#contacts_table tbody").html(html);
		$("#contacts_table button").click(cus_del_contact);
	});
}

function cus_del_contact(){
	var CCR_PKEY = $(this).attr("CCR_PKEY");
	console.log(CCR_PKEY);
	var url = "/index.php/welcome/CCR_del/" +  CCR_PKEY;
	$.get(url, "", function(result) {
		$().message(result);
		cus_feed_contacts_list(g_cus_selected_ccmid);
	});
}

function cus_feed_data(ccmid){

	if (is_null(ccmid) == true)
		return;

	var url = "/index.php/welcome/CCM_get_data/" + ccmid;
	var data = syncJsonRequest(url, "");

	setText("CCM_PKEY", data.CCM_PKEY);
	setText("CCM_ID", data.CCM_ID);
	setText("CCM_NAME", data.CCM_NAME);
	setText("CCM_BDATE", data.BDATE);
	setText("CCM_EDATE", data.EDATE);
	setSelect("CMA_PKEY", data.CMA_PKEY);
	setSelect("CAM_PKEY", data.CAM_PKEY);
	
	if (data.CCM_INACTIVE == "Y")
		setCheckBox("CCM_INACTIVE", 1);
	else
		setCheckBox("CCM_INACTIVE", 0);

}

function cus_generate_option_list(){
	var html = "";
//權限名稱	
	var typelist = syncJsonRequest("/index.php/welcome/CMA_get_by_type/2", "");
	html = "";
    $.each(typelist, function(key, value) {
        html += "<option value=\""+value.CMA_PKEY+"\">"+value.CMA_NAME+"</option>";
    });
    
    $($("select[name=CMA_PKEY]")[0]).html(html);
    $($("select[name=CMA_PKEY]")[1]).html(html);
//指定客服
	var CAMlist = syncJsonRequest("/index.php/welcome/CAM_get_list/", "");
	html = "";
	$.each(CAMlist.query_data, function(key, value) {
		if (value.CAM_INACTIVE == "Y") {
			html += "<option value=\"" + value.CAM_PKEY + "\">"
					+ value.CAM_NAME + "(停用)</option>";
		}
		else{
			html += "<option value=\"" + value.CAM_PKEY + "\">"
			+ value.CAM_NAME + "</option>";
		}
	});
    $($("select[name=CAM_PKEY]")[0]).html(html);
    $($("select[name=CAM_PKEY]")[1]).html(html);
    
}

function cus_auth_new_click(){
	$("#CCM_BDATE_frm").datepicker({
		dateFormat : "yy-mm-dd",
		changeMonth : true,
		changeYear : true
	});
	$("#CCM_EDATE_frm").datepicker({
		dateFormat : "yy-mm-dd",
		changeMonth : true,
		changeYear : true
	});
	
	$("#cus_add_form").validate({
		rules : {
			CCM_ID : {
				required : true,
				minlength : 4,
				maxlength : 16,
				generic_format : true
			},
			CCM_PWD : {
				required : true,
				minlength : 4,
				maxlength : 16,
				generic_format : true
			},
			CCM_NAME : {
				required : true,
				maxlength : 16
			}
		},
		submitHandler: cus_do_add
	});
	
	$("#dialog_customer").dialog({
		minWidth : 600,
		modal: true,
		buttons : {
			"新增" : function() {
				$("#cus_add_form").submit();
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

function cus_do_add() {
	var postData = $("#cus_add_form").serializeArray();

	$.post("/index.php/welcome/CCM_add", postData, function(result) {
		$("#dialog_customer").dialog("destroy");
		// console.log(result);
		$().message(result);
		pageload_add_customer();
	});

}