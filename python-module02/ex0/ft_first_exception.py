def input_temperature(tem_strp: str) -> int:
    temp: int = int(tem_strp)
    return (print(f"Temperature is now {temp}ºC"))


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        input_temperature("25")
    except ValueError as e:
        print(f"{e}")
    print("")
    try:
        print("Input data is 'abc'")
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("")
    test_temperature()
    print("")
    print("All test completed - program didn't crash!")
