#Lambda är en funktion utan namn. Det är Anno
from dataclasses import dataclass

@dataclass
class Player:
    Name: str
    Goals: int
    Assists: int
lista = [Player("Nils",14,20), Player("Steffo",3,50), Player("Erik",1,0)]

def sort_func(p):
    return p.Goals + p.Assists

lista.sort(key=sort_func,reverse=True)

print (lista)