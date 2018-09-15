import ithelps as ih


class TestMunch:
    data = [0, 1, 2, 3, 4, 5]

    def test_single(self):
        test = [list(x) for x in ih.munch(self.data, 1)]
        assert test == [[x] for x in self.data]

    def test_evenly_divisible(self):
        test = [list(x) for x in ih.munch(self.data, 2)]
        assert test == [[0, 1], [2, 3], [4, 5]]

    def test_unevenly_divisible(self):
        test = [list(x) for x in ih.munch(self.data, 4)]
        assert test == [[0, 1, 2, 3]]

    def test_sequence_too_short(self):
        test = [list(x) for x in ih.munch(self.data, 7)]
        assert test == []
