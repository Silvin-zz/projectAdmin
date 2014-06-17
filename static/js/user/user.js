$(document).ready(function(){
   
   $("#userAction").click(function(){
       
     $("#userAction").attr("value","new");
     $("#userId").attr("value", "");
   });
   
   $("#userSave").click(function(){
       
        $.ajax({  
      
                    url   : "/admin/user/new",
                    type    : "POST",
                    dataType: "JSON",
                    data    : $("#frmUser").serialize(),
                    success : function(result){
                            if(result.success=="true"){
                                addNewUser(result.data)
                                $('#userModal').modal('hide');
                            }
            
                      }
        });
      
       
   });
   
   
   function addNewUser(obj){
       
       cad ='<tr><td>';
       cad = cad + '<img src="/static/images/users/'  + obj.image +  '" width="40" class="img-circle" /><br />';
       cad = cad + obj.name + '<div class="color-swatch brand-primary"></div></td>';
       cad = cad + '<td>' + obj.username + '</td><td>'+ obj.profile +'</td><td>';
       cad = cad + '<button class="btn btn-xs btn-primary btn-flat taskdetail" title="edit"     action="edit"  lang="' + obj.id + '" data-toggle="modal" data-target="#userModal"><i class="glyphicon glyphicon-pencil white"></i></button>';
       cad = cad + '<button class="btn btn-xs btn-primary btn-flat taskdetail" title="remove"   action="edit"  lang="' + obj.id + '" data-toggle="modal" data-target="#userModal"><i class="glyphicon glyphicon-remove white"></i></button>';
       cad = cad + '</td></tr>';
       $("#usersBody").prepend(cad);
   }
    
});