import matplotlib.pyplot as plt
import numpy as np

from pid_control.robot import Robot

robot = Robot()
robot.set(0, 1, 0)


def run(robot, tau_p, tau_d, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    # TODO: your code here
    prev_cte = -robot.y
    dt = 1

    for _ in range(n):
        cte = -robot.y
        d_cte = (cte - prev_cte) / dt

        steer = tau_p * cte + tau_d * d_cte

        robot.move(steer, speed)

        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

        prev_cte = cte

    return x_trajectory, y_trajectory


x_trajectory, y_trajectory = run(robot, 0.2, 3.0)
n = len(x_trajectory)

plt.plot(x_trajectory, y_trajectory, 'g', label='PD controller')
plt.plot(x_trajectory, np.zeros(n), 'r', label='reference')
plt.show()
