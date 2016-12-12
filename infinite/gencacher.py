class GenCacher:
    """Cache the generator values to permit random accesses."""

    def __init__(self, generator):
        self._g = generator
        self._cache = []

    def __getitem__(self, idx):
        while len(self._cache) <= idx:
            self._cache.append(next(self._g))
        return self._cache[idx]
