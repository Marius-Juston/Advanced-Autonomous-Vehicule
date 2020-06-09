from particle_filter.robot import robot

if __name__ == '__main__':
    N = 1000

    turn = .1
    move = 5

    particles = [robot() for _ in range(N)]
    print(particles[:10])
    particles = [r.move(turn, move) for r in particles]
    print(particles[:10])
