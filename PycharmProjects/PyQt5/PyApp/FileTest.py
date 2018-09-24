try:
    with open("fun.py", 'r') as f:
        data = f.read()
        print(data)
except Exception as e:
    print("Deo mo duoc")