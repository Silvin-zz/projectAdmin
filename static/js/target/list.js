$(document).ready(function(){

loadTargets();

$('#datestart').datepicker({
    
    format: "yyyy/mm/dd"
}).on("changeDate",function(){
    $(this).datepicker("hide");
    
});


$('#dateend').datepicker({
    
    format: "yyyy/mm/dd"
}).on("changeDate",function(){
    $(this).datepicker("hide");
    
});

$("#projectId").change(function(event) {
    $(".type").removeClass("active");
    $(".period").removeClass("active");
    $("#periodweek").addClass("active");
    $("#typeactive").addClass("active");
    $("#taskFinished").val("active");
    $("#taskType").val("week");
	loadTargets();
});



$(".period").click(function(){
	    $(".period").removeClass("active");
	    $(this).addClass("active");
	    period=$(this).attr("alt");
	    $("#taskType").val(period);
	    loadTargets();
	    
	});
	
	
	$(".type").click(function(){
	    
	    $(".type").removeClass("active");
	    $(this).addClass("active");
	    
	    finished=$(this).attr("alt");
	    $("#taskFinished").val(finished);
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