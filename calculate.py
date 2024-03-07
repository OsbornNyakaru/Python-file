def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price
def main():
    # Prompt the user for the original price and discount percentage
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price after applying the discount
    final_price = calculate_discount(price, discount_percent)

    # Print the final price after applying the discount, or the original price if no discount was applied
    if final_price != price:
        print("Final price after discount: $", final_price)
    else:
        print("No discount applied. Original price: $", price)

if __name__ == "__main__":
    main()