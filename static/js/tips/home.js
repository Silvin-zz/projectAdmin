$(document).ready(function(){
    
   
   
   $("#search").click(function(){
       search();
       
   });
   
   $("#text").keyup(function(e){
      if(e.keyCode==13){
          search();
      } 
   });
   
   function search(){
       
       $("#tiplist").html('<div class="row col-xs-12 text-center" style="margin-top:100px;"><img src="/static/theme/img/ajax-loader.gif"></div>');
       
       text=$("#text").val();
       $("#textsearch").val(text);
        $.ajax({  
			
			  url		:  "/tips/search",
			  type		:  "POST",
			  data		:  $("#frmTips").serialize(),
			  success	: function(result){
			      $("#tiplist").html(result);
		      },
		      error: function(XMLHttpRequest, textStatus, errorThrown) { 
                    
                }   
	    });
   }
    
});