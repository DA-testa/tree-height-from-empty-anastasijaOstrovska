#python3

import sys
import threading
import numpy as np

def compute_height(num, parents):
    height = np.zeros(num)

    max_height = -1
    for i in range (len(parents)):
        k = i
        heighti = 1
        while parents[k] != -1 :
            if height[k] != 0 :
                heighti += height[k] - 1
                break
            

            heighti += 1
            k = parents[k]
        height[i] = heighti
        max_height = max(max_height, height[i])
    
    return max_height


def main():
    i = input() # file or input
    if "i" in i.lower() :
        num = int(input())# number of elements
        string = input() # for string
        string = string.split()
        parents = np.array(string)
        parents = parents.astype(int)
        print(compute_height(num, parents))

    if "f" in i.lower() :
        name = input()
        name = "./test/" + name
        if "a" not in name:
            with open(name, mode = 'r' ,  encoding = "utf8") as fail:
                text = fail.readline()
                num = int(text)# nember of elements
                string = fail.readline()# for string
                string = string.split()
                parents = np.array(string)
                parents = parents.astype(int)
                print(compute_height(num, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

