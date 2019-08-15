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
year = 366
annum = 1901



months = [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_key = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_key_leap = [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = {
    1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'
}

def get_day(date):
    if date < 7:
        return week[date % 7]
    elif date % 7 == 0: 
        return week[7]
    else: 
        return week[date % 7]

def cal_sundays(annum, year):
    date = 1
    idx = 1

    sundays = []
    for day_num in range(1, year+1):
        day = get_day(day_num)
        print('Date:', day, date, months[idx], annum )
        
        if year == 366:
            if date == months_key_leap[idx]:
                idx += 1
                date = 0  
                if day  == "Sunday" and date == 1:
                    sundays.append(day)
            date += 1
        else: 
            if date == months_key[idx]:
                idx += 1
                date = 0  
            date += 1
            # except:
            #     IndexError
            #     print('out of dates')
        
    return sundays

def days_in_year(leap):
    if leap == 'not leap':
        return 365
    return 366

# # Bool func for leap years
def is_leap(year):
    if year % 400 == 0:
        return 'is leap'
    if year % 100 == 0:
        return 'not leap'
    if year % 4 == 0:
        return 'is leap'
    return 'not leap'

def count_sundays():
    # years
    years = 3 #2001-1901

    for i in range(years, 0, -1):
        annum = 1905-i # 2001
        year = days_in_year(is_leap(annum))
        print( cal_sundays(annum, year) )

count_sundays()
