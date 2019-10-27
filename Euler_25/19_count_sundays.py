import time

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

months = [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
week = { 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday',}

months_key = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_key_leap = [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day(date):
    """  Likely a lite version of Gauss' method to get a particular day based on date number. """ 
    if date < 7:
        return week[date % 7]
    elif date % 7 == 0: 
        return week[7]
    else: 
        return week[date % 7]

def cal_sundays(start, annum, year):
    """ Many off by one errors.  To overcome this, I change the 'start' to ensure the new loop starts where the old loop ended.  
    Hadn't heard of Gauss' algorithm.  'Annum' is to help keep track of the particular year but is of no consequence in this func. 
    'Year' creates the range of the loop. Using various dictionaries to get back week or month. """
    date = 1
    idx = 1

    sundays = []
    for day_num in range(start, year+start):
        day = get_day(day_num)
        print('Date', day_num, 'day:', day, date, months[idx], annum)
        if day == 'Sunday' and date == 1:
            sundays.append( [day_num, day, date, months[idx], annum] )
            
        if year == 366:
            try:
                if date == months_key_leap[idx]:
                    idx += 1
                    date = 0  
                date += 1
            except:
                IndexError
                continue
        else: 
            try:
                if date == months_key[idx]:
                    idx += 1
                    date = 0  
                date += 1
            except:
                IndexError
                continue
    
    # print(sundays)
    return len(sundays)

def days_in_year(leap):
    """ Gives back year.  Could be cominbed with 'is_leap' """ 
    if leap == 'not leap':
        return 365
    return 366

def is_leap(year):
    """ Bool func for leap years """ 
    if year % 400 == 0:
        return 'is leap'
    if year % 100 == 0:
        return 'not leap'
    if year % 4 == 0:
        return 'is leap'
    return 'not leap'

# off by one errors after every leap year...


def count_sundays():
    """main function.  loops through all years to check if a leap year and how many days in respective years 365 or 366"""
    start = 1
    # years
    years = 2001-1900 #2001-1900

    total_sums = 0

    for i in range(years, 0, -1):
        annum = 2001-i # 2001
        year = days_in_year(is_leap(annum))
        # print(annum, cal_sundays(start, annum, year)) 
        total_sums += cal_sundays(start, annum, year)
        print('\n')
        if year == 366:
            start += 1
        start += 1
        
    # subtract 2 for 1900
    print('total sundays', total_sums)
    

start = time.time()
count_sundays()
end = time.time()
print('Processed in ', end - start, 'seconds')