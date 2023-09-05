#Funktioner = First class object

def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power
if __name__ == "__main__":
    raise_two = generate_power(2)
    raise_three = generate_power(3)

    res = raise_two(4)
    pass