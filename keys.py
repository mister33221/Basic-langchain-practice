keys = {}
with open("keys.txt", "r") as f:
    for line in f:
        key, value = line.strip().split("=")
        keys[key] = value

def get_key(key_name):
    return keys[key_name]