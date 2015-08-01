function add_admin_init() {
    console.log("add_admin_init");
    add_admin_generate_list();
    $("#auth_new").click(add_admin_auth_new_click);
    $("#auth_query_apply").click(add_admin_query_click);
    
    
    $("#add_admin_update_form").validate({
		rules : {
			CAM_ID : {
				required : true,
				minlength : 4,
				maxlength : 16,
				generic_format : true
			},
			CAM_NAME : {
				required : true,
				maxlength : 16,
			},
			CAM_EMAIL : {
				email : true
			}
		},
		submitHandler: add_admin_do_update
	});
    
//    console.log("add_admin_init end");
}

function add_admin_query_click() {
	var url = "/index.php/welcome/CAM_get_list_like/"
			+ $("#auth_query_name").val();
	var adminlist = syncJsonRequest(url, "");
	add_admin_generate_admin_table(adminlist);
	
	if(adminlist.total <1)
		$().message("查無資料");

}

function add_admin_generate_list(){
	var html = "";
	var adminlist = syncJsonRequest("/index.php/welcome/CAM_get_list", "");
	add_admin_generate_admin_table(adminlist);
	
	var authlist = syncJsonRequest("/index.php/welcome/CMA_get_by_type/1", "");
	html = "";
    $.each(authlist, function(key, value) {
        html += "<option value=\""+value.CMA_PKEY+"\">"+value.CMA_NAME+"</option>";
    });
    
    $($("select[name=CMA_PKEY]")[0]).html(html);
    $($("select[name=CMA_PKEY]")[1]).html(html);
}

function add_admin_generate_admin_table(adminlist){
	var html = "";
	$.each(adminlist.query_data, function(key, value) {
		if (is_null(value.CAM_EMAIL) == true)
			value.CAM_EMAIL = "";
		
		html += "<tr cam_id='"+value.CAM_ID+"' style='cursor:pointer'><td>"+value.CAM_ID+"</td><td>"+value.CAM_NAME+"</td><td>"+value.CAM_EMAIL+"</td><td>"+value.CMA_NAME+"</td><td>"+(value.CAM_INACTIVE=='Y'?"是":'否')+"</td></tr>";
		
	});
	$("#add_admin_table tbody").html(html);

	$("#add_admin_table tr").click(function() {
		var camid = $(this).attr("cam_id");
		add_admin_feed_data(camid);
		add_admin_generate_customer_list(camid);
	});
}


function add_admin_generate_customer_list(camid){
	var postData = "CAM_PKEY=" + camid;

	$.post("/index.php/welcome/CCM_get_list_like", postData, function(result) {
		var r = $.parseJSON(result);
		console.log(r);
		var html="";
		$.each(r.query_data, function(key, value) {
			if (is_null(value.CCM_PHONE))
				value.CCM_PHONE = "";
			html +="<tr><td>"+value.CCM_NAME+"</td><td>"+value.CCM_ID+"</td><td>"+value.CCM_PHONE+"</td></tr>";
		});
		$("#customer_table tbody").html(html);
	
	});
}

function add_admin_auth_new_click() {

	$("#add_admin_form").validate({
		rules : {
			CAM_ID : {
				required : true,
				minlength : 4,
				maxlength : 16,
				generic_format : true
			},
			CAM_NAME : {
				required : true,
				maxlength : 16
			},
			CAM_PWD : {
				required : true,
				minlength : 4,
				maxlength : 16,
				generic_format : true
			},
			CAM_EMAIL : {
				email : true
			}
		},
		submitHandler: add_admin_do_add
	});
	
	

//	if (is_null($("#dialog_add_admin").dialog("instance")) == false) {
//		$("#dialog_add_admin").dialog("destroy");
//		console.log("dialog destory");
//	}

	$("#dialog_add_admin").dialog({
		minWidth : 600,
		modal: true,
		buttons : {
			"新增" : function() {
				$("#add_admin_form").submit()
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

function add_admin_do_update() {

	var postData = $("#add_admin_update_form").serializeArray();
	
	$.post("/index.php/welcome/CAM_update", postData, function(result) {
//		console.log(result);
		$().message(result);
		pageload_add_admin();
	}).fail(function() {
		$().message("失敗");
	});
}
function add_admin_do_add() {
	var postData = $("#add_admin_form").serializeArray();

	$.post("/index.php/welcome/CAM_add", postData, function(result) {
		$("#dialog_add_admin").dialog("destroy");
//		console.log(result);
		$().message(result);
		pageload_add_admin();
	}).fail(function() {
		$().message("失敗");
	});
}

function add_admin_feed_data(cam_id) {
	if (is_null(cam_id) == true)
		return;

	var url = "/index.php/welcome/CAM_get_data/" + cam_id;
	var admindata = syncJsonRequest(url, "");
	setText("CAM_PKEY", admindata.CAM_ID);
	setText("CAM_ID", admindata.CAM_ID);
	setText("CAM_NAME", admindata.CAM_NAME);
	setText("CAM_EMAIL", admindata.CAM_EMAIL);
	setText("CAM_PHONE", admindata.CAM_PHONE);
	setSelect("CAM_SYSMAIL", admindata.CAM_SYSMAIL);
	setSelect("CMA_PKEY", admindata.CMA_PKEY);
	
	if (admindata.CAM_INACTIVE == "Y")
		setCheckBox("CAM_INACTIVE", 1);
	else
		setCheckBox("CAM_INACTIVE", 0);

		
	
}