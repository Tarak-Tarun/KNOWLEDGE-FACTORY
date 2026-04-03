def total_bill(item1=0,*remaining_items):
    total=item1
    if(total==0):
        print("Your Bill is ",total)
        return
    for i in remaining_items:
        total+=i
    print(f"Your Total Bill is {total}")
    return 
(total_bill())
(total_bill(10,30,50,70,90))
(total_bill(10))