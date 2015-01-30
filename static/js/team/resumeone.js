'use strict';
angular.module('singleProjects', []);

function resumeOneController($scope, $http){

    $scope.init = function(){
        $scope.getData();
    }

    $scope.getData = function(){


        $http({
            method              : 'POST',
            url                 : "/team/resumeonelist/",
            data                : $("#frmResume").serialize(),
            headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            $scope.resume         = data;
        }).error(function(){
                SPNotification("danger", "Team Request", "You have an error in your request, please select your project first and try again.");
        });

    }
}



$(document).ready(function(){

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

});
