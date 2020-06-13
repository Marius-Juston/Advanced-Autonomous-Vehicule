import matplotlib.pyplot as plt
import numpy as np

from pid_control.robot import Robot

robot = Robot()
robot.set(0, 1, 0)


def run(robot, tau, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []

    for _ in range(n):
        cte = -robot.y
        steer = cte * tau

        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

    return x_trajectory, y_trajectory


x_trajectory, y_trajectory = run(robot, 0.1)
n = len(x_trajectory)

plt.plot(x_trajectory, y_trajectory, 'g', label='P controller')
plt.plot(x_trajectory, np.zeros(n), 'r', label='reference')
plt.show()
