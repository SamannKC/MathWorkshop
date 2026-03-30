import matplotlib.pyplot as plt 
import random

def runTask():
    """Use this to run task"""
    # Example : Task1()


def task1():
    x = [random.randint(1,50) for _ in range(10)]
    y = [random.randint(1,50) for _ in range(10)]
    colors = ["red", "green", "blue", "yellow", "pink", "orange", "purple", "brown", "cyan", "magenta"]

    plt.scatter(x,y, c=colors)
    plt.show()

def task2():
    years = [year for year in range(2017, 2023)]
    population = [[8,150,80], [54,77,54], [93, 32, 100], [116, 11, 73], [137, 6,93], [184, 1, 72]]
    groups = ['Bears', 'Dolphins', 'Whales']

    _, axes = plt.subplots(2,3)

    axes = axes.flatten()

    for i in range(len(population)):
        axes[i].pie(population[i], labels = groups)
        axes[i].set_title(f"Year: {years[i]}")

    plt.show()

def task3():
    data = {
            'Mango':45,
            'Orange':30,
            'Plum':15,
            'Pineapple': 30,
            'Melon': 30
            }

    plt.pie(list(data.values()), labels = list(data.keys()))
    plt.show()


def task4():
    colors = ['Red', 'Silver', 'Blue', 'White', 'Green']
    seen = [123, 230, 78, 193, 12]

    # plt.bar(colors, seen, width=0.3)
    # plt.barh(colors, seen)
    # plt.bar(colors, seen , color = colors)
    plt.pie(seen, labels = colors)
    plt.show()

runTask()
