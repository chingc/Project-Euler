class EulerPyramid:
    def __init__(self, value):
        """Start building a pyramid using the given value as the root."""
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        self.paths = [[value]]
        self.pyramid = [[value]]

    def get_pyramid(self):
        """The pyramid as a list of lists."""
        return self.pyramid[:]

    def get_highest_path(self, index=None):
        """Highest path, or highest from root to the specified leaf index."""
        if index is None:
            totals = list(map(sum, self.paths))
            index = totals.index(max(totals))
        return self.paths[index][:]

    def add_level(self, values):
        """Add a new level to the pyramid using the given list of values."""
        if len(values) <= len(self.paths):
            raise ValueError("Not enough values in given level")
        if not all(map(lambda x: isinstance(x, int), values)):
            raise ValueError("All values must be integer")
        new_paths = []
        for i, path in enumerate(self.paths):
            left = path + [values[i]]
            right = path + [values[i + 1]]
            new_paths = self._prune(new_paths, [left, right])
        self.paths = new_paths
        self.pyramid.append(values[:])

    @staticmethod
    def build_pyramid(infile):
        """Build a pyramid by reading it from a file."""
        with open(infile, "r") as pyramid:
            for i, level in enumerate(pyramid):
                values = list(map(int, level.split()))
                try:
                    if i == 0:
                        if len(values) > 1:
                            raise SyntaxError("Too many values")
                        p = EulerPyramid(values[0])
                    else:
                        p.add_level(values)
                except Exception as error:
                    print("Input error on line {}: {}".format(i + 1, error))
                    p = None
                    break
        return p

    def _prune(self, current, additions):
        """Discard clashing lesser paths."""
        if len(current) < 2:
            return additions
        if sum(current[-1]) < sum(additions[0]):
            return current[:-1] + additions
        return current + additions[1:]
