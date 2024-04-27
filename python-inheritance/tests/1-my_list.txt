import unittest
import io
import sys

MyList = __import__("1-my_list").MyList


class TestMyList(unittest.TestCase):
    def test_print_sorted(self):
        # Redirect stdout to a string buffer
        captured_output = io.StringIO()
        sys.stdout = captured_output

        my_list = MyList([3, 1, 4, 1, -1])

        # Call the print_sorted method
        my_list.print_sorted()

        # Check if the output matches the expected sorted list
        expected_output = "[-1, 1, 1, 3, 4]\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Check that the original list is unchanged
        self.assertEqual([3, 1, 4, 1, -1], my_list)


if __name__ == "__main__":
    unittest.main()
