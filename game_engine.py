import math
import sys

import pygame

from cube import Cube
from point import Point2D, Point3D


class GameEngine:
    def __init__(self, win_width=640, win_height=480, field_of_vision=200, camera_dist=100):
        self.width = win_width
        self.height = win_height
        self.fov = field_of_vision
        self.camera_dist = camera_dist

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("3D Wireframe Cube Simulation")
        self.clock = pygame.time.Clock()

    def run(self):
        angle = Point3D(30.0, 30.0, 0.0)
        delta = Point3D(0, 0, 0)

        friction_factor = 0.98
        init_pos = None
        dragging = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    dragging = True
                    init_pos = Point2D(*event.pos)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    dragging = False
                elif event.type == pygame.MOUSEMOTION and dragging:
                    curr_pos = Point2D(*event.pos)
                    delta.y, delta.x = (init_pos - curr_pos) * 2 * math.pi / self.width
                    angle += delta

            cube = Cube(size=100, angle_x=angle.x, angle_y=angle.y, angle_z=angle.z)
            self.__draw_cube(cube)

            if not dragging:
                delta *= friction_factor

            angle += delta
            pygame.display.flip()

    def __draw_cube(self, cube):
        self.clock.tick(60)
        self.screen.fill((0, 0, 0))

        for face in cube.faces:
            vertices_2d = [tuple(cube.vertices[i].project(self.width, self.height, self.fov, self.camera_dist))
                           for i in face]
            pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[0], vertices_2d[1])
            pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[1], vertices_2d[2])
            pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[2], vertices_2d[3])
            pygame.draw.line(self.screen, (255, 255, 255), vertices_2d[3], vertices_2d[0])


if __name__ == "__main__":
    GameEngine().run()
