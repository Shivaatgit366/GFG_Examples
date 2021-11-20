# write a program to get the date and time. Use "datetime" module only, don't use pytz, time modules.
# solution:-

# method1:- using "datetime" module, now() function to get the time.
# from datetime import datetime

# now_method_time = datetime.now()
# print(now_method_time)  # now() gives both date and time of that moment.

# current_time = now_method_time.strftime("%H:%M:%S")  # strftime() is used to create a string for containing time.
# print(f"the current time is {current_time}")
# ---------------------------------------------------------------------------------------------------------------

# method2:- using "datetime" module, now() function with time() and date() function.
# remember:- there is no functions like day(), month(), year(), hour() functions. Use only time() and date() functions.
# from datetime import datetime

# current_time = datetime.now().time()  # strftime() gives only the time in string format. It won't give date in string.
# date_today = datetime.now().date()  # strftime() does not give date in string format.

# print(f"time is {current_time} and the date is {date_today}")
# ----------------------------------------------------------------------------------------------------------------

# method3:- create an object using now() function, then call the attributes of that object one by one.
# remember:- there are only time() and date() functions. There is no day(), year(), month(), minute() functions.

# import datetime

# date_time_object = datetime.datetime.now()  # from module "datetime", import "datetime" class.
# print(f"the day is {date_time_object.day}")
# print(f"the year is {date_time_object.year}")
# print(f"the month is {date_time_object.month}")
# print(f"the hour is {date_time_object.hour}")
# print(f"the minute is {date_time_object.minute}")
# print(f"the microsecond is {date_time_object.microsecond}")
# --------------------------------------------------------------------------------------------------------------
