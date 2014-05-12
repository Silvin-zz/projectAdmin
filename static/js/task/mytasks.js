$(document).ready(function(){

	$(".taskdetail").on("click",function(){
		loadTaskDetail($(this));

	});

	function loadTaskDetail(element){
		var id=element.prop("lang");
		$("#taskId").prop("value",id);
		$("#frmTaskDetail").submit();

	}

});