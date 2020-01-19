import sys

import pygame

from cube import Cube


class GameEngine:
    def __init__(self, win_width=640, win_height=480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("3D Wireframe Cube Simulation")
        self.clock = pygame.time.Clock()

    def run(self):
        angle_x, angle_y, angle_z = 0.0, 0.0, 0.0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0, 0, 0))

            width, height = self.screen.get_width(), self.screen.get_height()
            fov = 100
            camera_dist = 100

            cube = Cube(size=100)
            cube.rotate(angle_x, angle_y, angle_z)

            for face in cube.faces:
                vertices_2d = [tuple(cube.vertices[i].project(width, height, fov, camera_dist)) for i in face]
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[0], vertices_2d[1])
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[1], vertices_2d[2])
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[2], vertices_2d[3])
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[3], vertices_2d[0])

            angle_x += 1
            angle_y += 1
            angle_z += 1

            pygame.display.flip()


if __name__ == "__main__":
    GameEngine().run()
