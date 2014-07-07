$(document).ready(function(){

	/** Operaciones con el timeline
		@bravocado
	 **/
	$("#btnTimeLineSave").click(function(){
	    
	    confirmModalDialog("Confirm Time Line", "¿ Are you Sure to save this Time Line ?", 
            function(){
        		$.ajax({  
              
        	        url   : "/tasks/savetimeline",
        	        type    : "POST",
        	        data    : $("#frmTimeLine").serialize(),
        	        success : function(result){
        	            
        	        	$("#occupiedhours").val("");
        	        	$("#timeLineActivity").val("");
        	        	$("#reference1").val("");
        	        	$("#reference2").val("");
        	          	$("#timeLineContent").html(result);
        	          	
        	          }
        	    });
            },
            function(){  //Cancel confirm
                
            }
        );

	});

});