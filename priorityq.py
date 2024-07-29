
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
                continue
            elif left_item < current_item:
                self.data[current_index] = left_item
                current_index = child_index - 1
                continue
            break
        self.data[current_index] = newitem
        return rvalue
