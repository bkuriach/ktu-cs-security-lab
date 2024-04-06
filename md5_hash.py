import hashlib

def generate_md5_hash(input_string):
    md5_object = hashlib.md5(input_string.encode())
    return md5_object.hexdigest()

# Example usage
password = "Hello, world!"
md5_hash = generate_md5_hash(password)
print(f"The MD5 hash of '{password}' is: {md5_hash}")


