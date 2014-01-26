
$(document).ready(function(){
	$("#commentform").ajaxForm({
		beforeSubmit: validateForm,
		success:dealResponse
	});

	// $("a.js-side-nav-item").bind('click',function(){
	// 	$(this).attr('href',$(this).attr('id'));
	// 	$(this).parent().siblings('li').find('a').removeClass('selected');
	// 	$(this).addClass('selected');
	// 	return false;
	// });
	// $("#contactform").ajaxForm({
	// 	success:dealContact
	// })
	
	$('a.comment-reply-link').bind('click',function(){
		var commentDiv=$("div#commentAdd").clone();

		//commentDiv.slideToggle("slow");

		var commentThis=$(this).parents('li');
		commentThis.append(commentDiv);
		// 赋值
		var replyId=$(this).parents('li').attr('id').split('-')[1];
		$("input#id_msg_reply",commentDiv).val(replyId);
		return false;
	});
});
function showCategory(obj,url){
	$(obj).attr('href',url);
	$(obj).parent().siblings('li').find('a').removeClass('selected');
	$(obj).addClass('selected');	
}
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