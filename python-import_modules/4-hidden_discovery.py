#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import hidden_4
    for i in dir(hidden_4):
        if "__" not in i:
            print(i)
