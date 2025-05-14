import time

# time can also be used to create a list of alarms

alarms = [0,0,0]
delays = [10,20,60]
start = time.time()
alarms[0] = start + delays[0]
alarms[1] = start + delays[1]
alarms[2] = start + delays[2]

while True:
    for i in range(0,3):
        now = time.time()
        if now > alarms[i]:
            print(f"alarm {i} {delays[i]} second alarm has been triggered because now ({round(now,3)}) > alarm {i} {round(alarms[i],3)}")
            alarms[i] = now + delays[i]
    time.sleep(1)
    print(f"time elapsed is {round(time.time() - start,3)}")
