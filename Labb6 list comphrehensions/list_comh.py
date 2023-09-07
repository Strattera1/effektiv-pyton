if __name__ == "__main__":
    
    numbers = [i for i in range(1,11)]
    even_numbers = [i for i in numbers if i% 2 == 0]
    odd_numbesr = [i for i in numbers if i % 2 != 0]

    vowels = "aouåeiyäö"
    namn = "Nils Paulson"
    vowels_in_name = [i for i in namn if i in vowels and i not in vowels_in_name]
    print (vowels_in_name)