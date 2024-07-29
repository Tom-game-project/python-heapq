
class priorityq:
    def __init__(self,data:list[int],last_index:int):
        self.data = data
        self.last_index = last_index

    def push(self,a:int):
        self.data.append(a)
        current_index = self.last_index
        while True:
            # if current_index % 2:
            #     # 新しく追加される要素を追加したあとのそのindexが奇数であった場合
            #     parent_index =(current_index - 1) // 2 
            # else:
            #     # 偶数であった場合
            #     parent_index =(current_index - 2) // 2 
            parent_index = (current_index - (1 if current_index % 2 else 2)) >> 1
            if self.data[parent_index] > a:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break

        self.last_index += 1

    def swap(self,index_a:int,index_b:int):
        self.data[index_b],self.data[index_a] = self.data[index_a],self.data[index_b]

    def pop(self):
        self.last_index -= 1

if __name__ == "__main__":
    pq=priorityq([1,3,6,4,8,7], 6)
    pq.push(5)
    print(pq.data)

    # pq=priorityq([], 0)
    # for i in [3,1,4,6,7,8]:
    #     pq.push(i)
    # print(pq.data)