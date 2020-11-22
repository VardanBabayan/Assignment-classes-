class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self):
        self.store = [None for _ in range(16)]
    def get(self, key):
        index = hash(key) & 15
        if self.store[index] is None:
            return None
        n = self.store[index]
        while True:
            if n.key == key:
                return n.value
            else:
                if n.next:
                    n = n.next
                else:
                    return None
    def put(self, key, value):
        nd = Node(key, value)
        index = hash(key) & 15
        n = self.store[index]
        if n is None:
            self.store[index] = nd
        else:
            if n.key == key:
                n.value = value
            else:
                while n.next:
                    if n.key == key:
                        n.value = value
                        return
                    else:
                        n = n.next
                n.next = nd

hm = HashMap()
hm.put("1", "A")
hm.put("2", "B")
hm.put("3", "C")
hm.put("4", "D")
hm.put("5", "E")
hm.put("6", "F")
hm.put("7", "G")
hm.put("8", "H")
hm.put("9", "I")
hm.put("10", "J")
print(hm.get("1"))
print(hm.get("2"))
print(hm.get("3"))
print(hm.get("4"))
print(hm.get("5"))
print(hm.get("6"))
print(hm.get("7"))
print(hm.get("8"))
print(hm.get("9"))
print(hm.get("10"))
