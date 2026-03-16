import time

# O(1): direct formula
def constant_time(n):
    return n * (n + 1) // 2

# O(n): simple loop
def linear_time(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

# Timing helper (milliseconds)
def time_it(func, n, label):
    start = time.time()
    result = func(n)
    end = time.time()
    elapsed = (end - start) * 1000  # convert seconds → ms
    print(f"{label}: result={result}, time={elapsed:.3f} ms")

# Run demo
n = 10
print(f"Testing with n = {n}\n")

time_it(constant_time, n, "O(1) Constant")
time_it(linear_time, n, "O(n) Linear")

# Try larger n to see difference
n = 1_000_000
print(f"\nTesting with n = {n}\n")

time_it(constant_time, n, "O(1) Constant")
time_it(linear_time, n, "O(n) Linear")
