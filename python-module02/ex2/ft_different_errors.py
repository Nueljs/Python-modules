def garden_operations(operation_number):
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            10 / 0
        elif operation_number == 2:
            open("/non/existent/file")
        elif operation_number == 3:
            "Hola" + 5
        elif operation_number == 4:
            print("Operation completed succesfully")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        name = e.__class__.__name__
        print(f"Caught {name}: {e}")


def test_error_types() -> None:
    nums: list = [0, 1, 2, 3, 4]
    for num in nums:
        print(f"Testing operation {num}...")
        garden_operations(num)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("")
    print("All error types tested successfully")
