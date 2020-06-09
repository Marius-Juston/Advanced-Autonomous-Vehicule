import random

from particle_filter.robot import robot

if __name__ == '__main__':
    myrobot = robot()
    myrobot = myrobot.move(0.1, 5.0)
    Z = myrobot.sense()

    N = 1000
    p = []
    for i in range(N):
        x = robot()
        x.set_noise(0.05, 0.05, 5.0)
        p.append(x)

    p2 = [particle.move(.1, 5.) for particle in p]
    p = p2

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

    print(len(p3))
