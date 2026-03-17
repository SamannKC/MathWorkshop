def uniqueList(li):
    unique = list(set(li))
    print(unique)

def prime(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return 0
        else:
            return 1


def twinPrime():
    for i in range(2, 1001):
        if prime(i) and prime(i+2):
            print(i, i+2)

def perfect(n):
    divisors = [x for x in range(1, int(n/2)+1) if n%x == 0]
    return sum(divisors)

def nextperfect():
    i = 7
    while True:
        if perfect(i) == i:
            print("next perfect is: ", i)
            break
        i+= 1

def mean_mode(li):
    mean = sum(li)/len(li)
    count = {x: 0 for x in set(li)}

    for item in li:
        if item in count:
            count[item] += 1

    mode = max(count.values())

    print(mean, mode)

def decimal_binary(n):
    binary = ""
    while n != 0:
        binary += str(n%2)
        n = n//2
    print(binary)

def proddigit(n):
    return sum(int(ch) for ch in str(n))

