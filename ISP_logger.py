# ISP logger

import speedtest
import datetime
import sqlite3


def get_current_date_and_time():
    date_and_time = datetime.datetime.now()
    return date_and_time.strftime("%Y-%m-%d %I:%M:%S %p")


if __name__ == "__main__":
    current_date_and_time = get_current_date_and_time()
    s_test = speedtest.Speedtest()
    d = s_test.download()
    u = s_test.upload()
    r = s_test.results.dict()
