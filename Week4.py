def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

try:
    with open("input.txt", "r") as file:
        lines = file.readlines()
        price = float(lines[0])
        discount_percent = float(lines[1])

    final_price = calculate_discount(price, discount_percent)

    with open("output.txt", "w") as file:
        file.write("Final price: " + str(round(final_price, 2)))

except FileNotFoundError:
    print("Input file not found.")
except ValueError:
    print("Invalid data in the file.")
except Exception as e:
    print("An error occurred:", e)
