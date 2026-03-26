def input_temperature(tem_strp: str) -> None:
    try:
        temp: int = int(tem_strp)
        if temp < 0:
            raise (ValueError(f"{temp}ºC is too cold for plants (min 0º)"))
        elif temp > 40:
            raise (ValueError(f"{temp}ºC is too hot for plants (max 40º)"))
        else:
            print(f"Temperature is now {temp}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    print("Input data is '25'")
    input_temperature("25")
    print("")
    print("Input data is 'abc'")
    input_temperature("abc")
    print("")
    print("Input data is '100'")
    input_temperature("100")
    print("")
    print("Input data is '-50'")
    input_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature()
    print("")
    print("All test completed - program didn't crash!")
