# app.py
def greet(name):
    reversed_name = name[::-1]  # Reverse the user's name
    return f"Hello, {reversed_name}!"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
