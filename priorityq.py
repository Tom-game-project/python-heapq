# Copyright 2021-2024 Tom-game-project

class priorityq:
    """
    class based heap queue algorithm
    """
    def __init__(self, data:list[int]):
        self.__data:list[int] = data
        self.last_index:int = len(self.__data) - 1

    @property
    def data(self):
        return self.__data

    def push(self, a:int):
        """
        push to heapq
        """
        self.__data.append(a)
        self.last_index += 1
        current_index = self.last_index
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if a < self.__data[parent_index]:
                self.__data[current_index] = self.__data[parent_index]
                current_index = parent_index
                continue
            break
        self.__data[current_index] = a

    def pop(self) -> int:
        """
        return minimum element of heapq and delete it
        """
        rvalue = self.__data.pop(0)
        if self.last_index == 0:
            return rvalue
        self.last_index -= 1
        newitem = self.__data.pop(self.last_index)
        self.__data.insert(0, newitem)

        current_index = 0
        current_item = self.__data[current_index]
        while (child_index := current_index * 2 + 1) <= self.last_index: # 子供のindexがリストの範囲内
            left_item = self.__data[child_index]
            child_index += 1
            if child_index > self.last_index:
                if left_item < current_item:
                    self.__data[current_index] = left_item
                    current_index = child_index - 1
                break

            right_item = self.__data[child_index]
            if right_item < current_item:
                if right_item < left_item:
                    self.__data[current_index] = right_item
                    current_index = child_index
                else:
                    self.__data[current_index] = left_item
                    current_index = child_index - 1
                continue
            elif left_item < current_item:
                self.__data[current_index] = left_item
                current_index = child_index - 1
                continue
            break
        self.__data[current_index] = newitem
        return rvalue
