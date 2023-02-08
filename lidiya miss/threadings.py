# from time import sleep
# def task():
#     # block for a moment
#     sleep(3)
#     # display a message
#     print("this is from another thread")
# # task()
#
# from threading import Thread
# # creating a thread
# thread = Thread(target = task)
# # next, we can create an instance of the threading .thread class and specify
# #  our function name as the "target" argument in the constructor .
# # run the thread
# thread.start()
#
# # the start() function does not block ,meaning it returns immediately.
# task()

# def task(sleep_time,message):
#       #block for a moment
#       sleep(sleep_time)
#       print(mssage)
#
# #create a thread
# thread = Thread(target = task,args=(1.5,'new messaage from another thread')
# # run the thread
# thread.start()
# # wait for the thread to finish
# print('waiting for the thread...')
# thread.join()
# task()

import time
import threading

def cal_sqre(num):
    print("calculate the square root of the given number")
        for n in num:
             time.sleep(0.3)
             print("square is: ", n * n)
def cal_cube(num):
    print("calculate the cube of given number")
    for n in num:
        time.sleep(0.3)
        print("the cube is:",n*n*n)
arr = [4,5,6,7,2]#given array or list

t1 = time.time()
#cal_sqre(arr)
#cal_cube(arr)
th1 = threading.Thread(target=cal_sqre, args=(arr,))
th2  = threading.Thread(target=cal_cube, args=(arr, ))
th1.start()
th2.start()
th1.join()
th2.join()
print(" Total time taaken by threads is :",time.time() - t1) #print the total time




















