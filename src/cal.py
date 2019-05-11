"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Write a program that accepts user input of the form
#   `calendar.py month [year]`
# and does the following:
#  - If the user doesn't specify any input, your program should 
#    print the calendar for the current month. The 'datetime'
#    module may be helpful for this.

print('num of arguments:', len(sys.argv))
print( sys.argv[0] )

format_err = print("Month and year must be entered as integers in the following format: MM [YYYY]")

if len(sys.argv) == 1:
    m = datetime.now().month
    print(m)
    y = datetime.now().year

    # print(calendar.month(y, m))
    # print(calendar.month(y, m, w=3, l=3))

#  - If the user specifies one argument, assume they passed in a
#    month and render the calendar for that month of the current year.

elif len(sys.argv) == 2:
    m = int(sys.argv[1])
    y = sys.argv[2]
    print(calendar.month(y, m))

#  - If the user specifies two arguments, assume they passed in
#    both the month and the year. Render the calendar for that 
#    month and year.

elif len(sys.argv) == 3:
    m = int(sys.argv[1])
    y = int(sys.argv[2])
    print(calendar.month(y, m))

# - Otherwise, print a usage statement to the terminal indicating
#    the format that your program expects arguments to be given.
#    Then exit the program.

else:
    if len(sys.argv[2]) == 6:
        if sys.argv[1].isdigit() and sys.argv[2][1:5].isdigit():
            m = int(sys.argv[1])
            y = int(sys.argv[2][1:5])
        else:
            format_err
            exit()
    else:
        format_err
        exit()

