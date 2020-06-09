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

    weights_sum = sum(w)
    w = [weight / weights_sum for weight in w]

    p3 = []
    import random

    for _ in range(N):
        random_goal = random.random()

        start = 0.0

        for i in range(len(w)):
            start += w[i]

            if start >= random_goal:
                p3.append(p[i])
                break
