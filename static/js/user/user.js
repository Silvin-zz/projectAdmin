'use strict';

angular.module('singleProjects', []);
function listController($scope, $http){
    var nuevo=false;    
    
    $scope.users     = [];
    $scope.user      = {};
    $scope.profiles  = [];
    $scope.profile   = {};
    $scope.userName  = "";
    $scope.userEmail = "";
    $scope.area      = {};
    
    
    $scope.init = function(){
        
        $scope.getUsuarios();
        $scope.getProfiles();
        $scope.getAreas();
        
    }
    
    
    $scope.newUser = function(){
        nuevo=true;
        $scope.profile   = {};
        $scope.userName  = "";
        $scope.userEmail = "";
        $scope.area      = {};
    }
    
    
    
    $scope.getProfiles = function(){
        
        $http({
                method              : 'POST',
                url                 : '/admin/profile/list',
                data                : $("#form1").serialize(),
                headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function(data){
                $scope.profiles = data;
                console.log($scope.profiles);
        });
        
        
    }
    
    
    
    $scope.getAreas = function(){
        
        $http({
                method              : 'POST',
                url                 : '/admin/area/list',
                data                : $("#form1").serialize(),
                headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function(data){
                $scope.areas = data;
                
        });
        
        
    }
    
    $scope.getUsuarios = function(){
        $http({
                method              : 'POST',
                url                 : '/admin/user/list',
                data                : $("#form1").serialize(),
                headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function(data){
                $scope.users=data;
                console.log($scope.users);
        });
        
    }
    
    
    $scope.editUser = function(user){
	nuevo            = false; 
        $scope.area      = {};
        $scope.user      = user;
        $scope.userName  = user.name;
        $scope.userEmail = user.email;
        for (var n = 0; n < $scope.profiles.length; n++){
            if($scope.profiles[n].id== user.profileid){
                $scope.profile = $scope.profiles[n];
            }
        }
        debugger;
        for (var n = 0; n < $scope.areas.length; n++){
            if($scope.areas[n].id== user.areaid){
                $scope.area = $scope.areas[n];
            }
        } 
        
    }
    
    
    
    
    $scope.saveUser = function(){
        var data={};
        data.csrfmiddlewaretoken    = $("#token").attr("value");
        data.name                   = $scope.userName;
        data.username               = $scope.userEmail;
        data.profile                = $scope.profile.id;
        data.area                   = $scope.area.id;
        
        
        $("#tmpname").attr("value",data.name);
        $("#tmpusername").attr("value",data.username);
        $("#tmpprofile").attr("value",data.profile);
        $("#tmparea").attr("value",data.area);
        
        
        if(nuevo==false){ //Usuario Modificacion
            data.id   = $scope.user.id;
            $("#tmpid").attr("value",data.id);
        }
        
        $http({
                method              : 'POST',
                url                 : '/admin/user/save',
                data                : $("#frmSave").serialize(),
                headers             : {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function(data){
                alert(data.message);
                window.location.href="/admin/users/";
                
        });
            
        
    }
    
    
    
    
    
}

