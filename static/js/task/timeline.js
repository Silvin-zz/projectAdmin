$(document).ready(function(){

	/** Operaciones con el timeline
		@bravocado
	 **/
	$("#btnTimeLineSave").click(function(){
		$.ajax({  
      
	        url   : "/tasks/savetimeline",
	        type    : "POST",
	        data    : $("#frmTimeLine").serialize(),
	        success : function(result){
	        	alert(result);
	          	$("#timeLineContent").html(result);
	          }
	    });

	});

});