# Standard Libraries
from typing import Set


class SumsCounter:
    @staticmethod
    def count(numbers: Set[int], min_sum: int, max_sum: int) -> int:
        unique_sums_count = 0

        for s in range(min_sum, max_sum + 1):
            # Tests whether there are two distinct numbers x and y such that x + y = S
            for x in numbers:
                y = s - x

                if y in numbers and x != y:
                    unique_sums_count += 1
                    break

        return unique_sums_count
