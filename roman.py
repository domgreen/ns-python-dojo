def to_decimal(roman_number: str) -> int:
    """
    Takes a roman number and returns its decimal value
    """
    result = 0
    prev_number = 0
    for char in roman_number:
        match char:
            case "I":
                result += 1
                prev_number = 1
            case "V":
                if prev_number == 1:
                   result -= 2
                result = result + 5
                prev_number = 5
            case "X":
                result += 10
            case "L":
                result += 50
            case "C":
                result += 100
            case "D":
                result += 500
            case "M":
                result += 1000
    return result