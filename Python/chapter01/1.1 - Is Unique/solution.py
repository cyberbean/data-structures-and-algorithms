from collections import defaultdict
import unittest

def naive_solution(input_string):
    if len(input_string) < 2:
        return True
    '''
    fast_index keeps place of the current char tested on its uniqueness
    slow index iterates through each char behind the fast_index char and checks if both the char
    at the slow_index and the fast_index match if they match then the string is not unique
    '''
    for fast_index in range (1, len(input_string)):
        for slow_index in range (0,fast_index) :
            if input_string[slow_index] == input_string[fast_index]:
                return False
    return True

'''
This function will insert each character from input_string into a hashmap, if the 
size of the hashmap is less than the size of the input_string return False
'''
def hashmap_solution(input_string):
    if len(input_string) < 2:
        return True
    hashmap = defaultdict(list)
    for char_from_list in input_string:
        hashmap[char_from_list].append(char_from_list)
    return True if len(hashmap) == len(input_string) else False


class TestUniqueStringSolutions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_naive_solution(self):
        self.assertEqual(True, naive_solution(''))
        self.assertEqual(True, naive_solution('0'))
        self.assertEqual(True, naive_solution('@algo_1234'))
        self.assertEqual(True, naive_solution('Example'))
        self.assertEqual(False, naive_solution('example'))
        self.assertEqual(False, naive_solution('aa'))
        self.assertEqual(False, naive_solution('exam__+#*$!3145ple'))
    
    def test_hashmap_solution(self):
        self.assertEqual(True, hashmap_solution(''))
        self.assertEqual(True, hashmap_solution('0'))
        self.assertEqual(True, hashmap_solution('@algo_1234'))
        self.assertEqual(True, hashmap_solution('Example'))
        self.assertEqual(False, hashmap_solution('example'))
        self.assertEqual(False, hashmap_solution('aa'))
        self.assertEqual(False, hashmap_solution('exam__+#*$!3145ple'))


if __name__ == '__main__':
    unittest.main()
