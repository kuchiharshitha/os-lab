import threading
from threading import Semaphore

buffer, buffer_size = [], 5
empty, full, mutex = Semaphore(buffer_size), Semaphore(0), Semaphore(1)

def producer(value):
    empty.acquire()
    with mutex: buffer.append(value); print(f"Produced: {value} | Buffer: {buffer}")
    full.release()

def consumer():
    if full.acquire(blocking=False):
        with mutex: print(f"The consumed value is {buffer.pop(0)}")
        empty.release()
    else:
        print("Buffer is Empty")

while True:
    choice = input("1. Produce 2. Consume 3. Exit\nEnter your choice: ")
    if choice == "1": producer(int(input("Enter the value: ")))
    elif choice == "2": consumer()
    elif choice == "3": break
    else: print("Invalid choice, please enter 1, 2, or 3.")
