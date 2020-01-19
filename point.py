import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x, self.y = int(x), int(y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f'Point2D(x = {self.x}, y = {self.y})'

    def __repr__(self):
        return self.__str__()


class Point3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __str__(self):
        return f'Point3D(x = {self.x}, y = {self.y}, z = {self.z})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def __degree_to_radian(degree):
        return degree * math.pi / 180

    def __get_cos_and_sine(self, angle):
        radian = self.__degree_to_radian(angle)
        return math.cos(radian), math.sin(radian)

    def rotate_x(self, angle):
        cosine, sine = self.__get_cos_and_sine(angle)
        self.y = self.y * cosine - self.z * sine
        self.z = self.y * sine + self.z * cosine
        return self

    def rotate_y(self, angle):
        cosine, sine = self.__get_cos_and_sine(angle)
        self.z = self.z * cosine - self.x * sine
        self.x = self.z * sine + self.x * cosine
        return self

    def rotate_z(self, angle):
        cosine, sine = self.__get_cos_and_sine(angle)
        self.x = self.x * cosine - self.y * sine
        self.y = self.x * sine + self.y * cosine
        return self

    def rotate(self, angle_x, angle_y, angle_z):
        # self.rotate_x(angle_x).rotate_y(angle_y).rotate_z(angle_z)
        self.rotate_x(angle_x)
        self.rotate_y(angle_y)
        self.rotate_z(angle_z)
        return self

    def project(self, win_width, win_height, camera_distance, field_of_view):
        factor = field_of_view / (camera_distance + self.z)
        # factor = 1
        x = self.x * factor + win_width / 2
        y = self.y * factor + win_height / 2
        return Point2D(x, y)
