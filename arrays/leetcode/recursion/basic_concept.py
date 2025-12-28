def factorial(n):
    print(f"Entering factorial({n})")

    if n <= 1:
        print(f"Returning 1 from factorial({n})")
        return 1

    result = n * factorial(n - 1)
    print(f"Returning {result} from factorial({n})")
    return result
