def to_decimal(roman_number):
    
    result = 0
    match roman_number:
        case "I":
            result = 1
        case "II":
            result = 2
        case "V":
            result = 5
    
    return result