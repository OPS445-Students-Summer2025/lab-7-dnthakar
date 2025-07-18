#!/usr/bin/env python3
# Student ID: 154195226

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        # Returns a formatted string "HH:MM:SS"
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def sum_times(self, other):
        # Sum two Time objects and return a new Time object
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return Time.sec_to_time(total_seconds)

    def change_time(self, seconds):
        # Change time by a given number of seconds
        total_seconds = self.time_to_sec() + seconds
        new_time = Time.sec_to_time(total_seconds)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second

    def valid_time(self):
        # Returns True if time is valid else False
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def time_to_sec(self):
        # Convert current time to total seconds
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def sec_to_time(seconds):
        # Convert seconds to Time object, handle wrap around 24 hours
        seconds = seconds % (24 * 3600)
        h = seconds // 3600
        seconds %= 3600
        m = seconds // 60
        s = seconds % 60
        return Time(h, m, s)

    def __str__(self):
        # String representation to print object easily
        return self.format_time()


# Standalone function to sum two Time objects (used by lab7a1.py)
def sum_times(t1, t2):
    total_seconds = t1.time_to_sec() + t2.time_to_sec()
    return Time.sec_to_time(total_seconds)


# Standalone function to format Time object as string (used by lab7a1.py)
def format_time(t):
    return t.format_time()
