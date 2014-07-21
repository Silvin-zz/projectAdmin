$(document).ready(function(){




/* initialize the calendar
                 -----------------------------------------------------------------*/
                //Date for the calendar events (dummy data)
                var date = new Date();
                var d = date.getDate(),
                        m = date.getMonth(),
                        y = date.getFullYear();

                $('#calendar').fullCalendar({
                    header: {
                        left: 'prev,next today',
                        center: 'title',
                        right: 'month,agendaWeek,agendaDay'
                    },
                    buttonText: {//This is to add icons to the visible buttons
                        prev: "<span class='fa fa-caret-left'></span>",
                        next: "<span class='fa fa-caret-right'></span>",
                        today: 'today',
                        month: 'month',
                        week: 'week',
                        day: 'day'
                    },
                    firstDay: 1,
                    allDaySlot: false,
                    defaultView: 'agendaWeek',
                    minTime: "08:00:00",
                    selectable: true,
                    selectHelper: true,
                   
					select: function(start, end) {
					   
					   var inicio   = start.getFullYear() + "-" + (start.getMonth() + 1) + "-" + start.getDate() + " " + start.getHours() + ":" + start.getMinutes() + ":00";
					   var fin      = end.getFullYear() + "-" + (end.getMonth() + 1) + "-" + end.getDate() + " " + end.getHours() + ":" + end.getMinutes() + ":00";
					   
					    
					   $("#datestart").val(inicio);
					   $("#dateend").val(fin);
					   $("#action").val("new");
					   $("#myModal").modal("show");
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
					    $("#eventId").val(event.id);
					    $("#action").val("update");
					    $("#datestart").val(inicio);
					    $("#dateend").val(fin);
					    $("#title").val(event.title);
					    $("#description").val(event.description);
					    $("#remove").removeClass("hide");
					    $("#myModal").modal("show");
					},
					
					events: {
        				url: '/calendar/getAll',
        				error: function() {
        					$('#script-warning').show();
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

                    }
                });


    
    
   
    
    

    function createEvent(event){
        
        
    }
    
    function updateEvent(event){
        
        
    }
    
    function deleteEvent(eventId){
        
        
    }
     
     
     $("#saveChanges").click(function(){
        
        $("#myModal").modal("hide");
         $.ajax({  
             url         : "/calendar/save",
             type        : "POST",
             data        : $("#form1").serialize(),
             success : function(result){
				$('#calendar').fullCalendar('renderEvent', result[0], true); // stick? = true

             },
             error:function(){
                 
                 
             }
         });
         
    });           

});