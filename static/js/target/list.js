'use strict';

angular.module('singleProjects', []);

function listController($scope, $http){
    $scope.targets          =[];
    $scope.master           ={};
    
    $scope.init=function(){

        $scope.datestart    =$("#datestart").attr("data");
        $scope.dateend      =$("#dateend").attr("data");        
    }



    $scope.showModal        =function(){

        $scope.datestart=$("#datestart").attr("data");
        $scope.title        ="";
        $scope.code         ="";
        $scope.description  ="";
        $scope.datestart    ="";
        $scope.owner        ="";
        $scope.dateend      ="";
        $scope.targettype   ="";
        $scope.id           ="";
        $("#id").val($scope.id);
        
        

    }

    $scope.submit           =function(){
        
        var projectid       =$("#projectId option:selected").first().prop("value");
        var title           =$("#title").val();
        var datestart       =$scope.datestart;
        var dateend         =$scope.dateend;
        var id              =$scope.id;

        $("#project").prop("value",projectid);
        $('#modalclose').trigger("click");
        $("#loadingModal").modal("show");

        $http({
            method              : 'POST',
            url                 : '/target/save',
            data                : $("#frmNewtarget").serialize(),
            headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            $("#loadingModal").modal("hide");
            $scope.title        ="";
            $scope.code         ="";
            $scope.description  ="";

            if(id==""){
                SPNotification("success", "New Target", "The " + title + " Target has been created");
                $scope.targets.unshift(data[0]); //Con solo esta linea agrego un nuevo registro a la lista :D de pelos :D
                $("#listcontent").on("click", ".targetdetail",function(){
                    redirectToDetail($(this));                  
                });
            }
            else{  //Buscamos por id
                for(var n=0; n < $scope.targets.length; n++){
                    if($scope.targets[n].id==id){
                        $scope.targets[n]=data[0];
                        break;           
                    }
                }
                SPNotification("info", "Update Target", "The " + title + " Target has been Modified");

            }
            

            //$scope.targets.push (data[0]);
        });
    }








    $scope.changetargetsProject =function(){
        $http({
            method                  : 'POST',
            url                     : '/target/getbyproject',
            data                    : $("#frmGetTargets").serialize(),
            headers                 : {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            $scope.targets      = data;
        }).error(function(){
                SPNotification("danger", "Target Request", "You have an error in your request, please select your project first and try again.");

        });
    } 


    $scope.finishTarget=function(targetId, index){
        confirmModalDialog("Close Target", "¿ Are you Sure to close this Target ?", 
            function(){
                $("#loadingModal").modal("show");
                $("#targetid").val(targetId);
                $http({
                        method              : 'POST',
                        url                 : '/target/finish',
                        data                : $("#frmTargetDetail").serialize(),
                        headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
                    }).success(function(data){
                        $("#loadingModal").modal("hide");
                        $("#finish_" + targetId).attr("disabled","disabled");
                        SPNotification("success", "Close Target", "The target was Closed");
                });

            },
            function(){  //Cancel confirm
                
            }
        );

    }

    $scope.getTargetData=function(targetId){
        $("#targetid").val(targetId);
        $http({
                method              : 'POST',
                url                 : '/target/get',
                data                : $("#frmTargetDetail").serialize(),
                headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function(data){
                var target          = data[0];
                $("#myModal").modal("show");
                $scope.title        =target.title;
                $scope.code         =target.code;
                $scope.description  =target.description;
                $scope.datestart    =target.datestart;
                $scope.owner        =target.owner.id;
                $scope.dateend      =target.dateend;
                $scope.targettype   =target.targettype;
                $scope.id           =target.id;
                $("#id").val($scope.id);
                $("#project").val($("#projectId").val());
                

        });
    }



    $scope.removetarget=function(targetId, indexelement){
        
        var rowContent              =$("#remove_" + targetId).parent().parent();
        rowContent.parent().parent().removeClass('table-striped');
        $(rowContent).addClass("danger");

        $("#targetid").val(targetId);
        var index                   = indexelement;

        confirmModalDialog("Remove Target", "¿ Are you Sure to remove this Target ?", 
            function(){
                $("#loadingModal").modal("show");
                $http({
                    method          : 'POST',
                    url             : '/target/remove',
                    data            : $("#frmTargetDetail").serialize(),
                    headers         : {'Content-Type': 'application/x-www-form-urlencoded'}
                }).success(function(data){

                    for(var n=0; n < $scope.targets.length; n++){
                        if($scope.targets[n].id==id){
                            index=n;
                            break;           
                        }
                    }
                    alert(index);
                    $scope.targets.splice(index, 1);
                    SPNotification("success", "Remove Target", "The Target was removed");
                    $("#loadingModal").modal("hide");
                });
            },
            function(){  //Cancel confirm
                rowContent.parent().parent().addClass('table-striped');
                rowContent.removeClass("danger");
            }
        );

    }

    $scope.redirect=function(targetId){

        $("#targetid").prop("value",targetId);
        $("#frmTargetDetail").submit();
        return false;

    }



    $scope.loadTargets=function(type){
        $("#taskType").val(type);
        $scope.changetargetsProject();

    }

    $scope.loadTargetsbyStatus=function(type){
        $("#taskFinished").val(type);
        $scope.changetargetsProject();

    }


} //FIn de angular 


$(document).ready(function(){

//loadTargets();

    


$("#projectId").change(function(event) {
    /*$(".type").removeClass("active");
    $(".period").removeClass("active");
    $("#periodweek").addClass("active");
    $("#typeactive").addClass("active");
    $("#taskFinished").val("active");
    $("#taskType").val("week");
    */
    //loadTargets();
});



    $(".period").click(function(){
        $(".period").removeClass("active");
        $(this).addClass("active");
    });
    
    
    $(".type").click(function(){
        
        $(".type").removeClass("active");
        $(this).addClass("active");
    });




    // $("#listcontent").on("click", ".targetdetail",function(){
    //     redirectToDetail($(this));                  
    // });


    function redirectToDetail(button){
        var id  =button.attr("lang");
        $("#targetid").prop("value",id);
        $("#frmTargetDetail").submit();
        return false;

    }

});