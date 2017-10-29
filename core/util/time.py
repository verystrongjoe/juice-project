import time
from datetime import date

# get unix time
def get_unix_time(yyyy, mm='', dd='') :

    if len(str(yyyy)) == 8 :
        mm = int(yyyy[4:6])
        dd = int(yyyy[6:8])
        yyyy = int(yyyy[0:4])

    d = date(yyyy,mm,dd)
    unixtime = time.mktime(d.timetuple())
    return int(unixtime)


# print(get_unix_time(2001, 1, 1))
# print(get_unix_time(2017, 1, 1))
# print(get_unix_time('20170101'))

