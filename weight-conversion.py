# Weight Conversion Between Kilograms (kg) and Pounds (lb)
# Conversion Rate: 1 kg = 2.20462 lb

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

# Conversion functions are initialized above. Next the main function with some info and prompts

def main():
    print("Weight Converter")
    print("1: Kilograms to Pounds")
    print("2: Pounds to Kilograms")
    choice = input("Enter your choice (1 or 2): ")

# Convert from kg to lb and display the result
    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        lb = kg_to_lb(kg)
        print(f"{kg:.2f} kg = {lb:.2f} lb")

# Convert from kg to lb and display the result
    elif choice == "2":
        lb = float(input("Enter weight in pounds: "))
        kg = lb_to_kg(lb)
        print(f"{lb:.2f} lb = {kg:.2f} kg")

# Error message for invalid choice
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
