
MONTH_NAMES = {    0: "January",
                   1: "February",
                   2: "March",
                   3: "April",
                   4: "May",
                   5: "June",
                   6: "July",
                   7: "Auggy-Doggy",
                   8: "September",
                   9: "October",
                   10: "November",
                   11: "December"  }
                   
DAYS_OF_WEEK = {    0 : "Sunday",
                    1 : "Monday",
                    2 : "Tuesday",
                    3 : "Wednesday",
                    4 : "Thursday",
                    5 : "Friday",
                    6 : "Saturday"  }

DAYS_IN_MONTH = {  0: 31,
                   1: 28,
                   2: 31,
                   3: 30,
                   4: 31,
                   5: 30,
                   6: 31,
                   7: 31,
                   8: 30,
                   9: 31,
                   10: 30,
                   11: 31  }

class Date(object):
    def __init__(self, weekDay, day, month, year):
        self.weekDay = weekDay # should be int from 0 to 6
        self.day = day # should be int from 1 to 31
        self.month = month # should be int from 0 to 11
        self.year = year
        
    def __str__(self):
        dayName = DAYS_OF_WEEK[self.weekDay]
        monthName = MONTH_NAMES[self.month]
        return "The date is: {:>9}, {:>11} {:2d}, {:4d}".format(dayName, monthName, self.day, self.year)

    def nextDay(self):
        # Always iterate weekday
        wkdays = range(7)
        self.weekDay = wkdays[(self.weekDay + 1) % len(wkdays)]
        
        if self.day == DAYS_IN_MONTH[self.month]:
            if self.year % 4 == 0 and self.month == 1:
                if (not self.year % 100 == 0) or (self.year % 400 == 0):
                    self.day += 1
                else:
                    self.day = 1
            else:
                self.day = 1
        elif self.month == 1 and self.day == 29:
            self.day = 1
        else:
            self.day += 1
            
        months = range(12)
        if self.day == 1:
            self.month = months[ (self.month + 1) % len(months) ]
            
        if self.day == 1 and self.month == 0:
            self.year += 1
    
    
def testStates():
    #Test Week Day iteration
    test = Date(0,1,0,0) #Sunday January 1st 0000
    for i in range(8):
        test.nextDay()
        assert(test.weekDay == (i+1) % 7)
    
    # Test year iteration
    test = Date(0,31,11,1999)
    test.nextDay()
    assert(test.year == 2000)
    
    # Test day iteration
    test = Date(0,1,0,0000)
    for i in range(31):
        test.nextDay()
    assert(test.day == 1)
    
    # Test Leap year 29th day bullshit
    test = Date (0,28,1,4)
    test.nextDay()
    assert(test.day == 29 and test.month == 1)
    
    # Test that february iterates properly on 29th day
    test.nextDay()
    assert(test.day == 1 and test.month == 2)
    
    #Test that no leap day on century not divisible by 400
    test = Date(0,28,1,1400)
    test.nextDay()
    assert(test.day == 1 and  test.month == 2)
    
    # Test that there is a leap day on a century divisible by 400
    test = Date(0,28,1,1600)
    test.nextDay()
    assert(test.day == 29 and test.month == 1)


try: 
    testStates()

except:
    "Failed Tests!"
    quit()

# Figure out what day of the week Jan 1st 1901 was
# given that jan 1st 1900 was Monday.

first = Date(1,1,0,1900)
print first.year

while first.day != 1 or first.month != 0 or first.year != 1901:
    first.nextDay()

Start_weekday = first.weekDay

# Now count the sundays on first of month until Dec 31 2000

TODAY = Date(Start_weekday,1,0,1901)
count = 0
while TODAY.day != 31 or TODAY.month != 11 or TODAY.year != 2000:
    if TODAY.weekDay == 0 and TODAY.day == 1:
        count += 1
    
    TODAY.nextDay()

print TODAY
print "Count is : {}".format(count)