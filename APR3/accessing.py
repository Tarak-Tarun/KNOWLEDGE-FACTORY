# G → Global scope
x = "Global Variable"

def outer():
    # E → Enclosing scope
    x = "Enclosing Variable"
    
    def inner():
        # L → Local scope
        x = "Local Variable"
        
        print("Inside inner():")
        print("L (Local):", x)              # uses local
        print("B (Built-in):", len(x))      # len is built-in
        
    inner()
    
    print("\nInside outer():")
    print("E (Enclosing):", x)              # uses enclosing

outer()

print("\nOutside functions:")
print("G (Global):", x)                    # uses global