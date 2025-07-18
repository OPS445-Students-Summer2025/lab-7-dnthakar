#!/usr/bin/env python3

from lab7a import Time

def sec_to_time(seconds):
    return Time.sec_to_time(seconds)

# Create two time objects
time1 = Time(10, 45, 15)
time2 = Time(2, 20, 50)

# Print initial times
print("Time 1:", time1.format_time())  # 10:45:15
print("Time 2:", time2.format_time())  # 02:20:50

# Sum of times
time3 = time1.sum_times(time2)
print("Time 1 + Time 2 =", time3.format_time())  # expected output: 13:06:05

# Change time1 by adding 5000 seconds
time1.change_time(5000)
print("Time 1 after adding 5000 seconds:", time1.format_time())

# Check validity of a valid and an invalid time
print("Is Time 2 valid?", time2.valid_time())  # Should return True

invalid_time = Time(25, 70, 61)
print("Is invalid_time valid?", invalid_time.valid_time())  # Should return False
