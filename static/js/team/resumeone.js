'use strict';
angular.module('singleProjects', ["ngSanitize", "ngCsv"]);

function resumeOneController($scope, $http){

    $scope.getArray     = [];
    $scope.fileName     = "tiempo_por_proyecto.csv";
    $scope.getHeader    = function () {return ["Usuario", "Actividad", "Título", "Descripción","Fecha" ,  "Duración"]};


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
            $scope.generaCSV();
        }).error(function(){
                SPNotification("danger", "Team Request", "You have an error in your request, please select your project first and try again.");
        });

    }

    $scope.generaCSV = function(){
        debugger;
        for(var a = 0; a < $scope.resume.length; a++ ){

            $scope.getArray.push({"user": $scope.resume[a].owner.name,  "activity": $scope.resume[a].activity, "title": $scope.resume[a].title,  "description": $scope.resume[a].description,  "date": $scope.resume[a].date,   "total": $scope.resume[a].duration });

        }
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
