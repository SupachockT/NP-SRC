from multiprocessing import Process
import os
import time

#defien function for process
def square_number():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

#create processes
for i in range(num_processes):
    p = Process(target=square_number) # ,args=()
    processes.append(p)

# start
for p in processes:
    p.start()

# join used to synchronize the execution of multiple processes. 
for p in processes:
    p.join()

print('end main')