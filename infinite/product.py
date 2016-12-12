from .gencacher import GenCacher
import itertools

try: xrange
except NameError: xrange = range

def _summations(sumTo, n=2):
    """yields all the n-uples that sum to sumTo."""

    if n == 1:
        yield (sumTo,)

    else:
        for head in xrange(sumTo + 1):
            for tail in _summations(sumTo - head, n - 1):
                yield (head,) + tail

def product(*generators):
    """generate the cartesian product of infinite generators."""

    generators = list(map(GenCacher, generators))
    for distance in itertools.count(0):
        for idxs in _summations(distance, len(generators)):
            yield tuple(gen[idx] for gen, idx in zip(generators, idxs))
