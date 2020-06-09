from particle_filter.robot import robot

if __name__ == '__main__':
    N = 1000

    particles = [robot() for _ in range(N)]

    print(len(particles))
