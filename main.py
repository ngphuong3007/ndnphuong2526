def tinh_tong(a, b):
    return a + b

if __name__ == "__main__":
    x, y = 10, 20
    # Sử dụng f-string để chèn biến trực tiếp vào chuỗi
    print(f"Tổng của {x} và {y} là: {tinh_tong(x, y)}")