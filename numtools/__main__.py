import argparse
from .core import factorial, fib

def main():
    parser = argparse.ArgumentParser(prog="numtools", description="Tiny math helpers")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("factorial", help="Compute n!")
    p1.add_argument("n", type=int)

    p2 = sub.add_parser("fib", help="Compute nth Fibonacci (0-indexed)")
    p2.add_argument("n", type=int)

    args = parser.parse_args()

    if args.cmd == "factorial":
        print(factorial(args.n))
    elif args.cmd == "fib":
        print(fib(args.n))

if __name__ == "__main__":
    main()
