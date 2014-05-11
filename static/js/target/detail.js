$(document).ready(function(){


	$(".dial").knob({ readOnly:true });
	$("#taskList .taskdetail").click(function(){
		loadTaskDetail($(this));
	});
	


	$("#btnNewTask").on("click",function(){
		$("#title").val("");
		$("#description").val("");
		$("#title").focus();


	});

	$("#btnSaveTask").on("click",function(){

		$.ajax({  
			url			: "/tasks/save",
			type		: "POST",
			data		: $("#frmNewTask").serialize(),
			success	: function(result){
				$("#taskList").prepend(result);
				$("#modalclose").trigger('click');
				$(".taskdetail").on("click",function(){
					loadTaskDetail($(this));
				});

			}
		});
	});




	function loadTaskDetail(btn){
		id=btn.prop("lang");
		$("#taskId").prop("value", id);
		$("#frmTaskDetail").submit();

	}

});



