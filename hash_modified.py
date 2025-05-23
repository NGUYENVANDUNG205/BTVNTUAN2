
import hashlib
import base64
import os

def modified_sha256(data, salt=None):
    """Hàm băm SHA-256 có sửa đổi với salt"""
    if salt is None:
        salt = os.urandom(16)  # Tạo salt ngẫu nhiên 16 bytes
    
    # Kết hợp dữ liệu với salt
    salted_data = salt + data.encode()
    
    # Tạo hash
    sha256_hash = hashlib.sha256()
    sha256_hash.update(salted_data)
    
    # Trả về cả salt và hash được mã hóa base64
    return base64.b64encode(salt).decode() + ':' + base64.b64encode(sha256_hash.digest()).decode()

def modified_sha512(data, rounds=10000):
    """Hàm băm SHA-512 có sửa đổi với nhiều vòng lặp"""
    # Thêm prefix và suffix
    prefix = "secure_"
    suffix = "_hash"
    modified_data = prefix + data + suffix
    
    # Thực hiện nhiều vòng băm
    result = modified_data
    for _ in range(rounds):
        sha512_hash = hashlib.sha512()
        sha512_hash.update(result.encode())
        result = sha512_hash.hexdigest()
    
    return result

if __name__ == "__main__":
    test_data = "Hello World!"
    print("Dữ liệu gốc:", test_data)
    
    # Test SHA-256 với salt
    hashed_256 = modified_sha256(test_data)
    print("\nSHA-256 đã sửa đổi (với salt):", hashed_256)
    
    # Test SHA-512 với nhiều vòng
    hashed_512 = modified_sha512(test_data)
    print("\nSHA-512 đã sửa đổi (10000 vòng):", hashed_512)
