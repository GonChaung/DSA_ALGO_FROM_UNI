from sys import stdin
# Read the sequence of operations to be operated on the hash table

operations = []
for line in stdin:
   line = line.split()
   if len(line) > 2:
       line[2] = int(line[2])
   operations.append(line)


table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    # return the hash value
    # return sum(ord(char) for char in s) % table_size
    total = 0
    for i in range(len(s)):
        char_value = ord(s[i])
        total += (37**i + char_value)
    return (total % table_size)

def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
    index = hash_func(s)
    if search(s) == -1:
        hash_table[index].append((s, v))
        return 0  # successful insertion
    else:
        return -1

def search(s):
    # return value of the key or
    # return -1 if s does not exist in hash table
    index = hash_func(s)
    for item in hash_table[index]:
        if item[0] == s:
            return item[1]  # return the value of the key
    return -1  # s does not exist in hash table

def delete(s):
    # return 0 on successful deletion
    # return -1 if s does not exist in hash table
    index = hash_func(s)
    for item in hash_table[index]:
        if item[0] == s:
            hash_table[index].remove(item)
            return 0
    return -1


# The main program to execute the sequence of operations
for op in operations:
    # op[0] is "insert" or "search" or "delete"
    if op[0] == "insert":
        insert(op[1], op[2])
        show_hash_table()
    elif op[0] == "search":
        result = search(op[1])
        print(result)
    elif op[0] == "delete":
        delete(op[1])
        show_hash_table()
