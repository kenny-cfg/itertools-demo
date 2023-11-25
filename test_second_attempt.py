import unittest

from second_attempt import get_combinations


class TestSecondAttempt(unittest.TestCase):
    def test_works_for_single_coin(self):
        result = get_combinations(5, [1])

        result_list = list(result)
        print(result_list)
        assert [1, 1, 1, 1, 1] in result_list
        self.assertEqual(len(result_list), 1)

    def test_works_for_6p(self):
        result = get_combinations(6, [1, 2, 5])

        result_list = list(result)

        assert [1, 1, 1, 1, 1, 1] in result_list
        assert [1, 1, 1, 1, 2] in result_list
        assert [1, 1, 2, 2] in result_list
        assert [2, 2, 2] in result_list
        assert [1, 5] in result_list
        self.assertEqual(len(result_list), 5)


if __name__ == '__main__':
    unittest.main()
