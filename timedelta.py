import datetime
time = datetime.time()
print(str(time))
time_string = str(time).split(":")
print("Time String is",time_string)
joined_time = ":".join(time_string)
print("JOined Time is,type is",joined_time,type(joined_time))
# time_object = (datetime.time)joined_time
date_time_obj = datetime.datetime.strptime(joined_time, '%H:%M:%S')
print(date_time_obj)
