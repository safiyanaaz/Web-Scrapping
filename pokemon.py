import cv2
import numpy as np
import urllib.request
import threading
import math

def get_pokemon(start,end):
    for i in range(start,end):
        try:
            my_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/" + '{:03d}'.format(i) + ".png"
            # print(my_url)
            request = urllib.request.Request(my_url)
            response = urllib.request.urlopen(request)
            binary_str = response.read()
            byte_array = bytearray(binary_str)
            numpy_array = np.asarray(byte_array, dtype='uint8')
            image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
            cv2.imwrite("images/" + '{:04d}'.format(i) + ".png", image)
            print("Saved" + '{:04d}'.format(i) + ".png")
        except Exception as e:
            print(str(e))

thread_count=16      #Put your thread count here
image_count=800
thread_list=[]

#using multithreading to scrap 1000 of images faster in secs
'''
To create a new thread, we create an object of Thread class. It takes following arguments:
target: the function to be executed by thread
args: the arguments to be passed to the target function'''

for i in range(thread_count):
    start=math.floor(i*image_count/thread_count)+1
    end=math.floor((i+1)*image_count/thread_count)+1
    thread_list.append(threading.Thread(target=get_pokemon,args=(start,end)))


# starting thread 1-16

for thread in thread_list:
    thread.start()

# Once the threads start, the current program (you can think of it like a main thread) also keeps on executing.
# In order to stop execution of current program until a thread is complete, we use join method.As a result,
#  the current program will first wait for the completion of t1 and then t2. Once,
#  they are finished, the remaining statements of current program are executed.
for thread in thread_list:
    thread.join()

print("Done")


