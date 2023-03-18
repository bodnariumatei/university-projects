import unittest

from utils.sortings import selection_sort, shake_sort


class TestCaseSortings(unittest.TestCase):
    def setUp(self) -> None:
        self.__list1 = []
        self.__list2 = [43, 56, 22, 91, 4, 23]
        self.__list3 = ['abc', 'aads', 'eeras', 'a']

    def test_selection_sort(self):
        self.assertTrue(selection_sort(self.__list1) == [])
        self.assertEqual(selection_sort(self.__list2), [4, 22, 23, 43, 56, 91])
        self.assertEqual(selection_sort(self.__list2, reversed=True), [91, 56, 43, 23, 22, 4])
        self.assertEqual(selection_sort(self.__list3), ['a', 'aads', 'abc', 'eeras'])
        self.assertEqual(selection_sort(self.__list3, key=len), ['a', 'abc', 'aads', 'eeras'])

    def test_shake_sort(self):
        self.assertTrue(shake_sort(self.__list1) == [])
        self.assertEqual(shake_sort(self.__list2), [4, 22, 23, 43, 56, 91])
        self.assertEqual(shake_sort(self.__list2, reversed=True), [91, 56, 43, 23, 22, 4])
        self.assertEqual(shake_sort(self.__list3), ['a', 'aads', 'abc', 'eeras'])
        self.assertEqual(shake_sort(self.__list3, key=len), ['a', 'abc', 'aads', 'eeras'])
