import threading

def numbers():
    for i in range(5):
        print("Number",i)

def letters():
    for k in "ABCDE":
        print("Letter",k)

def squares(n):
    for x in range(10):
        print("square", n*n)

t1 = threading.Thread(target= numbers)
t2 = threading.Thread(target= letters)
t3 = threading.Thread(target= squares, args= (6,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()