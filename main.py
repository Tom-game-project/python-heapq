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
            parent_index = (current_index - (2 if current_index % 2 == 0 else 1)) // 2
            # print("current_index",current_index,
            #       "parent_index", parent_index,
            #       "self.data[parent_index]",self.data[parent_index] ,
            #       "data that ttempt to add ",a ,
            #       "up ?",self.data[parent_index] > a,
            #       sep="\n")
            if self.data[parent_index] > a:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break
        # self.last_index += 1

    def pop(self):
        rvalue = self.data.pop(0)
        if self.last_index == 0:
            return rvalue
        self.last_index -= 1
        self.data.insert(0, self.data.pop(self.last_index))
    
        current_index = 0
        while True:
            if (child_index := 2*current_index + 1) > self.last_index:
                break
            if self.data[child_index] < self.data[current_index]:
                self.swap(child_index,current_index)
            else:
                child_index += 1
                if child_index > self.last_index:
                    break
                if self.data[child_index] > self.data[current_index]:
                    self.swap(child_index,current_index)
            current_index = child_index
        return rvalue

    def swap(self,index_a:int,index_b:int):
        self.data[index_b], self.data[index_a] = self.data[index_a], self.data[index_b]

def test():
    RED = '\033[31m'
    END = '\033[0m' 
    a = [i for i in range(100)]
    random.shuffle(a)
    pq=priorityq([])
    for i in a:
        pq.push(i)
    print(pq.data)
    # print(pq.last_index, pq.data)
    # print("poped",pq.pop())
    # print(pq.last_index, pq.data)
    current_index = 0

    while True:
        # 長さを超えたら終わり
        if current_index > pq.last_index:
            break

        child_index = current_index*2 + 1
        if child_index > pq.last_index:
            current_index += 1
            continue

        if not (pq.data[current_index] <= pq.data[child_index]):
            print(RED + "push test failed" + END)
        
        child_index += 1
        if child_index > pq.last_index:
            current_index += 1
            continue

        if not (pq.data[current_index] <= pq.data[child_index]):
            print(RED + "push test failed" + END)
        current_index += 1

    pre_poped = -100
    while len(pq.data) != 0:
        j = pq.pop()
        print(j)
        assert(j >= pre_poped)
        pre_poped = j



if __name__ == "__main__":
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
    test()