def hash_function(key_str, size):
    return sum([ord(c) for c in key_str]) % size

if __name__ == "__main__":
    test_inputs = ["a", "caleb", "test", "more than a feeling"]

    hash_func = lambda key: hash_function(key, 10)
    print(map(hash_func, test_inputs))

    hash_func = lambda key: hash_function(key, 4)
    print(map(hash_func, test_inputs))
