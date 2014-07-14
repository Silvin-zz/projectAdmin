'use strict';
angular.module('singleProjects', []);

function teamController($scope, $http){
    $scope.team     =[];
    
    
    $scope.init = function(){
	var url="/team/resume/" + $("#extraparams").val();
        $http({
            method              : 'POST',
            url                 : url,
            data                : $("#frmTeam").serialize(),
            headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            $scope.team         = data;
        }).error(function(){
                SPNotification("danger", "Team Request", "You have an error in your request, please select your project first and try again.");
        });
        
    }
    
    
    $scope.getData = function(type){
        $("#type").val(type);
        $scope.init();
    
    }
}




$(document).ready(function(){
   $(".period").click(function(){
       
       $(".period").removeClass("active");
       $(this).addClass("active");
       
       
   });
    
    
});
