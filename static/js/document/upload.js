var myapi=gapi;
var mytoken="";
$(document).ready(function(){
    

    getToken();
    
    
    
    
    function getToken(){
        alert("Iniciamos");
        $.ajax({  
			url			: "/document/getToken",
			type		: "POST",
			data		: $("#frmQuery").serialize(),
			success	: function(result){
			    alert(result);
			    mytoken=result;
			    debugger;
			}
		});
        
    }
    
    $("#filePicker").on("change",function(){
        
    });
    
    
    
    /**
       * Start the file upload.
       *
       * @param {Object} evt Arguments from the file selector.
       */
      

      /**
       * Insert new file.
       *
       * @param {File} fileData File object to read data from.
       * @param {Function} callback Function to call when the request is complete.
       */
      
    
});

var filePicker      = document.getElementById('filePicker');
filePicker.onchange = uploadFile;

function listItems(resp) {
    debugger;
 var result = resp.items;
 var i = 0;
 for (i = 0; i < result.length; i++) {
  console.log(result[i].title);
 }
}


    function setToken(){
        
        myapi.auth.setToken(mytoken);
        token=myapi.auth.getToken();
        debugger;
       
    }

function uploadFile(evt) {
    
    
        var request = gapi.client.request({
      'path': 'drive/v2/files',
      'method': 'GET',
      'access_type:' : 'offline',
      'params': {
       'maxResults': '10'
      }
     });
 request.execute(listItems);
        
        setToken();
        datos=myapi.auth.getToken();
        debugger;
        gapi.client.load('drive', 'v2', function() {
          var file = evt.target.files[0];
          insertFile(file);
        });
        //myapi.client.load('drive', 'v2', onDriveClientLoaded);
        
      }
      
function insertFile(fileData, callback) {
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

          var request = myapi.client.request({
              'path': '/upload/drive/v2/files',
              'method': 'POST',
              'params': {'uploadType': 'multipart'},
              'headers': {
                'Content-Type': 'multipart/mixed; boundary="' + boundary + '"'
              },
              'body': multipartRequestBody});
          if (!callback) {
            callback = function(file) {
              console.log(file)
            };
          }
          request.execute(callback);
        }
      }
      
      
      function onDriveClientLoaded() {
            retrieveFiles();
        }
  
function retrieveFiles() {
   var retrievePageOfFiles = function(request, result) {
     request.execute(function(resp) {
       result = result.concat(resp.items);
       var nextPageToken = resp.nextPageToken;
       if (nextPageToken) {
         request = myapi.client.drive.files.list({'pageToken': nextPageToken});
         retrievePageOfFiles(request, result);
       } else {
      console.log(result);
      console.log(resp);
       
       }
     });
   };
   var initialRequest = myapi.client.drive.files.list();
   retrievePageOfFiles(initialRequest, []);
}