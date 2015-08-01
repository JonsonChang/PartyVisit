

function person_init() {
    console.log("person_init");
	
    var url = g_base_url + "index.php/welcome/users_get/H123061198";
	$.getJSON(url, function(data) {
//				console.log(data);
				setSpan("person_name", data.name);
				setSpan("person_sex", g_SEX_code[data.sex]);
				setSpan("person_birthday", data.birthday);
				setSpan("person_users_id", data.users_id);
				setSpan("person_introducer", data.introducer);
				setSpan("person_introducer_phone", data.introducer_phone);
				setSpan("person_email", data.email);
				setSpan("person_tel_office", data.tel_office);
				setSpan("person_tel_home", data.tel_home);
				setSpan("person_tel_mobile", data.tel_mobile);
				setSpan("person_address", data.address);
				setSpan("person_address_com", data.address_com);
				setSpan("person_edu", g_EDU_code[data.edu]);
				setSpan("person_in_school", g_isEDU_code[data.in_school]);
				setSpan("person_school", data.school);
				setSpan("person_major", data.major);
				setSpan("person_company", data.company);
				setSpan("person_title", data.title);
				setSpan("person_religion", g_RELIGION_code[data.religion]);
				setSpan("person_is_other_political_party",	g_YN_code[data.is_other_political_party]);
		
	}).error(function() { console.log("error"); });
	
	
//    
//    
//    
//	var cuslist = syncJsonRequest("/index.php/welcome/CCM_get_list", "");
//	cus_generate_table(cuslist);
//	
//    $("#cus_new").click(cus_auth_new_click);
//    $("#cus_query_apply").click(cus_query_click);
//
//	$("#CCM_BDATE").datepicker({
//		dateFormat : "yy-mm-dd",
//		changeMonth : true,
//		changeYear : true
//	});
//	$("#CCM_EDATE").datepicker({
//		dateFormat : "yy-mm-dd",
//		changeMonth : true,
//		changeYear : true
//	});
//	$("#q_bdate").datepicker({
//		dateFormat : "yy-mm-dd",
//		changeMonth : true,
//		changeYear : true
//	});
//	$("#q_edate").datepicker({
//		dateFormat : "yy-mm-dd",
//		changeMonth : true,
//		changeYear : true
//	});
//	
//	$("#cus_update_form").validate({
//		rules : {
//			CCM_ID : {
//				required : true,
//				minlength : 4,
//				maxlength : 16,
//				generic_format : true
//			},
//			CCM_PWD : {
//				required : true,
//				minlength : 4,
//				maxlength : 16,
//				generic_format : true
//			},
//			CCM_NAME : {
//				required : true,
//				maxlength : 16
//			}
//		},
//		submitHandler: cus_do_update
//	});
}
