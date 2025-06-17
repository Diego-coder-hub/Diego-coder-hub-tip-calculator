def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    remove_symbol_1 = d.removeprefix("$")
    result = float(remove_symbol_1)
    return result



def percent_to_float(p):
    remove_symbol_2 = p.removesuffix("%")
    result = float(remove_symbol_2) * 0.01
    return result

main() 