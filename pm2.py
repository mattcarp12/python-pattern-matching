
from typing import List


def sum1(x: List[int]):
    match x:
        case[]:
            return 0
        case[a, *b]:
            return a + sum1(b)