
import hashlib
import os
from tkinter import filedialog, Tk, Label, Button, Text, END
from PIL import Image

def calculate_image_hash(image_path):
    """Tính toán giá trị băm SHA-512 của file ảnh"""
    sha512_hash = hashlib.sha512()
    
    try:
        # Đọc ảnh theo từng khối
        with open(image_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha512_hash.update(chunk)
        return sha512_hash.hexdigest()
    except Exception as e:
        return f"Lỗi: {str(e)}"

def select_image():
    """Chọn file ảnh và hiển thị giá trị băm"""
    file_path = filedialog.askopenfilename(
        filetypes=[("image","anh.jpg"),])
    
    if file_path:
        # Hiển thị đường dẫn file
        path_text.delete(1.0, END)
        path_text.insert(END, f"File: {file_path}\n\n")
        
        # Tính và hiển thị giá trị băm
        hash_value = calculate_image_hash(file_path)
        path_text.insert(END, f"Giá trị băm SHA-512:\n{hash_value}")

# Tạo giao diện
root = Tk()
root.title("Băm Ảnh SHA-512")
root.geometry("800x400")
root.configure(bg='#2d2d2d')

# Tạo các thành phần giao diện
Label(root, text="Chọn ảnh để tính giá trị băm SHA-512", 
      bg='#2d2d2d', fg='white', font=('Arial', 14)).pack(pady=20)

Button(root, text="Chọn Ảnh", command=select_image,
       bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=10)

path_text = Text(root, height=10, width=70, bg='#404040', fg='white',
                 font=('Courier', 10))
path_text.pack(pady=20)

root.mainloop()
