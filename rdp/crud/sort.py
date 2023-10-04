from abc import ABC, abstractmethod
from typing import List

class Sort(ABC):
    @abstractmethod
    def sort(values: List) -> List:
        pass

class sort_small(Sort):
    def sort(values: List) -> List:
        return sorted(return_values, key=lambda x: x.value)

class sort_big(Sort):
    def sort(values: List) -> List:
        return sorted(return_values, key=lambda x: x.value, reverse=True)

sort_dic = {
    "small": sort_small,
    "big": sort_big
}
