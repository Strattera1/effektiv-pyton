# Vi kan funktioner redan. 
# vi använder oss av unpacking
from faker import Faker
import random
from dataclasses import dataclass
@dataclass
class GameScore:
    player_name: str
    score: int


def get_lowest_score(list_of_game_scores:list [GameScore]) -> int:
    smaller_score = None
    for game_score in game_scores:
        if smaller_score is None:
            smaller_score= game_score.score
            continue
        if game_score.score < smaller_score:
            smaller_score = game_score.score
    return smaller_score


        

def  get_highest_score (list_of_game_scores: list[GameScore]) -> int:
    bigger_score = None
    for game_score in game_scores:
        if bigger_score is None:
            bigger_score = game_score.score
        if game_score.score > bigger_score:
            bigger_score = game_score.score
    return bigger_score

def get_lowest_highest_scores(list_of_game_scores:list[GameScore]) -> int:
    highest_score = get_highest_score(list_of_game_scores)
    lowest_score = get_lowest_score(list_of_game_scores)
    return lowest_score,highest_score
    

if __name__ =="__main__":
    game_scores = []
    faker = Faker()
    for i in range (1000):
        random_score = random.randint(10,10_000)
        game_score = GameScore(player_name= faker.name(),
                               score= random_score)
        game_scores.append(game_score)

    
    lowest_score,highest_score = get_lowest_highest_scores(game_scores)
    print(f" lowest score {lowest_score}, highest score {highest_score}")








    def add(a:int,b:int,c:int) -> int:
        return a + b, a + c
    

    def summerise (*args) -> int:
        _sum = 0
        for number in args:
            _sum += number
        return _sum
    
  