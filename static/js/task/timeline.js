$(document).ready(function(){

	/** Operaciones con el timeline
		@bravocado
	 **/
	$("#btnTimeLineSave").click(function(){
		alert("iniciamos");
		$.ajax({  
      
	        url   : "/tasks/savetimeline",
	        type    : "POST",
	        data    : $("#frmTimeLine").serialize(),
	        success : function(result){
	          	$("#timeLineContent").html(result);
	          }
	    });

	});

});