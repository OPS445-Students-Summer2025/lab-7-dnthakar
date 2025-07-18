#!/usr/bin/env python3

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    s = Time(0,0,0)
    s.hour = t1.hour + t2.hour
    s.minute = t1.minute + t2.minute
    s.second = t1.second + t2.second
    if s.second >= 60:
        s.minute += s.second // 60
        s.second %= 60
    if s.minute >= 60:
        s.hour += s.minute // 60
        s.minute %= 60
    return s

def change_time(time, seconds):
    time.second += seconds
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def valid_time(t):
    return not (t.hour < 0 or t.minute < 0 or t.second < 0 or 
                t.hour >= 24 or t.minute >= 60 or t.second >= 60)
