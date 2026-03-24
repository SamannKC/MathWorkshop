import matplotlib.pyplot as plt
from matplotlib.patches import Circle , Ellipse
import numpy as np
import math
import random

def run_task():
    #RUNNING
    Exercise12()

def task1():
    x_cord = np.array([1, 50])
    y_cord = np.array([3, 40])
    plt.xlim(0,50)
    plt.xlim(0,50)

    plt.grid()
    plt.plot(x_cord, y_cord)
    plt.show()

def task2():
    days = np.array([1,2,3,4,5])
    Enfield = np.array([50,40,70, 80, 20])
    Honda = np.array([80,20,20,50,60])
    Yamaha = np.array([70,20,60,40,60])
    Ktm = np.array([40,20,30,70,60])
    
    plt.plot(days, Enfield)
    plt.plot(days, Honda)
    plt.plot(days, Yamaha)
    plt.plot(days, Ktm)

    plt.xlabel("Days")
    plt.ylabel("Distance Covered")
    plt.title("Bike Details in plot ")

    plt.legend()

    plt.show()

def TrigPlot():
    x, y = [], []

    start = -4 * math.pi
    end = 4 * math.pi
    step = 0.1

    i = start
    while i <= end:
        x.append(i)
        y.append(math.sin(i))
        i += step

    plt.plot(x,y, color = "red", label = "sin function")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

def Exercise4():
    x = [i for i in range(10)]
    y = x

    plt.plot(x,y)
    plt.title("Y=X Graph")

    plt.show()

def Exercise5():
    x = [1,2,6,8]
    y = [3,8,1,10]

    plt.plot(x,y)

    plt.show()

def Exercise6():
    x = sorted([random.randint(1,20) for _ in range(20)])

    f1 = lambda x: 5*x**3 + 2*x - 1
    f2 = lambda x: -2*x**3 + x**2 + 100
    f3 = lambda x: 2*np.pi*x + 20

    y1 = [f1(i) for i in x]
    y2 = [f2(i) for i in x]
    y3 = [f3(i) for i in x]

    plt.plot(x, y1, marker= 'o',label="function 1", linestyle='None')
    plt.plot(x, y2, marker= 'o', label="function 2", linestyle='None')
    plt.plot(x, y3, marker= 'o', label="function 3", linestyle='None')

    plt.legend()

    plt.show()

def Exercise7():
    x = sorted([random.randint(1,20) for _ in range(20)])

    f1 = lambda x: 5*x**3 + 2*x - 1
    f2 = lambda x: -2*x**3 + x**2 + 100
    f3 = lambda x: 2*np.pi*x + 20

    y1 = [f1(i) for i in x]
    y2 = [f2(i) for i in x]
    y3 = [f3(i) for i in x]

    fig, axes = plt.subplots(1,3, figsize=(15,5))

    axes[0].plot(x, y1, marker= 'o')
    axes[0].set_title("Function 1")

    axes[1].plot(x, y2, marker='o')
    axes[1].set_title("Function 2")

    axes[2].plot(x, y3, marker='o')
    axes[2].set_title("Function 3")

    plt.show()


def Exercise8():
    days = np.array([1,2,3,4,5])
    Enfield = np.array([50,40,70, 80, 20])
    Honda = np.array([80,20,20,50,60])
    Yamaha = np.array([70,20,60,40,60])
    Ktm = np.array([40,20,30,70,60])

    bikes = [Enfield, Honda, Yamaha, Ktm]

    fig, axes = plt.subplots(2,2)
    axes = axes.flatten()

    for axis, bike in zip(axes, bikes):
        axis.plot(days, bike)
        axis.set_xlabel("days")
        axis.set_ylabel("Distance Covered")

    plt.show()

def Exercise9():
    x, y = [], []

    start = -3 * math.pi
    end = 3 * math.pi
    step = 0.1

    i = start
    while i <= end:
        x.append(i)
        y.append(math.cos(i))
        i += step

    plt.plot(x,y, color = "red", label = "sin function")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

def Exercise10_11():
    Center = (2,2)
    r = 4

    fig, ax = plt.subplots()

    circle = Circle((2, 2), radius=r, color='skyblue', edgecolor='blue', linewidth=2)

    ellipse = Ellipse(Center, 4, 10, angle = 90, edgecolor = 'r', facecolor = 'none', lw = 2)

    ax.add_patch(circle)
    ax.add_patch(ellipse)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')

    plt.grid(True, linestyle='--')

    plt.show()

def Exercise12():
    p , q , a = 4 , 2, 0.1

    x = [i for i in range(-20, 25)]
    y = []
    for val in x:
        y_val = 4*a*(val - q)**2 + p
        y.append(y_val)

    plt.plot(x, y)
    plt.show()

run_task()
