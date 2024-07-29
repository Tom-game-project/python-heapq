import random

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
                # self.swap(current_index, parent_index)
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
        self.data.insert(0, self.data.pop(self.last_index))

        current_index = 0
        while True:
            child_index = 2 * current_index + 1
            if child_index > self.last_index:
                break
            left_item = self.data[child_index]
            child_index += 1
            if child_index > self.last_index:
                if left_item < self.data[current_index]:
                    self.swap(child_index - 1, current_index)
                break
            right_item = self.data[child_index]
            if right_item < self.data[current_index]:
                if right_item < left_item:
                    self.swap(child_index, current_index)
                    current_index = child_index
                else:
                    # left_item がright_itemよりも小さい
                    self.swap(child_index - 1, current_index)
                    current_index = child_index - 1
            elif left_item < self.data[current_index]:
                self.swap(child_index - 1, current_index)
                current_index = child_index - 1
            else:
                break
        return rvalue

    def swap(self,index_a:int,index_b:int):
        self.data[index_b], self.data[index_a] = self.data[index_a], self.data[index_b]

def test():
    a = [i for i in range(100)]
    random.shuffle(a)
    pq=priorityq([])
    for i in a:
        pq.push(i)
    # print(pq.data)
    push_test(pq.data)
    pre_poped = -100
    iter100 = (i for i in range(100))
    while len(pq.data) != 0:
        j = pq.pop()
        assert(j== next(iter100))
        push_test(pq.data)
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
    # pq=priorityq([1,3,6,4,8,7])
    # pq.push(5)
    # # pq.push(0)
    
    # print(pq.last_index, pq.data)
    # print("poped",pq.pop())
    # print(pq.last_index, pq.data)


    # pq=priorityq([], 0)
    # for i in [3,1,4,6,7,8]:
    #     pq.push(i)
    # print(pq.data)
    # pq.push(2)
    # print(pq.last_index,pq.data)
    for i in range(1000):
        test()
    print(GREEN + "random test (length 100) ---> Ok" + END)