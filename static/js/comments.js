
$(document).ready(function(){
	$("#id_content_type").val(22);
	 $("#id_object_id").val(2);
	$("#commentform").ajaxForm({
		beforeSubmit: validateForm,
		success:dealResponse
	});

	// $("#contactform").ajaxForm({
	// 	success:dealContact
	// })
});

function validateForm(arr,$form,options){
	for(item in arr){
		var obj=arr[item];
		var name=obj.name;
		var value=obj.value;
		// if(name=='content_type'){
		// 	value=22;
		// }
		// if(name=='object_id')
		// {
		// 	value=2;
		// }
		if(name=='msg_user'||name=='msg_email'||name=='msg_content'){
			if((name=='msg_user'&&value=='昵称')||(name=='msg_email'&&value=='邮箱')){
				value='';
			}
			if(value==''||typeof(value)== undefined){
				alert("提交信息有误，请重新填写！");
				return false;
			}
		}
	}
}

function dealResponse(responseText,statusText){
	if(responseText=='0'){
		alert("评论保存失败");
	}else{
		alert("评论成功");
	}
}

function dealContact(responseText,statusText)
{
	alert(responseText);
}