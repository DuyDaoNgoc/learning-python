def categorize(height, weight):
    if height >= 180 and weight >= 80:
        return "cao và chuppi."
    elif height >= 180 and weight < 80:
        return ""
    elif height < 180 and weight >= 80:
        return "cao bình thường nhưng chuppi."
    elif height < 180 and weight < 80:
        return "cao bình thường và không chuppi."
    elif height <= 170   and weight >= 80:
        return "cao bình thường nhưng chuppi."
    elif height <= 170 and weight < 80:
        return "cao bình thường và không chuppi."
    elif height > 170 and weight >= 80:
        return "cao bình thường và chuppi."

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
