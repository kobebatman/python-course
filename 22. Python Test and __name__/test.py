import unittest
import utility

# test method-уудыг агуулах class TestCase class-аас удамшина.
class TestUtility(unittest.TestCase):

	# test-ийн method-ийн нэр test_ - аар эхэлнэ.
    def test_add_1(self):
        num1 = 10
        num2 = '20'
        result = utility.add(num1, num2)

		# тэнцүү эсэхийг шалгах
        self.assertEqual(result, 30)

    def test_add_2(self):
        num1 = None
        num2 = 10
        result = utility.add(num1, num2)

		# илэрхийлэл True утгатай эсэхийг шалгах
        self.assertTrue(isinstance(result, TypeError))

# уг file-ыг шууд ажиллуулж байгаа бүх test method дуудагдаж ажиллана.
# уг file буюу module-ыг өөр нэг газар import хийж байгаа бол __name__ нь "__main__" биш "test" байх test method-ууд дуудагдаж ажиллахгүй.
if __name__ == '__main__':
    unittest.main()