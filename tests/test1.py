from python_heapq import priorityq

if __name__=="__main__":
    a = priorityq([])
    for i in [5,2,7,3,1,6,4]:
        a.push(i)
    print(
        a.data
    )