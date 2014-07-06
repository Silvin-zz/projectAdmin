'use strict';

angular.module('singleProjects', []);

function listController($scope, $http){
    $scope.targets          =[];
    $scope.master           ={};
    
    $scope.init=function(){

        $scope.datestart        =$("#datestart").attr("data");
        $scope.dateend          =$("#dateend").attr("data");        
    }



    $scope.showModal        =function(){

        $scope.datestart=$("#datestart").attr("data");
        
        

    }

    $scope.submit           =function(){
        
        var projectid       =$("#projectId option:selected").first().prop("value");
        var title           =$("#title").val();
        var datestart       =$scope.datestart;
        var dateend         =$scope.dateend;

        $("#project").prop("value",projectid);
        $('#modalclose').trigger("click");
        $("#loadingModal").modal("show");

        $http({
            method      : 'POST',
            url         : '/target/save',
            data        : $("#frmNewtarget").serialize(),
            headers     : {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            $("#loadingModal").modal("hide");
            $scope.title        ="";
            $scope.code         ="";
            $scope.description  ="";
            $scope.targets.unshift(data[0]); //Con solo esta linea agrego un nuevo registro a la lista :D de pelos :D
            $('#frmNewtarget')[0].reset();
            SPNotification("success", "New Target", "The " + title + " Target has been created");

            //$scope.targets.push (data[0]);
        });
    }








    $scope.changetargetsProject =function(){
        $http({
            method      : 'POST',
            url         : '/target/getbyproject',
            data        : $("#frmGetTargets").serialize(),
            headers     : {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            $scope.targets = data;
        });
    } 

    $scope.getTargetData=function(targetId){
        $("#targetid").val(targetId);
        $http({
                method      : 'POST',
                url         : '/target/get',
                data        : $("#frmTargetDetail").serialize(),
                headers     : {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function(data){
                var target      = data[0];
                $("#myModal").modal("show");
                $scope.title        =target.title;
                $scope.code         =target.code;
                $scope.description  =target.description;
                $scope.datestart    =target.datestart;
                $scope.dateend      =target.dateend;
                debugger;

        });
    }



    $scope.removetarget=function(targetId, indexelement){
        
        var rowContent  =$("#remove_" + targetId).parent().parent();
        rowContent.parent().parent().removeClass('table-striped');
        $(rowContent).addClass("danger");

        $("#targetid").val(targetId);
        var index       = indexelement;

        confirmModalDialog("Remove Target", "¿ Are you Sure to remove this Target ?", 
            function(){
                $("#loadingModal").modal("show");
                $http({
                    method      : 'POST',
                    url         : '/target/remove',
                    data        : $("#frmTargetDetail").serialize(),
                    headers     : {'Content-Type': 'application/x-www-form-urlencoded'}
                }).success(function(data){
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




} //FIn de angular 


$(document).ready(function(){

//loadTargets();

$('#datestart').datepicker({
    
    format: "yyyy-mm-dd"
}).on("changeDate",function(){
    $(this).datepicker("hide");
    
});


$('#dateend').datepicker({
    
    format: "yyyy-mm-dd"
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
    //loadTargets();
});



$(".period").click(function(){
        $(".period").removeClass("active");
        $(this).addClass("active");
        var period=$(this).attr("alt");
        $("#taskType").val(period);
        loadTargets();
        
    });
    
    
    $(".type").click(function(){
        
        $(".type").removeClass("active");
        $(this).addClass("active");
        
        var finished=$(this).attr("alt");
        $("#taskFinished").val(finished);
        loadTargets();
        
    });


$("#btnSaveTarget").click(function(event) {
   // saveTarget();
});


function saveTarget(){
    var projectid=$("#projectId option:selected").first().prop("value");
    
    $("#project").prop("value",projectid);
    $('#modalclose').trigger("click");
    $("#loadingModal").modal("show");
    var title           =$("#title").val();
    $.ajax({  
        url         : "/target/save",
        type        : "POST",
        data        : $("#frmNewtarget").serialize(),
        success : function(result){
            $("#loadingModal").modal("hide");
            $('#frmNewtarget')[0].reset();
            $("#targetList").prepend(result);
            SPNotification("success", "New Target", "The " + title + " Target has been created");
            
            $("#listcontent .targetdetail").on("click",function(){
                redirectToDetail($(this));                  
            });
        }
    });


}

function loadTargets(){
    
    $.ajax({  
        url         : "/target/getbyproject",
        type        : "POST",
        data        : $("#frmGetTargets").serialize(),
        success : function(result){
            $("#listcontent").html(result);
        }
    });
}


function redirectToDetail(button){
    var id  =button.attr("lang");
    $("#targetid").prop("value",id);
    $("#frmTargetDetail").submit();
    return false;

}

    $("#listcontent").on("click", ".targetdetail",function(){
        redirectToDetail($(this));                  
    });

});