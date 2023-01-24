
from threading import Thread

def f1():
    for i in range(5):
        print(f"f1 - {i}")
 
def f2():
    for i in range(5):
        print(f"f2 - {i}")
 
def f3():
    for i in range(5):
        print(f"f3 - {i}")
       
def f4():
    for i in range(5):
        print(f"f4 - {i}")

fn1 = Thread(target=f1)
fn2 = Thread(target=f2)
fn3 = Thread(target=f3)
fn4 = Thread(target=f4)

fn1.start()
fn2.start()
fn3.start()
fn4.start()
fn1.join()
fn2.join()
fn3.join()
fn4.join()

