def contract_calculator():
    try:
        monthly_cost = float(input("Enter monthly contract cost (£): "))
        months = int(input("Enter contract length (months): "))
        upfront_cost = float(input("Enter upfront cost (£): "))
    except ValueError:
        print("Please enter numbers only.")
        return

    total_cost = (monthly_cost * months) + upfront_cost

    print("\n----- Contract Summary -----")
    print(f"Monthly Cost: £{monthly_cost:.2f}")
    print(f"Contract Length: {months} months")
    print(f"Upfront Cost: £{upfront_cost:.2f}")
    print(f"Total Contract Cost: £{total_cost:.2f}")


def payment_tracker():
    try:
        total_bill = float(input("Enter bill amount (£): "))
        amount_paid = float(input("Enter amount paid (£): "))
    except ValueError:
        print("Please enter numbers only.")
        return

    balance = total_bill - amount_paid

    print("\n----- Payment Summary -----")
    print(f"Bill Amount: £{total_bill:.2f}")
    print(f"Amount Paid: £{amount_paid:.2f}")
    print(f"Remaining Balance: £{balance:.2f}")

    if balance <= 0:
        print("Account fully paid.")
    else:
        print("Payment still required.")


def support_chatbot():
    print("\nWelcome to Customer Support (type 'exit' to go back)")

    while True:
        question = input("\nHow can I help you today? ").lower()

        if question == "exit":
            print("Thank you for contacting support.")
            break
        elif "data" in question:
            print("Please restart your device and check if mobile data is enabled.")
        elif "sim" in question:
            print("Please remove and reinsert the SIM card, then restart your device.")
        elif "bill" in question:
            print("You can check your bill through the app or your online account.")
        elif "upgrade" in question:
            print("You can view available upgrades by logging into your account.")
        elif "cancel" in question:
            print("Please contact support to ask about cancelling your contract.")
        else:
            print("Sorry, I don't understand that request.")


def main():
    while True:
        print("\n==== XL TECH SOLUTIONS ====")
        print("1. Contract Calculator")
        print("2. Payment Tracker")
        print("3. Customer Support Chatbot")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            contract_calculator()
        elif choice == "2":
            payment_tracker()
        elif choice == "3":
            support_chatbot()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


main()