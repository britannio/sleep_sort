import threading
import time
import random

time_dilation = 0.1

unsortedList = random.sample(range(0, 10), 5)
sortedList = []

class myThread (threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        time.sleep(self.number * time_dilation)
        sortedList.append(self.number)
        print(self.number)



print('Original list: ' + str(unsortedList))

largestNumber = 0

for item in unsortedList:
    thread = myThread(item)
    thread.start()
    if item > largestNumber:
        largestNumber = item

time.sleep(largestNumber * time_dilation)
print('Sorted list: ' + str(unsortedList))


