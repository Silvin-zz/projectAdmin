
/**
 * Clase para el manejo de google drive a través de javacript e integración con el servidor para algunas peticiones :)
 * */

function DocumentClass(){
    this.breadcrumbId         = "breadcrumb";
    this.formComunitationId   = "frmNewFolder";
    this.fileObjectId         = "filePicker"; 
    this.contentFilesId       = "driveList";
    this.token                = "";
    
    this.init=function(){
        this.listenUpload();
        
    }
    
    this.listenUpload=function(){
        var owner=this;
        $("#" + this.fileObjectId).change(function(e){
            var files = e.target.files;
            owner.uploadFile(files);
        });
        
    }
    
    
    this.getToken=function(callback){
        var owner=this;
        $.ajax({  
			url			: "/document/getToken",
			type		: "POST",
			data		: $("#" + this.formComunitationId).serialize(),
			success	: function(result){
			    gapi.auth.setToken(result);
			    if (typeof callback === "function"){
			        callback();
			    }
			}
		});
        
    }
    
    this.uploadFile=function(files){
        var owner=this;
        $.ajax({  
			url			: "/document/getToken",
			type		: "POST",
			data		: $("#" + this.formComunitationId).serialize(),
			success	: function(result){
			    
			    gapi.auth.setToken(result);
			    gapi.client.load('drive', 'v2', function() {
                  var file = files[0];
                  owner.insertFile(file);
                });
                
			    
			}
		});
        
        
    } 
    
    
    
    this.insertFile=function(fileData, callback) {
        owner=this;
        const boundary = '-------314159265358979323846';
        const delimiter = "\r\n--" + boundary + "\r\n";
        const close_delim = "\r\n--" + boundary + "--";

        var reader = new FileReader();
        reader.readAsBinaryString(fileData);
        reader.onload = function(e) {
          var contentType = fileData.type || 'application/octet-stream';
          var metadata = {
            'title': fileData.name,
            'mimeType': contentType
          };

          var base64Data = btoa(reader.result);
          var multipartRequestBody =
              delimiter +
              'Content-Type: application/json\r\n\r\n' +
              JSON.stringify(metadata) +
              delimiter +
              'Content-Type: ' + contentType + '\r\n' +
              'Content-Transfer-Encoding: base64\r\n' +
              '\r\n' +
              base64Data +
              close_delim;

          var request = gapi.client.request({
              'path': '/upload/drive/v2/files',
              'method': 'POST',
              'params': {'uploadType': 'multipart', 'parents':[{'id': 'root'}]},
              'headers': {
                'Content-Type': 'multipart/mixed; boundary="' + boundary + '"'
              },
              'body': multipartRequestBody});
          if (!callback) {
            callback = function(file) {
              debugger;
              alert("llegamos :)");
              owner.printFile(file);    
              
            };
          }
          request.execute(callback);
        }
      }
      
      
      
    /**
     * pintamos en pantalla una representación de un documento al cual tenemos  derecho de ver en
     * google drive :D
     * */
     
    this.printFile=function(document){
       
        
        var cad='<div class="col-lg-2 col-xs-4" style="height: 210px; width:154px; margin: 10px;">';
	        cad = cad + '<a class="drivefile" href="'+document.alternateLink+'" documentId="'+ document.id +'" target="_blank" title="'+ document.title +'">';
		    cad = cad + '<div class="box box-success" style="height: 210px; width:154px; padding-top: 2px;">';
		    cad = cad + '<div style="text-align:center;">';
		    cad = cad + '<img src="' + document.thumbnailLink + '"style="width:150px; height: 150px;"  />';
		    cad = cad + '<div style="width:100%; height:30px; font-size: 70%; overflow:hidden;"><label style="font-size: 100%; width: 100%; overflow: hidden;"> ' + document.title + '</div></label>';
		    cad = cad + '</div>';
		    cad = cad + '<div class="small-box-footer" style="text-align:center; display:none;">';
		    cad = cad + '<button class="btn btn-success btn-sm btn-flat" style="width:20px; height: 20px; font-size: 10px; padding:0px;"><i class="glyphicon glyphicon-share"></i></button>';
		    cad = cad + '<button class="btn btn-info btn-sm btn-flat"  style="width:20px; height: 20px; font-size: 10px; padding:0px;"><i class="glyphicon glyphicon-share"></i></button>';
		    cad = cad + '</div>';
		    cad = cad + '</div>';
	        cad = cad + '</a>';
	        cad = cad + '</div>';
	        $("#" + this.contentFilesId).prepend(cad);
       
        
    }
    
    
    
    /**
     * pintamos en pantalla una representación de un Folder al cual tenemos  derecho de ver en
     * google drive :D
     * */
     
    this.printFolder=function(object){
        
        
    }
    
    
    
    
}