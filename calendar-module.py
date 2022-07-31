import calendar
from unicodedata import name
"""
A single line of input containing the space separated month, day and year, respectively, in    format."""

if __name__ == '__main__':
    
    date = input().split()
    
    
    print(calendar.day_name[calendar.weekday(int(date[2]),int(date[0]),int(date[1]))].upper())