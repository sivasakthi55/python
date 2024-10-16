"""import threading
import time

def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(2)

def  print_letters():
    for char in['a','b','c','d','e']:
        print(char)
        time.sleep(2)

threads1=threading.Thread(target=print_numbers)
threads2=threading.Thread(target=print_letters)

threads1.start()
threads2.start()


threads1.join()
threads2.join()

print("both threads hane finished.")
"""





import threading   
import time 
def cal_sqre(num): 
    for n in num: 
        print(' Square is : ', n * n)    
        time.sleep(1) 
  
def cal_cube(num):   
    for n in num:   
        print(" Cube is : ", n * n *n)  
        time.sleep(1)

arr = [4, 5, 6, 7, 2]
arr1 = [4, 5, 6, 7, 22]




threads1=threading.Thread(target=lambda:cal_sqre(arr))
threads2=threading.Thread(target=lambda:cal_cube(arr1))


threads1.start()
threads2.start()

threads1.join()
threads2.join()



  
