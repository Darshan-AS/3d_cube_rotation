from point import Point3D


class Cube:
    def __init__(self, size=2, angle_x=0.0, angle_y=0.0, angle_z=0.0):
        self.size = size
        self.angle_x, self.angle_y, self.angle_z = angle_x, angle_y, angle_z
        self.vertices = self.__calculate_vertices()
        self.faces = self.__get_faces()
        self.rotate(self.angle_x, self.angle_y, self.angle_z)

    def __calculate_vertices(self):
        dist = self.size / 2

        return [
            Point3D(-dist, -dist, dist),
            Point3D(-dist, dist, dist),
            Point3D(dist, dist, dist),
            Point3D(dist, -dist, dist),
            Point3D(-dist, -dist, -dist),
            Point3D(-dist, dist, -dist),
            Point3D(dist, dist, -dist),
            Point3D(dist, -dist, -dist)
        ]

    @staticmethod
    def __get_faces():
        return [(0, 1, 2, 3), (3, 2, 6, 7), (7, 6, 5, 4), (4, 5, 1, 0), (1, 5, 6, 2), (0, 4, 7, 3)]

    def rotate(self, angle_x, angle_y, angle_z):
        for vertex in self.vertices:
            vertex.rotate(angle_x, angle_y, angle_z)
