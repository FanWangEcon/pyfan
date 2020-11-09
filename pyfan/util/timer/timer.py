"""
The :mod:`pyfan.util.timer.timer` generates various timer related strings.

Includes method :func:`getDateTime`.
"""

# import ProjectDisertCredit.Support.Timer import Timer
import time
import datetime as date


def curTimeDiff(startTime=None):
    if (startTime == None):
        return time.time()
    else:
        return (time.time() - startTime)


def getDateTime(timeType=6):

    if (timeType == 1):
        date_time = date.datetime.now().time()
    elif (timeType == 2):
        date_time = date.datetime.now()
    elif (timeType == 3):
        date_time = date.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    elif (timeType == 4):
        date_time = date.datetime.now().strftime('%Y-%m-%d %H:%M')
    elif (timeType == 5):
        date_time = date.datetime.now().strftime('%Y%m_%d_%H%M')
    elif (timeType == 6):
        date_time = date.datetime.now().strftime('%Y%m_%d')
    elif (timeType == 7):
        date_time = "{:%Y%m%d-%H%M%S-%f}".format(date.datetime.now())
    elif (timeType == 8):
        date_time = "{:%Y%m%d}".format(date.datetime.now())
    elif (timeType == 9):
        date_time = "{:%Y%m%d%H%M%S%f}".format(date.datetime.now())
    elif (timeType == 10):
        date_time = time.time()
    else:
        date_time = ''

    return date_time


class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print('[%s]' % self.name)
        print('Elapsed: %s' % (time.time() - self.tstart))


if __name__ == '__main__':
    with Timer('foo_stuff'):
        1 + 1
