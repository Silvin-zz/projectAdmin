'use strict';
alert("saludos");
angular.module('singleProjects', []);

function catalogController($scope, $http){

    $scope.catalogtype  = [];
    $scope.catalogs     = [];
    

    $scope.init = function(){
        
        $scope.catalogtype =[
                                { "name": "Target   Type"   , "id": "targettype"},
                                { "name": "Task Type"       , "id": "tasktype"  },
                                { "name": "Priority"        , "id": "priority"  },
                            ];
        
        
    }
    
    $scope.getList = function(){
        
       
        
    }
    
}