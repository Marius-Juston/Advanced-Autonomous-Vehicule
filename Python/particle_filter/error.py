import random

from particle_filter.robot import robot, eval

if __name__ == '__main__':

    myrobot = robot()
    N = 1000
    T = 10  # Leave this as 10 for grading purposes.

    p = []
    for i in range(N):
        r = robot()
        r.set_noise(0.05, 0.05, 5.0)
        p.append(r)

    turn = .1
    move = 5.

    for t in range(T):
        myrobot = myrobot.move(turn, move)
        Z = myrobot.sense()

        p = [particle.move(turn, move) for particle in p]
        w = [particle.measurement_prob(Z) for particle in p]

        p3 = []
        index = int(random.random() * N)
        beta = 0.0
        mw = max(w)
        for i in range(N):
            beta += random.random() * 2.0 * mw
            while beta > w[index]:
                beta -= w[index]
                index = (index + 1) % N
            p3.append(p[index])
        p = p3
        
        print(eval(myrobot, p))
