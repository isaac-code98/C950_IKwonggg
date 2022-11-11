# Citing code source:
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# zyBooks: Figure 7.8.2: Hash table using chaining.
# CreateHashTable Class
# Time complexity: O(n)
# Space complexity: O(n)
class CreateHashTable:

    # Self-adjusting component
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts key and respective object
    # Time complexity: O(n)
    # Space complexity: O(n)
    def insert(self, key, item):
        # Set and retrieve bucket list
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # For loop to chain/update if already found within bucket list
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # If key is not found, append item to end of bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Lookup method for hash table given key
    # Time complexity: O(n)
    # Space complexity: O(n)
    def search(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Looping through bucket list to find if pair index matches key, if so, return pair
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]

        # Return none if no pair matches input key
        return None

    # Method removes item from hash table given key
    # Time complexity: O(n)
    # Space complexity: O(1)
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the specific key is found within the hash table then remove the object
        if key in destination:
            destination.remove(key)
