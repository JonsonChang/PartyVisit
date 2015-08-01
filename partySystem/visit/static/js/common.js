var g_SEX_code = {
	"0" : "女",
	"1" : "男"
}
var g_YN_code = {
		"0" : "否",
		"1" : "是"
}

var g_EDU_code = {
	"7" : "博士",
	"6" : "碩士",
	"5" : "學士",
	"4" : "專科",
	"3" : "高中/職",
	"2" : "國中",
	"1" : "國小"
}

var g_isEDU_code = {
	"0" : "畢業",
	"1" : "就讀"
}

var g_RELIGION_code = {
	"1" : "佛教",
	"2" : "回教",
	"3" : "道教",
	"4" : "天主教",
	"5" : "基督教",
	"6" : "一貫道",
	"7" : "無",
	"8" : "其他"
}

var g_PERSON_status = {
	"0" : "無狀態",
	"1" : "拒決",
	"2" : "認同",
	"9" : "已入黨"
}



function load_page(content, url, fn) {
	$.get(url, function(data) {
		$(content).html(data);
		if (fn)
			fn();
	});
}

function syncJsonRequest(url, data) {
	var r={};
	$.ajax({
		url : url,
		async : false,
		method : "GET",
		dataType : "json",
		data : data
	}).done(function(jsondata) {
//		console.log("ok");
		$.extend(r,jsondata);
	}).error(function(data) {
//		console.log("error");
	});
	return r;
}

function is_null(obj) {
	if (typeof (obj) == 'undefined' || obj == null)
		return true;
	return false;
}  

function id(myid) {
	return myid.replace(/(\b\w+\b(\.*\w*)*)/g, "#$1")
			.replace(/(:|\.)/g, '\\$1');
}

function setSpan(elem_id, value) {
	var elem = $(id(elem_id));
	if (elem.is("span") && elem.length == 1) {
		elem.html( value);
	} else
		console.warn('setSpan() cannot find id:' + elem_id);
}

function setText(elem_id, value) {
	var elem = $(id(elem_id));
	if (elem.is("input") && elem.length == 1) {
//		elem.attr('value', value);
		elem.val(value);
	} else
		console.warn('setText() cannot find id:' + elem_id);
}

function setTextarea(elem_id, value) {
	var elem = $(id(elem_id));
	if (elem.is("textarea") && elem.length == 1) {
		elem.val(value);
	} else
		console.warn('setTextarea() cannot find id:' + elem_id);
}

function setSelect(elem_id, value_in) {
	var value = "";
	
	if(is_null(value_in)==false)
		value = value_in.toString();
	
	var elem = $(id(elem_id));
	if (elem.is("select") && elem.length == 1) {
//		elem.attr('value', value);
		elem.val(value);
		if (elem.val() != value) {
			elem.children("option:first-child").attr("selected", true);
			console.warn('setSelect() cannot match value:', elem_id,
					elem.val(), value);
		}
	} else
		console.warn('setSelect() cannot find id:' + elem_id);
}

function getSelectText(elem_id) {
	var elem = $(id(elem_id));
	if (elem.is("select") && elem.length == 1) {
		return elem.find("option:selected").text();
	} else
		console.warn('getSelectText() cannot find id:' + elem_id);
}

function setCheckBox(elem_id, value) {
	var elem = $(id(elem_id));

	if (elem.is("input") && elem.length == 1) {
		if (value == '1')
			elem.attr("checked", true);
		else
			elem.attr("checked", false);
	} else
		console.warn('setCheckBox() cannot find id:' + elem_id);
}

function setRadio(elem_id, value) {
	var select_str = "input[name=\"" + elem_id + "\"][value=\"" + value + "\"]";
	var elem = $(select_str);

	if (elem.length == 1) {
		elem.attr('checked', true);
	} else
		console.warn('setRadio() cannot find name:' + elem_id);
}

function getRadio(input_name) {
	return $("input[type=radio][name='" + input_name + "']:checked").val();
}

function nl2br (str, is_xhtml) {   
    var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';    
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1'+ breakTag +'$2');
}

function faqcode2str(code) {
	if (is_null(code) == true) {
		return "";
	}
	
	var ret = eval("g_FAQ_code." + code);
	if(is_null(ret)==false)
		return ret;
	else
		return "";
}
