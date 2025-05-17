class HashTable:
    """
    A basic implementation of a hash table using chaining for collision handling.
    """

    def __init__(self, size=100):
        """
        Initializes the hash table with a given number of buckets.

        Args:
            size (int): The number of buckets. Default is 100.
        """
        self.size = size
        self.hash_table = self._create_buckets()

    def _create_buckets(self):
        """
        Creates empty buckets for the hash table.

        Returns:
            list: A list of empty lists (buckets).
        """
        return [[] for _ in range(self.size)]

    def __setitem__(self, key, val):
        """
        Adds or updates a key-value pair in the hash table.
        """
        h = hash(key) % self.size
        bucket = self.hash_table[h]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return

        bucket.append((key, val))

    def __getitem__(self, key):
        """
        Retrieves the value associated with a given key.
        Returns None if the key is not found.
        """
        h = hash(key) % self.size
        bucket = self.hash_table[h]

        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        return None

    def __delitem__(self, key):
        """
        Deletes a key-value pair from the hash table.
        Does nothing if the key is not found.
        """
        h = hash(key) % self.size
        bucket = self.hash_table[h]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket.pop(index)
                return

    def __str__(self):
        """
        Returns a readable string representation of the hash table.
        """
        return str(self.hash_table)


if __name__ == "__main__":
    # Initialize hash table
    ht = HashTable(size=20)

    # Insert key-value pairs
    ht["march 6"] = 102
    ht["march 10"] = 10
    ht["march 17"] = 1082

    # Display hash table
    print("Hash Table Contents:")
    print(ht)

    # Retrieve values
    print("\nRetrieve values:")
    print(f"march 10: {ht['march 10']}")
    print(f"march 17: {ht['march 17']}")
    print(f"march 6 : {ht['march 6']}")

    # Delete a key
    print("\n❌ Deleting 'march 10'...")
    del ht["march 10"]

    # Display updated table
    print("Hash Table After Deletion:")
    print(ht)

    # Try to retrieve deleted key
    print("\nTry to retrieve deleted key:")
    print(f"march 10: {ht['march 10']}")
