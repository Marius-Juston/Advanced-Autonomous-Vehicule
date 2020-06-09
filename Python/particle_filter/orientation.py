import random

from particle_filter.robot import robot

if __name__ == '__main__':
    myrobot = robot()

    N = 1000
    p = []
    for i in range(N):
        x = robot()
        x.set_noise(0.05, 0.05, 5.0)
        p.append(x)

    t = 10

    turn = .1
    move = 5.

    for _ in range(t):
        myrobot = myrobot.move(turn, move)
        Z = myrobot.sense()

        p = [particle.move(turn, move) for particle in p]
        w = [particle.measurement_prob(Z) for particle in p]

        p3 = []

        max_weight = max(w) * 2
        index = random.randrange(N)
        beta = 0

        for _ in range(N):
            beta += random.random() * max_weight

            while w[index] < beta:
                beta -= w[index]
                index = (index + 1) % N

            p3.append(p[index])

        p = p3

    print(p)
    print(myrobot)
