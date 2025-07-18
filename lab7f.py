#!/usr/bin/env python3
# Student ID: [seneca_id]

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

    def time_to_sec(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def change_time(self, seconds):
        time_seconds = self.time_to_sec() + seconds
        time_seconds %= 24 * 3600
        new_time = sec_to_time(time_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def sum_times(self, t2):
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        total_seconds %= 24 * 3600
        return sec_to_time(total_seconds)

    def __add__(self, t2):
        """Operator overloading for + to add two Time objects"""
        return self.sum_times(t2)

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
