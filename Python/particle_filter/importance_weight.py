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

    print(max(w))
    print(min(w))
