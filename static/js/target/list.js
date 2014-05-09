$(document).ready(function(){

loadTargets();

$("#projectId").change(function(event) {
	loadTargets();
});


$("#btnSaveTarget").click(function(event) {
	saveTarget();
});


function saveTarget(){
	var projectid=$("#projectId option:selected").first().prop("value");
	
	$("#project").prop("value",projectid);


	$.ajax({  
		url			: "/target/save",
		type		: "POST",
		data		: $("#frmNewtarget").serialize(),
		success	: function(result){
			$('#frmNewtarget')[0].reset();
			$("#targetList").prepend(result);
			$('#modalclose').trigger("click");
			$("#listcontent .targetdetail").on("click",function(){
				redirectToDetail($(this));					
			});
		}
	});


}

function loadTargets(){
	
	$.ajax({  
		url			: "/target/getbyproject",
		type		: "POST",
		data		: $("#frmGetTargets").serialize(),
		success	: function(result){
			$("#listcontent").html(result);
			$("#listcontent .targetdetail").on("click",function(){
				redirectToDetail($(this));					
			});
		}
	});
}


function redirectToDetail(button){
	var id 	=button.attr("lang");
	$("#targetid").prop("value",id);
	$("#frmTargetDetail").submit();
	return false;

}

});