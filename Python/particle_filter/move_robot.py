from math import pi

from particle_filter.robot import robot

if __name__ == '__main__':
    myrobot = robot()
    myrobot.set(30, 50, pi / 2)
    myrobot = myrobot.move(-pi / 2, 15)
    print(myrobot.sense())
    myrobot = myrobot.move(-pi / 2, 10)
    print(myrobot.sense())
