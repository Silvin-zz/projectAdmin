
/**
 * Clase para el manejo de google drive a travs de javacript e integración con el servidor para algunas peticiones :)
 * 
 **/

function DocumentClass(){
    this.breadcrumbId         = "breadcrumb";    //Id del div que sera el breadcrumb de la aplicacion de documentos :)
    this.formComunitationId   = "frmNewFolder";  //Id del formulario para comunicacion con el servidor para el caso de 
    this.fileObjectId         = "filePicker";    //Id del boton de tipo file para subir archivos
    this.contentFilesId       = "driveList";     //Contenedor visual donde estara la representación de carpetas y archivos
    this.token                = "";              //Token para comunicación con google drive
    this.rootFolderId         = "root";          //FolderId por default
    this.createFolderButtonId = "createFolder";  //id del Boton Guardar que esta en el modal para crear una carpeta :D
    this.formCreateFolderId   = "frmNewFolder";  //Id del formulario que se enviara al servidor para crear el nuevo directorio :D
    this.modalFolderId        = "myModal";
    this.breadcrumbRoot       = "Root";
    
    
    /* Variables para el caso de compartir documentos :) */
    
    this.shareFormId          ="frmShareDocument";
    this.shareItemId          = "shareItemId";
    this.shareRoleId          = "shareRole"
    
    
    this.init=function(){
        this.listenUpload();
        this.listenCreateFolder();
        this.addBreadCrumb(this.rootFolderId, this.breadcrumbRoot);
        this.breadcrumHandler();
    }
    
    
    this.listenCreateFolder=function(){
        var owner=this;
        $("#" + this.createFolderButtonId).click(function(){
		owner.CreateNewFolder();
		$('#' + owner.modalFolderId).modal('hide');
	});
        
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
        owner.printEmpty();
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
            'title'     : fileData.name,
            'mimeType'  : contentType,
            'parents'   :[{'id': owner.rootFolderId}]
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
              'params': {'uploadType': 'multipart'},
              'headers': {
                'Content-Type': 'multipart/mixed; boundary="' + boundary + '"'
              },
              'body': multipartRequestBody});
          if (!callback) {
            callback = function(file) {
              owner.printFile(file);  
              owner.shareItem(file.id);
              
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
	        this.removeEmpty();
	        $("#" + this.contentFilesId).prepend(cad);
       
        
    }
    
    
    
    /**
     * pintamos en pantalla una representación de un Folder al cual tenemos  derecho de ver en
     * google drive :D
     * */
     
    this.printFolder=function(object){
        
        
    }
    
    this.printEmpty=function(object){
        
        var cad='<div class="col-lg-2 col-xs-4 drivetmp" style="height: 210px; width:154px; margin: 10px; ">';
	        cad = cad + '<a class="drivefile" href="#" documentId="" target="_blank" title="">';
		    cad = cad + '<div class="box box-success" style="height: 210px; width:154px; padding-top: 2px;">';
		    cad = cad + '<div style="text-align:center;">';
		    cad = cad + '<img src="/static/theme/img/ajax-loader.gif" />';
		    cad = cad + '<div style="width:100%; height:30px; font-size: 70%; overflow:hidden;"><label style="font-size: 100%; width: 100%; overflow: hidden;"> </div></label>';
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
    
    this.removeEmpty=function(){
    
        $(".drivetmp:first").remove();
    }
    
    
    this.getDriveList   =function(){
        var owner=this;
	    $("#" + owner.contentFilesId ).html('<div class="alert alert-success col-xs-4">looking data .... </div>');
	    
		$.ajax({  
			url			: "/document/getList",
			type		: "POST",
			data		: $("#" + owner.formComunitationId).serialize(),
			success	: function(result){
				$("#" + owner.contentFilesId ).html(result);
				owner.folderHandler();
			}
		});
	}
	
	
	this.CreateNewFolder=function(){
	    var owner=this;
	    owner.printEmpty();
		$.ajax({  
			url			: "/document/newFolder",
			type		: "POST",
			data		: $("#" + owner.formCreateFolderId).serialize(),
			success	: function(result){
			    owner.removeEmpty();
				$("#" + owner.contentFilesId).prepend(result);
				owner.folderHandler();
			}
		});
	}
		
	this.folderHandler=function(){
	    var owner=this;
	    $(".drivedocument").on("click",function(){
			var id 		=$(this).attr("documentId");
			var title 	=$(this).attr("title");
			$("#" + owner.contentFilesId).empty();
			
			owner.setFolderId(id);
			owner.getDriveList();
			owner.addBreadCrumb(id, title);
		});
		//owner.breadcrumHandler();
	}
	
	this.setFolderId=function(newid){
	    var owner=this;
	    owner.rootFolderId=newid;
		$("#folderId").attr("value",newid);
		$("#folderIdParent").attr("value",newid);

	}
    
    
    this.addBreadCrumb=function(data, name){
        var owner=this;
		var html='<li><a href="#" class="breadlink" data="' + data + '"><strong>'+ name +'</strong></a></li>';
		$("#" + owner.breadcrumbId).append(html);

	}
	
	this.breadcrumHandler=function(){
	    var owner=this;
		$("#" + owner.breadcrumbId).on("click", ".breadlink",function(){
			var id=$(this).attr("data");
			owner.setFolderId(id);
			owner.getDriveList();
			var iniciado=false;
			$(".breadlink").each(function(){
				if($(this).attr("data")==id){
					iniciado=true;
				}
				else{
					if(iniciado==true){
						$(this).parent().remove();

					}
				}
			});
		});
	}
	
	
	this.shareItem=function(itemId){
	    
        $("#" +this.shareItemId).attr("value",itemId);
	    
	    $.ajax({  
			url			: "/document/share",
			type		: "POST",
			data		: $("#" + this.shareFormId).serialize(),
			success	: function(result){
			    
			}
		});
	    
	}
    
    
    
    
    
}