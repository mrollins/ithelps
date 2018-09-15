import ithelps as ih


class TestSlide:
    data = [0, 1, 2, 3, 4, 5]

    def test_single(self):
        test = [list(x) for x in ih.slide(self.data, 1)]
        assert test == [[0], [1], [2], [3], [4], [5]]

    def test_evenly_divisible(self):
        test = [list(x) for x in ih.slide(self.data, 3)]
        assert test == [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]

    def test_unevenly_divisible(self):
        test = [list(x) for x in ih.slide(self.data, 4)]
        assert test == [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]

    def test_sequence_too_short(self):
        test = [list(x) for x in ih.slide(self.data, 7)]
        assert test == []
