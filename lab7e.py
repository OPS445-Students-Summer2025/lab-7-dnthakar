#!/usr/bin/env python3
# Student ID: [154195226]

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times
    """
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return time in 'HH:MM:SS' format"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return time in 'HH.MM.SS' format"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time in 'HH:MM:SS' format"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert time object to total seconds from midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def change_time(self, seconds):
        """Modify time by adding 'seconds' (positive or negative)"""
        time_seconds = self.time_to_sec() + seconds
        # wrap around 24 hours if needed
        time_seconds %= 24 * 3600
        new_time = sec_to_time(time_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def sum_times(self, t2):
        """Add two Time objects and return a new Time object"""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        total_seconds %= 24 * 3600  # wrap around 24 hours if needed
        return sec_to_time(total_seconds)

def sec_to_time(seconds):
    """Convert seconds to Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
