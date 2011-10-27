# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

import datetime
import re

def unwrap_datetime(obj):
    """ Return an obj with datetime_-key split into date_-and time_-keys. """
    result = {}
    for k, v in obj.items():
        if k.startswith('datetime_') and isinstance(v, datetime.datetime):
            result.update({
                re.sub('^datetime', 'date', k): v.date(),
                re.sub('^datetime', 'time', k): v.time(),

            })
        elif k.startswith('datetime_') and v is None:
            result.update({
                re.sub('^datetime', 'date', k): None,
                re.sub('^datetime', 'time', k): None,

            })
    
        else:
            result.update({k: v})
    return result


def wrap_datetime(obj):
    """ Return an obj with datetime_-key split into date_-and time_-keys. """
    result = obj.copy()
    key_pairs = [(dk,
                  re.sub('date_', 'time_', dk),
                  re.sub('date_', 'datetime_', dk))
                 for dk in result if dk.startswith('date_')]
    for dk, tk, dtk in key_pairs:
        if (tk in result and
            isinstance(result[dk], datetime.date) and
            isinstance(result[tk], datetime.time)):
            result.update({
                dtk: datetime.datetime(year=result[dk].year,
                                       month=result[dk].month,
                                       day=result[dk].day,
                                       hour=result[tk].hour,
                                       minute=result[tk].minute,
                                       second=result[tk].second,
                                       microsecond=result[tk].microsecond),
            })
            del(result[dk])
            del(result[tk])
        elif tk in result and result[tk] is None and result[dk] is None:
            result.update({dtk: None})
            del(result[dk])
            del(result[tk])
    return result
