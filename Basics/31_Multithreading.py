# Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from API's
# threading.Thread(targer= , args=())

print("#################### Multithreading #####################")
import time
import threading
def walk_the_dog(first):
    time.sleep(10)
    print(f"You finish walking {first}")
def take_out_trash():
    time.sleep(4)
    print("You take out the trash")
def take_mail():
    time.sleep(2)
    print("You take tha mail")

chore1 = threading.Thread(target=walk_the_dog, args=("Scooby",))
chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=take_mail)
chore3.start()

chore1.join() # To wait until thread terminates
chore2.join() # To wait until thread terminates
chore3.join() # To wait until thread terminates
print("All chores are finished")
print("#########################################################")
