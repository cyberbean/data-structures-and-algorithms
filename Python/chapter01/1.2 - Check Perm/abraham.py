import unittest
from collections import defaultdict

'''
This function will manually check that each character exists in both strings.
If the character is present in both strings then it gets popped off str2. This
will continue until we finish looping through str1.If str2 is empty that 
means each character was also in str1; therefore, a permutation
'''
def naive_is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    for char1 in str1:
        for char2_index in range (0,len(str2)):
            if str2[char2_index] == char1:
                str2 = str2[:char2_index] + str2[(char2_index+1):]
                break
    #if string is not empty then it is not a permutation
    if str2 != '':
        return False
    return True

'''
This function will sort the strings alphabetically. The reason for this is if the 
two strings are permutations of each other then once sorted they will be 
hashed identiaclly; therefore, the two hashmaps would equal each other.
'''
def hashmap_is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)

    hashmap1 = defaultdict(list)
    hashmap2 = defaultdict(list)

    for i in range (0, len(str1)):
        hashmap1[ord(str1[i])].append(str1[i])
        hashmap2[ord(str2[i])].append(str2[i])
    if hashmap1 != hashmap2:
        return False
    return True
    
    


class TestUniqueStringSolutions(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_naive_is_permutation(self):
        self.assertEqual(True, naive_is_permutation('ABC','ABC'))
        self.assertEqual(True, naive_is_permutation('b','b'))
        self.assertEqual(True, naive_is_permutation('ABC','CBA'))
        self.assertEqual(True, naive_is_permutation('T3+scx!l','xsc+3T!l'))
        self.assertEqual(True, naive_is_permutation('',''))

        self.assertEqual(False, naive_is_permutation('ABC','AB'))
        self.assertEqual(False, naive_is_permutation('ABC','CBD'))
        self.assertEqual(False, naive_is_permutation('ABC','abc'))
        self.assertEqual(False, naive_is_permutation('T3+scx!l','Xsc+3T!l'))
        self.assertEqual(False, naive_is_permutation('','}'))
    
    def test_hashmap_is_permutation(self):
        self.assertEqual(True, hashmap_is_permutation('ABC','ABC'))
        self.assertEqual(True, hashmap_is_permutation('b','b'))
        self.assertEqual(True, hashmap_is_permutation('ABC','CBA'))
        self.assertEqual(True, hashmap_is_permutation('T3+scx!l','xsc+3T!l'))
        self.assertEqual(True, hashmap_is_permutation('',''))

        self.assertEqual(False, hashmap_is_permutation('ABC','AB'))
        self.assertEqual(False, hashmap_is_permutation('ABC','CBD'))
        self.assertEqual(False, hashmap_is_permutation('ABC','abc'))
        self.assertEqual(False, hashmap_is_permutation('T3+scx!l','Xsc+3T!l'))
        self.assertEqual(False, hashmap_is_permutation('','}'))



if __name__ == '__main__':
    unittest.main()