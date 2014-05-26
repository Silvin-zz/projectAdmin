$(document).ready(function(){
	var folderId="root";

	getDriveList();
	breadcrumHandler();
	addBreadCrum("root", "ROOT");

	function getDriveList(){
		$.ajax({  
			url			: "/document/getList",
			type		: "POST",
			data		: $("#frmQuery").serialize(),
			success	: function(result){
				$("#driveList").html(result);
				folderHandler()
			}
		});
	}


	function CreateNewFolder(){
		$.ajax({  
			url			: "/document/newFolder",
			type		: "POST",
			data		: $("#frmNewFolder").serialize(),
			success	: function(result){
				$("#driveList").prepend(result);
				folderHandler();
			}
		});

	}

	$("#createFolder").click(function(){
		CreateNewFolder();
		$('#myModal').modal('hide');
	});

	function folderHandler(){
	
		$(".drivedocument").on("click",function(){
			var id 		=$(this).attr("documentId");
			var title 	=$(this).attr("title");
			setFolderId(id);
			getDriveList();
			addBreadCrum(id, title);
		});
		breadcrumHandler();
	}

	function setFolderId(newid){
		$("#folderId").attr("value",newid);
		$("#folderIdParent").attr("value",newid);

	}

	/** FUNCIONAMIENTO DE BREADCRUM ***********/
	function breadcrumHandler(){
		$(".breadlink").on("click",function(){
			var id=$(this).attr("data");
			setFolderId(id);
			getDriveList();
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

	function addBreadCrum(data, name){
		var html='<li><a href="#" class="breadlink" data="' + data + '"><strong>'+ name +'</strong></a></li>';
		$("#breadcrumb").append(html);

	}


});
