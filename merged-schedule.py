# To do this, you’ll need to know when any team is having a meeting.
# In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time).
# These integers represent the number of 30-minute blocks past 9:00am.

# (2, 3)  # Meeting from 10:00 – 10:30 am
# (6, 9)  # Meeting from 12:00 – 1:30 pm

#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] =>   [(0, 1), (3, 8), (9, 12)]

def merged_schedule(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = meetings[-1]

    return merged_meetings
