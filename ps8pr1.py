#
# ps8pr1.py  (Problem Set 8, Problem 1)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def days_in_month(self):
        """ Returns the number of days in the called object's month
        """
        numdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            numdays[2] = 29
            
        return numdays[self.month]    

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def day_name(self):
        """ Return the day of the week that the called Date object falls on. 
            IMPORTANT: This method won't work until you implement the 
            other methods of the class, as specified in Problem 1.
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
        monday = Date(11, 20, 2023)
        num_days = self.days_between(monday)
        return day_names[num_days % 7]
    
    #### Put your code for the methods from Problem 1 below. ####
    #### Make sure that it is indented by an appropriate amount. ####

# problem 3
    def advance_one(self):
        """ changes the called object so that it represents one calendar 
        day after the date that it originally represented 
        """
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month <= 11:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
    
# problem 4
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) 
        represent the same calendar date 
        """
        if self.day == other.day:
            if self.month == other.month:
                if self.year == other.year:
                    return True
        else:
            return False
        
# problem 5
    def is_before(self, other):
        """ returns True if the called object represents a calendar date that 
        occurs before the calendar date that is represented by other. If self 
        and other represent the same day, or if self occurs after other, the 
        method should return False 
        """
        if self.__eq__(other) == True:
            return False
        elif self.year > other.year:
            return False
        elif self.year < other.year:
            return True
        else:  #when both have the same year
            if self.month > other.month:
                return False
            elif self.month < other.month:
                return True
            else: #when both have same month and year
                if self.day >= other.day:
                    return False
                else:
                    return True
            
# problem 6
    def is_after(self, other):
        """ returns True if the called object (self) represents a calendar 
        date that occurs after the calendar date that is represented by other. 
        If self and other represent the same day, or if self occurs before 
        other, the method should return False 
        """
        if self.__eq__(other) == True:
            return False
        elif self.is_before(other) == False:
            return True
        else:
            return False
        
# problem 7
    def days_between(self, other):
        """ returns an integer that represents the number of days between 
        self and other """
        newself = self.copy()
        newother = other.copy()
        count = 0
        if self.is_before(other):
            while newself != newother:
                count -= 1
                newself.advance_one()
        elif self.is_after(other):
            while newself != newother:
                count += 1
                newother.advance_one()
        else:
            count = 0
        return count
    
            
                
            
    
    
    
    
    