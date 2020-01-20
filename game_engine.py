import math
import sys

import pygame

from cube import Cube
from point import Point2D


class GameEngine:
    def __init__(self, win_width=640, win_height=480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("3D Wireframe Cube Simulation")
        self.clock = pygame.time.Clock()

    def run(self):
        angle_x, angle_y, angle_z = 0.0, 0.0, 0.0
        delta_x, delta_y, delta_z = 0, 0, 0

        width, height = self.screen.get_width(), self.screen.get_height()
        mouse_start, mouse_end = None, None
        drag = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    drag = True
                    mouse_start = Point2D(*event.pos)
                    print(mouse_start)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    drag = False
                elif event.type == pygame.MOUSEMOTION and drag:
                    curr_pos = Point2D(*event.pos)
                    delta_y = (mouse_start.x - curr_pos.x) * 2 * math.pi / width
                    delta_x = (mouse_start.y - curr_pos.y) * 2 * math.pi / height

                    angle_x += delta_x
                    angle_y += delta_y

            self.clock.tick(50)
            self.screen.fill((0, 0, 0))

            width, height = self.screen.get_width(), self.screen.get_height()
            fov = 200
            camera_dist = 100

            cube = Cube(size=100)
            cube.rotate(angle_x, angle_y, angle_z)

            for face in cube.faces:
                vertices_2d = [tuple(cube.vertices[i].project(width, height, fov, camera_dist)) for i in face]
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[0], vertices_2d[1])
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[1], vertices_2d[2])
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[2], vertices_2d[3])
                pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[3], vertices_2d[0])

            angle_x += delta_x
            angle_y += delta_y
            angle_z += delta_z

            pygame.display.flip()


if __name__ == "__main__":
    GameEngine().run()
