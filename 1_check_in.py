def parse_quantity(raw):
    try:
        result = int(raw)
    except ValueError:
        print("except")
        result = 0
    else:
        print("else")
    finally:
        print("finally")
    return result

print(parse_quantity("12"))
print(parse_quantity("abc"))
