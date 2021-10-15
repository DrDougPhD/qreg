"""
Module implementation of an empirical distribution function given a collection of numeric observations.
"""

from numbers import Number
from typing import Callable
from typing import List
from typing import Union

import numpy
import pandas

from ..typehints import Matrix
from ..typehints import Vector


def of(random_variable: Matrix) -> Callable[[Vector], Number]:
    # For now, assume the random variable is a 1xM column vector, and not a NxM matrix.
    # TODO: come back and implement CDF in the multivariate case

    def edf(observation: Vector) -> Number:
        # For now, assume the observation is a single value, and not a Nx1 row vector.
        # TODO: come back and implement EDF in the multivariate case
        count_le = random_variable.le(observation[0], axis=0).sum()[random_variable.columns[0]]
        return count_le / random_variable.shape[0]

    return edf

