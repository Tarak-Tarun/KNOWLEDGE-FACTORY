def temperature_conversion(temp, choice):
    if choice == 1:
        print(f"C to F: {(temp * 9/5) + 32}")
    
    elif choice == 2:
        print(f"C to K: {temp + 273.15}")
    
    elif choice == 3:
        print(f"F to C: {(temp - 32) * 5/9}")
    
    elif choice == 4:
        print(f"F to K: {(temp - 32) * 5/9 + 273.15}")
    
    elif choice == 5:
        print(f"K to C: {temp - 273.15}")
    
    elif choice == 6:
        print(f"K to F: {(temp - 273.15) * 9/5 + 32}")
    
    else:
        print("Invalid choice")


while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Exiting program...")
        break

    temp = float(input("Enter temperature: "))
    temperature_conversion(temp, choice)