$(document).ready(function(){
    loadTasks();
    
    
    $("#tablebody").on("click",".taskdetail",function(){
        	loadTaskDetail($(this));    
        
    });
	$(".taskdetail").on("click",function(){
	
	});

	function loadTaskDetail(element){
		var id=element.prop("lang");
		$("#taskId").prop("value",id);
		$("#frmTaskDetail").submit();

	}
	
	
	function loadTasks(){
	    $.ajax({  
			
			  url		:  "/tasks/filter",
			  type		:  "POST",
			  data		:  $("#frmmyTasks").serialize(),
			  success	: function(result){
			      $("#tablebody").html(result);
		      },
		      error: function(XMLHttpRequest, textStatus, errorThrown) { 
                    
                }   
	    }); 
	    
	}
	
	$(".period").click(function(){
	    $(".period").removeClass("active");
	    $(this).addClass("active");
	    period=$(this).attr("alt");
	    $("#taskType").val(period);
	    loadTasks();
	    
	});
	
	
	$(".type").click(function(){
	    
	    $(".type").removeClass("active");
	    $(this).addClass("active");
	    
	    finished=$(this).attr("alt");
	    $("#taskFinished").val(finished);
	    loadTasks();
	    
	});
	
	

});