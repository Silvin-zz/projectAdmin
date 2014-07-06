'use strict';

angular.module('singleProjects', []);
/**
    We Use angular for validate the HTML components (this code live in html pages) and to set the component value
    this funcionality must implement with ajax request, but we dont have an REST API, and for a moment, we put the value
    in data property and here set the object value whith data value.
    silvio.bravo
**/
function contentController($scope) {


    $scope.master           ={};
    $scope.title            =$("#title").attr("data");
    $scope.code             =$("#code").attr("data");
    $scope.clientid         =$("#clientid").attr("data");
    $scope.datestart        =$("#datestart").attr("data");
    $scope.dateend          =$("#dateend").attr("data");
    $scope.owner            =$("#owner").attr("data");
    $scope.projecttypeid    =$("#projecttypeid").attr("data");
    $scope.description      =$("#description").attr("data");
    $scope.id               =$("#projectId").attr("data");
    
}
function newClientController($scope){
    

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

    $("#btnSave").click(function(){
        $("#loadingModal").modal("show");
    });

});
