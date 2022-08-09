import datetime
time=input(("enter time:"))
curr_time = datetime.datetime.now().time() # Current Time
print(curr_time) 
dt_obj = datetime.time(8,10,20)
print(dt_obj)
# dt_obj = datetime.datetime.strptime(time,"%H:%M:%S")
# print(dt_obj)
# Now Calculate the difference
diff = datetime.timedelta(hours=(dt_obj.hour - curr_time.hour), minutes=(dt_obj.minute - curr_time.minute), seconds=(dt_obj.second - curr_time.second))
print(diff)