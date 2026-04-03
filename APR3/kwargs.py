def total_bill(**items):
    total = 0
    
    for name, price in items.items():
        print(f"{name}: {price}")
        total += price
    
    print("Total Bill:", total)
total_bill(burger=120, pizza=250, coke=60)