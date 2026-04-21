def categorize(height, weight):
    if height > 160:
        height_label = "cao"
    elif height > 150:
        height_label = "cao bình thường"
    else:
        height_label = "lùn"

    weight_label = "chuppi" if weight >= 80 else "không chuppi"

    return f"{height_label} và {weight_label}."

# To handle multiple inputs, use a loop
while True:
    try:
        height = int(input("Enter your height in cm (or 0 to stop): "))
        if height == 0:
            break
        weight = int(input("Enter your weight in kg: "))
        result = categorize(height, weight)
        print(result)
    except ValueError:
        print("Please enter valid numbers.")

