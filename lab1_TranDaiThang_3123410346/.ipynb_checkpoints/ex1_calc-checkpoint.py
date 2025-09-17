print ("calculator basics")
while True:
    try:
        a,b = map(int,input("Moi ban nhap vao a, b (co khoang cach): ").split())
        break
    except ValueError:
        print("a,b nhap vao khong hop le")
print(f"c = {a} + {b} = {a + b}")