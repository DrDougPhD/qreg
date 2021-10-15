"""
The infimum (abbreviated inf; plural infima) of a subset S of a partially ordered set P
is a greatest element in P that is less than or equal to all elements of S,
if such an element exists.
"""
from numbers import Number
from typing import Any
from typing import List
from typing import Optional
from typing import Set


def of(subset: Set, from_superset: Set) -> Optional[Number]:
    smallest_of_subset = min(subset)
    values_from_superset_le_smallest = set(filter(
        lambda v: v <= smallest_of_subset,
        from_superset
    ))

    if len(values_from_superset_le_smallest) == 0:
        return None

    return max(values_from_superset_le_smallest)

if __name__ == '__main__':
    print(of({2, 3}, {0, 1, 2, 3}))
