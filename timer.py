import datetime

def get_time():
    return datetime.datetime.now()

time1 = get_time()
time2 = get_time()

passed_time = str(round(datetime.timedelta.total_seconds(time2 - time1)))

