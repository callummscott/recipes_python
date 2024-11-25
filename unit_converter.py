import re

masses = {"kg":1000, "lbs":453.5924, "g":1}
volumes = {"L":1000, "pt":568.2612, "tbsp":15, "tsp":5, "ml":1}
unit_pattern = r"^(\d+\.?\d*)([a-zA-Z]+)$"

def parse_quantity(initial:str) -> str:
    """ Converts ingredient quantity into `match` object, numerical
     quantity stored in match.group(1), unit stored in match.group(2). """
    if not isinstance(initial, str):
        raise TypeError("Invalid quantity type")
    
    unit_pattern = r"^(\d+\.?\d*)([a-zA-Z]+)$"
    match = re.match(unit_pattern, initial)

    if match:
        return match
    else:
        raise ValueError("Invalid quantity input")
    

def unit_converter(initial:str, desired:str) -> str:
    """ Takes in a number-unit string (e.g. '123.45ml'), and a unit (e.g. 'ml') and returns the converted value """
   
    # Parse out the units from the inputs,
    #   raises error if no units or invalid string
    parsed_quantity = parse_quantity(initial)

    number_string = parsed_quantity.group(1)
    unit_a = parsed_quantity.group(2)
    unit_b = desired

    # Check if the units are actually translatable or not, raise error if not?
    # Apply relevant conversions if they are translatable
    if (unit_a in masses) and (unit_b in masses):
        value = float(number_string)*masses[unit_a]/masses[unit_b]
        value = int(value) if value.is_integer() else value
        return f"{value}" + desired
    elif (unit_a in volumes) and (unit_b in volumes):
        value = float(number_string)*volumes[unit_a]/volumes[unit_b]
        value = int(value) if value.is_integer() else value
        return f"{value}" + desired
    else:
        raise ValueError(f"Units are not translatable: '{unit_a}' cannot be converted to '{unit_b}'.")