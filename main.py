import random
import time
import heapq
import copy

class priorityq:
    def __init__(self,data:list[int]):
        self.data:list = data
        self.last_index:int = len(self.data) - 1

    def push(self,a:int):
        self.data.append(a)
        self.last_index += 1
        current_index = self.last_index
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if a < self.data[parent_index]:
                self.data[current_index] = self.data[parent_index]
                current_index = parent_index
                continue
            break
        self.data[current_index] = a

    def pop(self):
        rvalue = self.data.pop(0)
        if self.last_index == 0:
            return rvalue
        self.last_index -= 1
        newitem = self.data.pop(self.last_index)
        self.data.insert(0, newitem)

        current_index = 0
        current_item = self.data[current_index]
        while (child_index := current_index * 2 + 1) <= self.last_index: # 子供のindexがリストの範囲内
            left_item = self.data[child_index]
            child_index += 1
            if child_index > self.last_index:
                if left_item < current_item:
                    self.data[current_index] = left_item
                    current_index = child_index - 1
                break

            right_item = self.data[child_index]
            if right_item < current_item:
                if right_item < left_item:
                    self.data[current_index] = right_item
                    current_index = child_index
                else:
                    self.data[current_index] = left_item
                    current_index = child_index - 1
            elif left_item < current_item:
                self.data[current_index] = left_item
                current_index = child_index - 1
            else:
                break
        self.data[current_index] = newitem
        return rvalue

def my_test(lst:list):
    print(lst[0:10])
    pq=priorityq([])
    for i in lst:
        pq.push(i)
    # print(pq.data)
    push_test(pq.data)
    pre_poped = -100
    iter100 = (i for i in sorted(lst))
    while pq.data:
        j = pq.pop()
        assert(j == next(iter100))
        push_test(pq.data)
        assert(j >= pre_poped)
        pre_poped = j
    
def py_test(lst:list):
    print(lst[0:10])
    pq=[]
    for i in lst:
        heapq.heappush(pq,i)
    # print(pq.data)
    push_test(pq)
    pre_poped = -100
    iter100 = (i for i in sorted(lst))
    while pq:
        j = heapq.heappop(pq)
        assert(j == next(iter100))
        push_test(pq)
        assert(j >= pre_poped)
        pre_poped = j

def push_test(lst:list):
    RED = '\033[31m'
    END = '\033[0m' 
    current_index = 0
    last_index = len(lst) - 1
    while True:
        # 長さを超えたら終わり
        if current_index > last_index:
            break
    
        child_index = current_index*2 + 1
        if child_index > last_index:
            current_index += 1
            continue
    
        if not (lst[current_index] <= lst[child_index]):
            print(RED + "heap structure is wrong" + END)
        
        child_index += 1
        if child_index > last_index:
            current_index += 1
            continue
    
        if not (lst[current_index] <= lst[child_index]):
            print(RED + "heap structure is wrong" + END)
        current_index += 1
    
if __name__ == "__main__":
    GREEN = '\033[92m'
    END = '\033[0m' 

    lst_lst:list[list[int]] = []
    for i in range(10):
        lst = list(range(10001))
        random.shuffle(lst)
        lst_lst.append(lst)
    lst_lst2 = copy.deepcopy(lst_lst)

    now = time.perf_counter()
    for i in lst_lst:
        my_test(i)
    print(GREEN + f"{time.perf_counter() - now} msec" + END)
    print(GREEN + "my random test (length 100) ---> Ok" + END)
    now = time.perf_counter()
    for i in lst_lst2:
        py_test(i)
    print(GREEN + f"{time.perf_counter() - now} msec" + END)
    print(GREEN + "py random test (length 100) ---> Ok" + END)