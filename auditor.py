inventory = 0
rejected_entries = 0
MAX_CAPACITY = 500

while True:
    user_input = input("Enter stock quantity or 'quit' to exit: ")

    # User chooses to finish
    if user_input.lower() == "quit":
        break

    try:
        quantity = float(user_input)

        # Negative number
        if quantity < 0:
            print("Invalid input. Please enter a non-negative stock quantity.")
            rejected_entries += 1
            continue

        # Only whole numbers are allowed
        if not quantity.is_integer():
            print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
            rejected_entries += 1
            continue

        quantity = int(quantity)

        # Zero
        if quantity == 0:
            print(
                f"No items added to inventory. "
                f"Total inventory remains: {inventory}"
            )
            continue

        # Exceeds maximum capacity
        if inventory + quantity > MAX_CAPACITY:
            print(
                f"Overstock alert! You cannot add {quantity} items. "
                f"Maximum capacity is {MAX_CAPACITY}."
            )
            rejected_entries += 1
            break

        # Valid quantity
        inventory += quantity

        print(
            f"Added {quantity} items to inventory. "
            f"Total inventory: {inventory}"
        )

    except ValueError:
        print(
            "Invalid input. Please enter a valid stock quantity "
            "or 'quit' to exit."
        )
        rejected_entries += 1


print(f"Total Units Processed: {inventory}")
print(f"Total rejected entries: {rejected_entries}")