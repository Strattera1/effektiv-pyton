from countries import Country,countries
#Labb1
population_between_8m_12m = [p for p in countries if p.Population > 8000000 and p.Population < 12000000]

for x in population_between_8m_12m:
    print (f"population between 8-12 m : {x.Namn} \n\n")


#2. Skapa en lista med alla länder som har minst 15 bokstäver i sitt namn. Skriv ut namn och population för varje

# population_with_15_letters = [p for p in countries if len(p.Namn) >= 15]

# for x in population_with_15_letters:
#     print(f"Country: {x.Namn},\n Pop {x.Population}")

#3. Skapa en lista med alla länder som har som börjar på A eller har en huvudstad som börjar på A. Skriv ut namn och capital för varje

# country_with_A = [i for i in countries if i.Namn.startswith ("A") or i for i in countries if i.Capital.startswith("A")]

# for x in country_with_A:
#     print (f"Country: {x.Namn} \n  Capital: {x.Capital}")

#4. Skapa en lista med alla länder som där man pratar English
# Skriv ut namn och capital för varje 

english_country = [p for p in countries if p.Langages == ["English"]]

# for x in english_country:
#     print(f"Country: {x.Namn} \n Capital: {x.Capital} \n Lagagues{x.Langages}")

#5. Skapa en lista med FÖRSTA BOKSTAVEN för alla capitals
#  länder som med population mindre än 1000000.  Skriv ut listan i formatet (ex "VAVRST" om det är 6 stycken etc)

population_first_letter_capital = [p.Capital[0] for p in countries if p.Population > 1000000]

print(*population_first_letter_capital)


#6. Skapa en lista som i list comprehension omvandlar alla numeriska karaktärer
#  i en sträng till int ( Tips! Python har inbyggd metod för att se om en sträng är numerisk eller alfabetisk! =) ) Finns inga siffror blir listan tom.

#if_int = [i for i in countries if  ]