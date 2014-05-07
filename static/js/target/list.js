$(document).ready(function(){

loadTargets();
$("#projectId").change(function(event) {
	loadTargets();
});

$("#btnSaveTarget").click(function(event) {
	saveTarget();
});


function saveTarget(){
	var projectid=$("#projectId option:selected").first().attr("value");
	alert(projectid);
	$("#project").attr("value",projectid);


	$.ajax({  
		url			: "/target/save",
		type		: "POST",
		data		: $("#frmNewtarget").serialize(),
		success	: function(result){
			$("#targetList").html(result);
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
		}
	});
}

});