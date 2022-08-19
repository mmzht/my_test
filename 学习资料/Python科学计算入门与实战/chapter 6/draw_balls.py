import random

def make_hat(colors,nob):
    hat = []
    for color in colors:
        for _ in nob:
            hat.append(color)
    random.shuffle(hat)
    return hat

def draw_balls(hat,k):
    balls = random.choices(hat,k=k)
    return balls

def draw_ball(hat):
    ball = random.choice(hat)
    hat.remove(ball)
    return ball,hat

def draw_ball(hat):
    index = random.randint(0,len(hat)-1)
    ball = hat.pop(index)
    return ball,hat


def perform_experiment(colors,nob,k,N):
    balls = []
    for _ in range(N):
        hat = make_hat(colors,nob)
        drew = draw_balls(hat,k)
        balls += drew
    counts = [balls.count(color) for color in colors]
    sum_counts = sum(counts)
    return [count/sum_counts for count in counts]

colors = [0,1,2]
nob = [3,3,3]
k = 3
N = 1000
P = perform_experiment(colors,nob,k,N)
