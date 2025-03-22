#!/usr/bin/env python3

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(time):
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t

def sum_times(t1, t2):
    total_sec = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_sec)

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    total_sec = time_to_sec(time) + seconds
    new_time = sec_to_time(total_sec)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None

