#### implement hash table

class HashTable:

    def __init__(self):
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def hash_Function(self,key):
        sum1 = 0
        for pos in range(len(key)):
            sum1 += ord(key[pos])

        return sum1 % self.size

    def put(self,key,value):
        index = self.hash_Function(key)

        #### check for collision
        while self.keys[index] is not None:
            # updating the value of the key
            if self.keys[index] == key:
                self.values[index] = value
                return

            # rehashing
            index= (index+1)%self.size

        self.keys[index] = key
        self.values[index] = value


    def get(self,key):
        index = self.hash_Function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index+1)%self.size

        return None


table = HashTable()
table.put("apple",24)
table.put("orange",34)
table.put("car",15)
table.put("nancy",50)

print(table.get("nancy"))



