import time

start_time = time.time()

# outer loop
for o in range(100):
    # inner loop
    for i in range(1000):
        print(0, end=" ")
    print()

# time effect
print(round(time.time() - start_time, 2))
