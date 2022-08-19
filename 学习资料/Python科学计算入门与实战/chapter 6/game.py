import random
class Game:
    def __init__(self):
        self.fruits = ["苹果","梨子","香蕉","橙子","榴莲"]
        self.labels = [1,2,3,4,5]
        self.weights = None
        self.investment = 0
        self.payback = 0

    def set_weights(self,weights):
        self.weights = weights

    def press_button(self):
        self.investment += 1
        labels = self.labels
        weights = self.weights
        rn = random.choices(labels,weights=weights,k=2)
        if rn == [5,5]:
            self.payback += 30
        if rn == [3,3]:
            self.payback += 5
        if rn == [1,1]:
            self.payback += 1

    def play_rounds(self,N):
        for _ in range(N):
            self.press_button()

    def rate_of_return(self):
        if not self.investment:
            return 0
        return (self.payback-self.investment)/self.investment

    

import random
def play_rounds(N):
    labels = [1,2,3,4,5]
    investment = 0
    payback = 0
    for _ in range(N):
        investment += 1
        weights = [0.4,0.15,0.2,0.15,0.1]
        rn = random.choices(labels,weights = weights,k=2)
        if rn == [5,5]:
            payback += 30
        if rn == [3,3]:
            payback += 5
        if rn == [1,1]:
            payback += 1
    return investment,payback

        
        
            
    
