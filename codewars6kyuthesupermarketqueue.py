#https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
'''
The Supermarket Queue 6 kyu

There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.

output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12.  RM:  till1 is the 2, till2 is the 3.  till1 takes the 10 after the 2 and till2 finishes the 3 after the first minute of the 10.  till1 needs nine minutes to finish the 10.  10 + 2 = 12.

Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.

N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
'''
def queue_time(customers, n):
    pass

#https://stackoverflow.com/questions/64929435/supermarket-queue-programming-problem-from-codewars
#You can actually do this with 0 imports and 5 lines of code.  You create a list of available tills, iterate over customer checkout times, add to the first index and run sort on the list so the biggest int (Longest time in to checkout) is the last index.  Each iteration then adds the next checkout time to the first index as it is the next available till etc.  Then simply return the biggest number in the list.
def queue_time(customers: list[int], n: int) -> int:
    tills = [0] * n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)


print(queue_time([], 1)) #print 0
print(queue_time([5], 1)) #print 5
print(queue_time([2], 5)) #print 2
print(queue_time([1, 2, 3, 4, 5], 1)) #print 15
print(queue_time([1, 2, 3, 4, 5], 100)) #print 5
print(queue_time([2, 2, 3, 3, 4, 4], 2)) #print 9

#The above is fine for small number of queues and customers but slightly inefficient for larger pools, which is where heapq comes in. It avoids sorting the entire list of tills for each customer. It instead uses a heap to efficiently find and update the till with the shortest queue.
import heapq

def queue_time(customers: list[int], n: int) -> int:
    tills = [0] * n
    heapq.heapify(tills)
    for i in customers:
        smallest_till = heapq.heappop(tills)
        heapq.heappush(tills, smallest_till + i)
    return max(tills)


#One helpful thing is to use the collections.deque data structure from python standard library, which can be easily used as queue (or stack).
from collections import deque

def supermarket_queue(customers, n):
    queue = deque(customers)
    total_time = 0
    workers = [0 for _ in range(n)]
    while True:
        for i in range(n): # loop over self-checkouts
            if workers[i] == 0: # check for free self-checkout
                if queue:
                    workers[i] = queue.popleft()
            if workers[i] > 0: # checkout has work to do
                # reduce amount of work
                workers[i] -= 1
        # for live updates (i.e. debugging)
        print(f"t: {total_time}, checkouts: {workers}")
        # check for customers or busy self-checkouts
        if queue or any([w > 0 for w in workers]):
            # add one timestep
            total_time += 1
        else:
            # no customers waiting, no checkouts busy
            break
    return total_time

#https://www.reddit.com/r/learnpython/comments/u9elzo/spoiler_codewars_the_supermarket_queue_spoiler/
def queue_time(customers, n):
    time = 0
    while len(customers[:]) > 0:
        customers[:n] = [i - 1 for i in customers[:n]]
        customers = [i for i in customers if i != 0]
    time += 1
    return(time)

#YouTube video Codewars - The Supermarket Queue Challenge - Thread Pool Concept - Python Application [4KA5L_RSw8E]
def queue_time(customers, n):
    #No customers.  The total time is zero.
    if len(customers) == 0:
        return 0
    #More cashiers or equal cashiers available than customers.  The total time is the largest time in customers.
    if len(customers) <= n:
        time = max(customers)
        return time
    #More customers than cashiers available.  RM:  Look at Excel file Code Wars The Supermarket Queue 6 Kyu Customer Check Out Time Breakdown.xlsx as a simulation.
    if len(customers) > n:
        cashierqueues = [0] * n
        print(f"cashierqueues {cashierqueues}")
        print(f"customers {customers}")
        for j in customers:
            print(f"In for loop cashierqueues {cashierqueues}")
            cashierqueues.sort()
            print(f"In for loop cashierqueues after sort {cashierqueues}")
            print(f"In for loop j {j}")
            cashierqueues[0] = cashierqueues[0] + j #The lowest time is added with the next customer's time because the lowest time just finished the previous customer's time.
        print(f"Final cashierqueues all customers checked out {cashierqueues}")
        return max(cashierqueues)


print(queue_time([], 1)) #print 0
print(queue_time([5], 1)) #print 5
print(queue_time([2], 5)) #print 2
print(queue_time([1, 2, 3, 4, 5], 1)) #print 15
print(queue_time([1, 2, 3, 4, 5], 100)) #print 5
print(queue_time([2, 2, 3, 3, 4, 4], 2)) #print 9
print(queue_time([32, 5, 4, 30, 11, 7, 16, 29, 14, 29, 17], 6)) #print 40
'''
cashierqueues [0, 0, 0, 0, 0, 0]
customers [32, 5, 4, 30, 11, 7, 16, 29, 14, 29, 17]
In for loop cashierqueues [0, 0, 0, 0, 0, 0]
In for loop cashierqueues after sort [0, 0, 0, 0, 0, 0]
In for loop j 32
In for loop cashierqueues [32, 0, 0, 0, 0, 0]
In for loop cashierqueues after sort [0, 0, 0, 0, 0, 32]
In for loop j 5
In for loop cashierqueues [5, 0, 0, 0, 0, 32]
In for loop cashierqueues after sort [0, 0, 0, 0, 5, 32]
In for loop j 4
In for loop cashierqueues [4, 0, 0, 0, 5, 32]
In for loop cashierqueues after sort [0, 0, 0, 4, 5, 32]
In for loop j 30
In for loop cashierqueues [30, 0, 0, 4, 5, 32]
In for loop cashierqueues after sort [0, 0, 4, 5, 30, 32]
In for loop j 11
In for loop cashierqueues [11, 0, 4, 5, 30, 32]
In for loop cashierqueues after sort [0, 4, 5, 11, 30, 32]
In for loop j 7
In for loop cashierqueues [7, 4, 5, 11, 30, 32]
In for loop cashierqueues after sort [4, 5, 7, 11, 30, 32]
In for loop j 16
In for loop cashierqueues [20, 5, 7, 11, 30, 32]
In for loop cashierqueues after sort [5, 7, 11, 20, 30, 32]
In for loop j 29
In for loop cashierqueues [34, 7, 11, 20, 30, 32]
In for loop cashierqueues after sort [7, 11, 20, 30, 32, 34]
In for loop j 14
In for loop cashierqueues [21, 11, 20, 30, 32, 34]
In for loop cashierqueues after sort [11, 20, 21, 30, 32, 34]
In for loop j 29
In for loop cashierqueues [40, 20, 21, 30, 32, 34]
In for loop cashierqueues after sort [20, 21, 30, 32, 34, 40]
In for loop j 17
Final cashierqueues all customers checked out [37, 21, 30, 32, 34, 40]
40
'''


#My Python doesn't work
totaltimer = 0
totaltill = 2
tillnumberlist = ["till" + str(n) for n in range(1, totaltill + 1)]
print(tillnumberlist)
customerslist = [10, 2, 3, 3]
for eachtill in tillnumberlist:
    print(totaltimer)
    print(eachtill)
    totaltimer += 1
