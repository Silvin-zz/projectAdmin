$(document).ready(function(){

   var folderId                 = $("#folderReference").attr("value");
   var folderName               = $("#folderRootName").attr("value");
   $("#folderIdParent").attr("value", folderId);
   var document                 = new DocumentClass();
   document.breadcrumbId        ="breadcrumbDocument";
   document.breadcrumbRoot      = folderName;
   document.formComunitationId  ="frmDocument";
   document.rootFolderId        = folderId;
   document.init();
   document.getDriveList();
   
});