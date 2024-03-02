from dateutil import rrule
from datetime import datetime, timedelta

start = datetime.strptime("1/22/24", "%m/%d/%y")

ct = datetime.now()-start

series_as_object = list(
    rrule.rrule(
        rrule.DAILY,
        count=ct.days,
        dtstart=start,
        byweekday=[0,1,2,3,4]
    )
)

print(series_as_obj)

series_as_str = [ i.strftime('%m/%d/%y') for i in series_as_object]

print(series_as_str)
