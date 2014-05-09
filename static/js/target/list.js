$(document).ready(function(){

loadTargets();
$("#projectId").change(function(event) {
	loadTargets();
});

$("#btnSaveTarget").click(function(event) {
	saveTarget();
});


$("body").append('<button class="targetdetail">Hola</button>');

$("button").on("click",function(){
	alert("ya");

	alert("saludos");
	var id=$(this).prop("lang");
	alert(id);

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