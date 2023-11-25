import unittest

from main import get_combinations


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_works_for_6p():
        result = get_combinations(6, [1, 2, 5])

        result_list = list(result)
        print(result_list)
        assert [1, 1, 1, 1, 1, 1] in result_list
        assert [1, 1, 1, 1, 2] in result_list
        assert [1, 1, 2, 2] in result_list
        assert [2, 2, 2] in result_list
        assert [1, 5] in result_list
        assert len(result_list) == 5


if __name__ == '__main__':
    unittest.main()
