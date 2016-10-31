class Time:
    def number_of_subtime(days):
        raise NotImplementedError
    def number_of_subtime(days,hrs):
        raise NotImplementedError
    def number_of_subtime(days,hrs,mins):
        raise NotImplementedError
    def number_of_subtime(days,hrs,mins,sec):
        raise NotImplementedError
class Month(Time):
    def _init_():
        self.days=30
        self.hours=720
        self.mins=43200
        self.sec=2592000
    def number_of_subtime(days):
        
        return self.days
    def number_of_subtime(days,hrs):
        return [self.days,self.hours]
    def number_of_subtime(days,hrs,mins):
        return [self.days,self.hours,self.mins]
    def number_of_subtime(days,hrs,mins,sec):
        return [self.days,self.hours,self.mins,self.sec]
class Day(Time):
    def _init_():
        self.days=1
        self.hours=24
        self.mins=1440
        self.sec=86400
    def number_of_subtime(days):
        
        return self.days
    def number_of_subtime(days,hrs):
        return [self.days,self.hours]
    def number_of_subtime(days,hrs,mins):
        return [self.days,self.hours,self.mins]
    def number_of_subtime(days,hrs,mins,sec):
        return [self.days,self.hours,self.mins,self.sec]
class Hour(Time):
    def _init_():
        self.days=round((1/24),2)
        self.hours=1
        self.mins=60
        self.sec=3600
    def number_of_subtime(days):
        
        return self.days
    def number_of_subtime(days,hrs):
        return [self.days,self.hours]
    def number_of_subtime(days,hrs,mins):
        return [self.days,self.hours,self.mins]
    def number_of_subtime(days,hrs,mins,sec):
        return [self.days,self.hours,self.mins,self.sec]
class Minute(Time):
    def _init_():
        self.days=round((1/60)/24),2)
        self.hours=round((1/60),2)
        self.mins=1
        self.sec=60
    def number_of_subtime(days):
        
        return self.days
    def number_of_subtime(days,hrs):
        return [self.days,self.hours]
    def number_of_subtime(days,hrs,mins):
        return [self.days,self.hours,self.mins]
    def number_of_subtime(days,hrs,mins,sec):
        return [self.days,self.hours,self.mins,self.sec]
class Second(Time):
    def _init_():
        self.days=round((((1/60)/60)/60),2)
        self.hours=round(((1/60)/60),2)
        self.mins=round((1/60),2)
        self.sec=1
    def number_of_subtime(days):
        
        return self.days
    def number_of_subtime(days,hrs):
        return [self.days,self.hours]
    def number_of_subtime(days,hrs,mins):
        return [self.days,self.hours,self.mins]
    def number_of_subtime(days,hrs,mins,sec):
        return [self.days,self.hours,self.mins,self.sec]




        
