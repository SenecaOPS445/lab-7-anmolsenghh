#!/usr/bin/env python3
# Student ID: [your_seneca_id]

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        total_sec = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_sec)

    def change_time(self, seconds):
        total_sec = self.time_to_sec() + seconds
        t = sec_to_time(total_sec)
        self.hour, self.minute, self.second = t.hour, t.minute, t.second
        return None

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
