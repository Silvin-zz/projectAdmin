'use strict';

angular.module('singleProjects', []);

function catalogController($scope, $http){

    $scope.catalogtype  = [];
    $scope.catalogs     = [];
    $scope.type         = "";
    

    $scope.init = function(){
        
        $scope.loadTypes('targettype');
        $scope.catalogtype =[
                                { "name": "Target Type"     , "id": "targettype"},
                                { "name": "Task Type"       , "id": "tasktype"  },
                                { "name": "Priority"        , "id": "priority"  },
                            ];
        
        
    }
    
    $scope.loadTypes = function(type){
        $scope.type  = type;
        $http({
            method                  : 'GET',
            url                     : '/catalogs/list?name='+  type,
            data                    : {"name": type},
            //headers                 : {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            $scope.catalogs      = data;
        }).error(function(){
                SPNotification("danger", "Target Request", "You have an error in your request, please select your project first and try again.");
        });
       
        
    }
    
    $scope.remove = function(item){
    
        var index = $scope.catalogs.indexOf(item);
        var type  = $scope.type;
        var id    = item.id;
        
         confirmModalDialog("Remove Target", "¿ Are you Sure to remove this Target ?", 
         
            function(){
                
              
                $http({
                    method                  : 'GET',
                    url                     : '/catalogs/remove?id='+  id + "&name=" + type,
                    data                    : {"name": type},
                    //headers                 : {'Content-Type': 'application/x-www-form-urlencoded'}
                }).success(function(data){
                    $scope.catalogs.splice(index, 1);
                    SPNotification("success", "Catalog", "Your item was deleted");
                }).error(function(){
                        SPNotification("danger", "Catalog Request", "You have an error in your request, please select your project first and try again.");
                });
                return false;
            },function(){
                
                return false;
            }
        );
    }
    
    
    $scope.save=function(name){
        name=$("#name").val();
        var type=$scope.type;
        confirmModalDialog("Add Target", "¿ Are you Sure to Add this Target ?", 
            function(){
                $http({
                    method                  : 'GET',
                    url                     : '/catalogs/save?value='+  name + "&name=" + type,
                    data                    : {"name": type},
                    //headers                 : {'Content-Type': 'application/x-www-form-urlencoded'}
                }).success(function(data){
                    $scope.loadTypes(type);
                    SPNotification("success", "Catalog", "Your item was created");
                }).error(function(){
                        SPNotification("danger", "Catalog Request", "You have an error in your request, please select your project first and try again.");
                });
            },function(){
                
                
            }
        );
        
    }
    
    
    
    
    
}


$(".period").click(function(){
    
   $(".period").removeClass("active");
   $(this).addClass("active");
});