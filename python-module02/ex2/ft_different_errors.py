def garden_operations(operation_number):
    try:
        if operation_number == 0:
            raise (ValueError("invalid literal for int() with base 10: 'abc'"))
        elif operation_number == 1:
            raise (ZeroDivisionError("division by zero"))
        elif operation_number == 2:
            raise (FileNotFoundError("[Errno 2] No such fule or directory: "
                                     "'non/existent/file'"))
        elif operation_number == 3:
            raise (TypeError("can only concatenate str (not "'int'") to str"))
    except (ValueError, ZeroDivisionError, TypeError, FileNotFoundError) as e:
        print(f"Caught {e.__name__}: {e}")


def test_error_types() -> None:
    nums: list = [0, 1, 2, 3]
    for num in nums:
        print(f"Testing operation {num}")
        garden_operations(num)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully")
