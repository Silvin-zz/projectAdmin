$(document).ready(function(){

   var folderId                 = $("#folderReference").attr("value");
   var document                 = new DocumentClass();
   document.formComunitationId  ="frmDocument";
   document.rootFolderId        = folderId;
   document.init();
   document.getDriveList();
   
});