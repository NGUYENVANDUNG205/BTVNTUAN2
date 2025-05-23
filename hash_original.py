
import hashlib

def hash_sha256(data):
    """Hàm băm SHA-256 nguyên bản"""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode())
    return sha256_hash.hexdigest()

def hash_sha512(data):
    """Hàm băm SHA-512 nguyên bản"""
    sha512_hash = hashlib.sha512()
    sha512_hash.update(data.encode())
    return sha512_hash.hexdigest()

if __name__ == "__main__":
    test_data = "Hello World!"
    print("Dữ liệu gốc:", test_data)
    print("\nSHA-256:", hash_sha256(test_data))
    print("\nSHA-512:", hash_sha512(test_data))
