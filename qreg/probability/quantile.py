"""
TODO:
* Memoize the edfs so that they are computed in ascending order, not recomputed every time.
"""

from numbers import Number
from typing import Callable

import pandas

from . import cdf
from ..typehints import Matrix
from ..typehints import Vector


def of(random_variable: Matrix) -> Callable[[Number], Number]:
    F_X = cdf.of(random_variable=random_variable)
    quantile_thresholds = random_variable.apply(F_X, axis='columns')

    def quantile(tau: Number) -> Number:
        # TODO: we can stop computing the quantiles of the occurrences
        # once we reach tau.
        # No... gotta sort the random variable first,
        # and then once tau exceeded, return the associated value.
        rvs_above_tau = random_variable[quantile_thresholds >= tau]
        return rvs_above_tau.min()[random_variable.columns[0]]

    return quantile
