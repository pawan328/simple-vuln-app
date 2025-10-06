def get_user_input():
    user_input = input("Enter a number: ")
    # Vulnerable: using unsanitized input in eval
    result = eval(user_input)
    print(f"Result: {result}")

if __name__ == "__main__":
    get_user_input()
