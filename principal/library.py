import datetime


class Library:
    def getPeriodWeek(self):
        
        decrease    = datetime.datetime.today().weekday()
        if(decrease > 0):
            decrease= decrease * -1
        add         = 6-datetime.datetime.today().weekday()
        today       = datetime.datetime.now().date()
        enddate     = today + datetime.timedelta(days=add)
        startdate   = today + datetime.timedelta(days=decrease)
    
    
        return {"start": startdate, "end": enddate}
        
    
    
    def getPeriodMonth(self):
        
        decrease    = int(datetime.datetime.today().day) -1
        if(decrease > 0):
            decrease= decrease * -1
        
        today       = datetime.datetime.now().date()
        startdate   = today + datetime.timedelta(days=decrease)
        month       = startdate.month +1
        year        = startdate.year
        
        if(month > 12):
            year    = year +1 
            month   = 1
        
        enddate     = datetime.date(year, month, 1) - datetime.timedelta(1)
    
    
        return {"start": startdate, "end": enddate}
        
        
    def getPeriodWeekToBack(self, weekNumber):
        
        decrease    = datetime.datetime.today().weekday()
        if(decrease > 0):
            decrease= decrease * -1
        decrease   = decrease + ((weekNumber * 7) *-1)
        
    
        add         = 6-datetime.datetime.today().weekday()
        today       = datetime.datetime.now().date()
        enddate     = today + datetime.timedelta(days=add)
        startdate   = today + datetime.timedelta(days=decrease)
        return {"start": startdate, "end": enddate}
    