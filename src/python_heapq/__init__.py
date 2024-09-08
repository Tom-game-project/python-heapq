# Copyright 2021-2024 Tom-game-project

class priorityq:
    """
    class based heap queue algorithm
    """
    def __init__(self, data:list[int]):
        self.__data:list[int] = data

    def __getitem__(self,key:int) -> int:
        return self.data[key]

    def __len__(self) -> int:
        return len(self.data)

    @property
    def data(self):
        return self.__data

    def push(self, a:int):
        """
        push to heapq
        """
        self.__data.append(a)
        current_index = len(self) - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if a < self[parent_index]:
                self.__data[current_index] = self[parent_index]
                current_index = parent_index
                continue
            break
        self.__data[current_index] = a

    def pop(self) -> int:
        """
        return minimum element of heapq and delete it
        """
        rvalue = self.__data.pop(0)
        if not self.__data:
            return rvalue
        last_index = len(self) - 1
        newitem = self.__data.pop(last_index)
        self.__data.insert(0, newitem)

        self.__data[self.__pop_proc(last_index)] = newitem
        return rvalue
    
    def __pop_proc(self,last_index:int) -> int:
        current_index = 0
        current_item = self[current_index]

        while (child_index := current_index * 2 + 1) <= last_index:
            left_item = self[child_index]
            if last_index <= child_index:
                if left_item < current_item:
                    self.__data[current_index] = left_item
                    current_index = child_index 
                break
            child_index += 1
            right_item = self[child_index]
            if right_item < current_item and right_item < left_item:
                self.__data[current_index] = right_item
                current_index = child_index
                continue
            elif right_item < current_item or left_item < current_item:
                self.__data[current_index] = left_item
                current_index = child_index - 1
                continue
            break
        return current_index
    
