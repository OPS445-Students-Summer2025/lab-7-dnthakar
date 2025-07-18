#!/usr/bin/env python3
class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(t):
    return (t.hour * 60 + t.minute) * 60 + t.second

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t

def sum_times(t1, t2):
    total = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total)

def change_time(time, seconds):
    total = time_to_sec(time) + seconds
    new = sec_to_time(total)
    time.hour, time.minute, time.second = new.hour, new.minute, new.second

def valid_time(t):
    return not (t.hour < 0 or t.minute < 0 or t.second < 0 or 
                t.hour >= 24 or t.minute >= 60 or t.second >= 60)
