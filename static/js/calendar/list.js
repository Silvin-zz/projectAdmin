var periodoInicio="";
var periodoFinal ="";
$(document).ready(function(){

evaluateActivity();
$("#totalhours").knob({ readOnly:true });



$("#activity").change(function(){
   evaluateActivity();
});


function evaluateActivity(){
    
     if($("#activity :selected").text() == "Proyecto"){
        $("#comboProject").fadeIn("slow");
    }
    else{
        $("#comboProject").fadeOut();
    }
}


var academicYearStartDate = new Date($("#startdate").val());

/* initialize the calendar
                 -----------------------------------------------------------------*/
                
                var date = new Date();
                var d = date.getDate(),
                        m = date.getMonth(),
                        y = date.getFullYear();

                $('#calendar').fullCalendar({
                    header: {
                        left: 'prev,next today',
                        center: 'title',
                        right: 'agendaWeek,agendaDay'
                    },
                    buttonText: {//This is to add icons to the visible buttons
                        prev: "<span class='fa fa-caret-left'></span>",
                        next: "<span class='fa fa-caret-right'></span>",
                        today: 'today',
                        week: 'week',
                        day: 'day'
                    },
                    firstDay: 1,
                    allDaySlot: false,
                    defaultView: 'agendaWeek',
                    minTime: "08:00:00",
                    selectable: true,
                    selectHelper: true,
                    //disableResizing: true,
                    //eventStartEditable: false,
                    //editable: false,
                    
                    
                    
                    viewDisplay: function (view) {
                        //========= Hide Next/ Prev Buttons based on academic year date range
                        if (view.start <= academicYearStartDate) {
                            $("#calendar .fc-button-prev").hide();
                            
                        }
                        else {
                            $("#calendar .fc-button-prev").show();
                        }
        
                    },
                   
					select: function(start, end) {
					   
					   var inicio   = start.getFullYear() + "-" + (start.getMonth() + 1) + "-" + start.getDate() + " " + start.getHours() + ":" + start.getMinutes() + ":00";
					   var fin      = end.getFullYear() + "-" + (end.getMonth() + 1) + "-" + end.getDate() + " " + end.getHours() + ":" + end.getMinutes() + ":00";
					   
					   
					    $("#remove").removeClass("disabled");
					    $("#saveChanges").removeClass("disabled");
					   
					   $('#activity option[value="545c5cc9ecd02405532ad402"]').attr('disabled', "disabled");
					   $('#activity option[value="54468267ecd024057614da6e"]').attr('selected', "selected");
 
					   $("#datestart").val(inicio);
					   $("#dateend").val(fin);
					   $("#action").val("new");
					   $("#myModal").modal("show");
					   evaluateActivity();
					   $("#remove").addClass("hide");
					   
					   
					   $("#title").val("");
					   $("#description").val("");
					   
					   
					},
					
					
					
					eventResize:function(event, jsEvent, ui, view){
					    
					    
					    
					    var start    = event.start;
					    var end      = event.end;
					    var inicio   = start.getFullYear() + "-" + (start.getMonth() + 1) + "-" + start.getDate() + " " + start.getHours() + ":" + start.getMinutes() + ":00";
					    var fin      = end.getFullYear() + "-" + (end.getMonth() + 1) + "-" + end.getDate() + " " + end.getHours() + ":" + end.getMinutes() + ":00";
					    $("#eventId").val(event.id);
					    $("#action").val("resize");
					    $("#datestart").val(inicio);
					    $("#dateend").val(fin);
					    $.ajax({  
                             url         : "/calendar/save",
                             type        : "POST",
                             data        : $("#form1").serialize(),
                             success : function(result){
                			    SPNotification("success", "Event", "Your Event has been Resized");
                                getTotalHours();
                             },
                             error:function(){
                                 
                                 
                             }
                        });
					    
					},
					
					
					eventDrop:function(event, jsEvent, ui, view){
					    
					    debugger;
					    
					    var start    = event.start;
					    var end      = event.end;
					    var inicio   = start.getFullYear() + "-" + (start.getMonth() + 1) + "-" + start.getDate() + " " + start.getHours() + ":" + start.getMinutes() + ":00";
					    var fin      = end.getFullYear() + "-" + (end.getMonth() + 1) + "-" + end.getDate() + " " + end.getHours() + ":" + end.getMinutes() + ":00";
					    $("#eventId").val(event.id);
					    $("#action").val("resize");
					    $("#datestart").val(inicio);
					    $("#dateend").val(fin);
					    $.ajax({  
                             url         : "/calendar/save",
                             type        : "POST",
                             data        : $("#form1").serialize(),
                             success : function(result){
                			    SPNotification("success", "Event", "Your Event has been Moved");
                                getTotalHours();
                             },
                             error:function(){
                                 
                                 
                             }
                        });
					    
					},
					
					eventClick:function( event, jsEvent, view){
					    
					    var start    = event.start;
					    var end      = event.end;
					    var inicio   = start.getFullYear() + "-" + (start.getMonth() + 1) + "-" + start.getDate() + " " + start.getHours() + ":" + start.getMinutes() + ":00";
					    var fin      = end.getFullYear() + "-" + (end.getMonth() + 1) + "-" + end.getDate() + " " + end.getHours() + ":" + end.getMinutes() + ":00";
					    
					    
					    
					    $("#remove").removeClass("disabled");
					    $("#saveChanges").removeClass("disabled");
					    
					    if(event.editable==false){
					        
					        $("#remove").addClass("disabled");
					        $("#saveChanges").addClass("disabled");
					        
					    }
					    
					    //if(event.activity == '545c5cc9ecd02405532ad402'){
					    
					     if(event.editable==false){
					       
                                $('#activity').attr("disabled", "disabled");
					    }
					    
					   $('#activity option[value="545c5cc9ecd02405532ad402"]').attr('disabled', "disabled");
					   $('#activity option[value="54468267ecd024057614da6e"]').attr('selected', "selected");
					    
					    $( "#activity option:selected" ).removeAttr("selected");
					    var option= $( '#activity option[value="' + event.activity + '"]' );
					    option.attr("selected", "selected");
					    
					    
					    debugger;
					    if(event.projectId !=null){  // ES un proyecto :D
					    
					        $( "#tmpproject option:selected" ).each(function(){
					           $(this).removeAttr("selected");
					        });
					        $( "#tmpproject option" ).each(function(){
					           if($(this).val() == event.projectId){
					               $(this).attr("selected","selected");
					           }
					        });
					        
					    }
					    
					    $("#eventId").val(event.id);
					    $("#action").val("update");
					    $("#datestart").val(inicio);
					    $("#dateend").val(fin);
					    $("#title").val(event.title);
					    $("#description").val(event.description);
					    $("#remove").removeClass("hide");
					    $("#myModal").modal("show");
					    evaluateActivity();
					},
					
					events: {
        				url: '/calendar/getAll',
        				error: function() {
        					$('#script-warning').show();
        				},
        				success:function(){
        				    
        				    periodoInicio   = new Date($('#calendar').fullCalendar('getView').start).toISOString().slice(0,10);
        				    periodoFinal    = new Date($('#calendar').fullCalendar('getView').end).toISOString().slice(0,10);
        				    
        				    getTotalHours();
        				}
        			},



                    editable: true,
                    //droppable: true, // this allows things to be dropped onto the calendar !!!
                    drop: function(date, allDay) { // this function is called when something is dropped

                        // retrieve the dropped element's stored Event Object
                        var originalEventObject = $(this).data('eventObject');

                        // we need to copy it, so that multiple events don't have a reference to the same object
                        var copiedEventObject = $.extend({}, originalEventObject);

                        // assign it the date that was reported
                        copiedEventObject.start = date;
                        copiedEventObject.allDay = allDay;
                        copiedEventObject.backgroundColor = $(this).css("background-color");
                        copiedEventObject.borderColor = $(this).css("border-color");

                        // render the event on the calendar
                        // the last `true` argument determines if the event "sticks" (http://arshaw.com/fullcalendar/docs/event_rendering/renderEvent/)
                        $('#calendar').fullCalendar('renderEvent', copiedEventObject, true);

                        // is the "remove after drop" checkbox checked?
                        if ($('#drop-remove').is(':checked')) {
                            // if so, remove the element from the "Draggable Events" list
                            $(this).remove();
                        }

                    },
                    eventRender: function(event, element){
                       
                        
                    }
                });


   
     
     
     $("#remove").click(function(){
         $("#myModal").modal("hide");
         $("#action").val("remove");
         eventId        = $("#eventId").val();
         
         $.ajax({  
             url         : "/calendar/save",
             type        : "POST",
             data        : $("#form1").serialize(),
             success : function(result){
                 
                $("#calendar").fullCalendar( 'removeEvents', eventId );
                SPNotification("success", "Event", "Your Event has been removed");
                getTotalHours();
                
             },
             error:function(){
                 
                 
             }
         });
     });
     
     
     
     
     $("#closeModal2").click(function(){
        $('#activity option[value="545c5cc9ecd02405532ad402"]').removeAttr('disabled');
        $('#activity').removeAttr("disabled");
        $('#activity option[value="54468267ecd024057614da6e"]').attr('selected', "selected"); 
         
     });
     
     $("#btnClose").click(function(){
          $('#activity option[value="545c5cc9ecd02405532ad402"]').removeAttr('disabled');
          $('#activity').removeAttr("disabled");
          $('#activity option[value="54468267ecd024057614da6e"]').attr('selected', "selected");
         
     });
     
     $("#saveChanges").click(function(){
         
         $('#activity option[value="545c5cc9ecd02405532ad402"]').removeAttr('disabled');
         $('#activity').removeAttr("disabled");
        $("#myModal").modal("hide");
        eventId     = $("#eventId").val();
        eventtype   = $("#action").val();
       
         $.ajax({  
             url         : "/calendar/save",
             type        : "POST",
             data        : $("#form1").serialize(),
             success : function(result){
                 getTotalHours();
                if(eventtype =="update"){
                    
                    $("#calendar").fullCalendar( 'removeEvents', eventId );
                    SPNotification("success", "Event", "Your Event was Modified");
                    
                    
                }
                else{
                    
                    SPNotification("success", "Event", "Your Event was Created");
                    
                }
				$('#calendar').fullCalendar('renderEvent', result[0], true); // stick? = true
				$('#calendar').fullCalendar('unselect');

             },
             error:function(){
                 
                 
             }
         });
         
    });       
    
    function getTotalHours(){
        
        $.ajax({  
             url         : "/calendar/getTotalHours",
             type        : "GET",
             data        :{"start": periodoInicio, "end": periodoFinal},
             success : function(result){
                 
                 
                 $('#totalhours')
                    .val(result[0].totalhours)
                    .trigger('change');

             },
             error:function(){
                 
                 
             }
         });
        
    }
    

});