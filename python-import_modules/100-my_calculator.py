#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithemetic operations."""
    from calculator_1 import add, sub, mul, div
    import calculator_1
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = {"+": add. "-": sub. "*": mul. "/": div}
    if sys.argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operator: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argc[3])
    print("<a> <operator> <b> = <result>".format(a, sys.argv[2], b, operator[sys.argv[2]](a, b)))