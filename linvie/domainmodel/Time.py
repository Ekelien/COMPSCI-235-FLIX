import time


class TimeStamp(object):

    @staticmethod
    def current_time():
        time_tuple = time.localtime()
        return time.strftime("%d/%m/%Y", time_tuple)
