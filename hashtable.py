'''
hashtable:
take list of strings as arg
hash the string and assign an index
'''

class hashtable:
    strings = []
    index = [[] for _ in range(20)]

    def __init__(self, string_list):
        strings = string_list
        for x in strings:
            self.add(x)

    #create hash value from string
    def hash(string):
        for x in string:
            hash_val += x
        hash_val * 31

    #find index from hash value
    def find_index(self, string):
        index = hash(string) % len(self.index)
        return index

    #add string to index
    def add(self, string):
        location = self.find_index(string)
        self.index[location].append(string)

    def includes(self, string):
        location = self.find_index(string)
        if string in self.index[location]:
            return True
        else:
            return False

    def list(self):
        ret_list = []
        for x in self.index:
            for i in x:
                ret_list.append(i)
        return ret_list

ht = hashtable(["this", "is", "a", "bunch", "of", "words"])

print(ht.list())
