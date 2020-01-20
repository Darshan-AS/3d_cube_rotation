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

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Point2D(self.x * k, self.y * k)

    def __floordiv__(self, k):
        return Point2D(self.x // k, self.y // k)

    def __truediv__(self, k):
        return Point2D(self.x / k, self.y / k)


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

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, k):
        return Point3D(self.x * k, self.y * k, self.z * k)

    def __floordiv__(self, k):
        return Point3D(self.x // k, self.y // k, self.z // k)

    def __truediv__(self, k):
        return Point3D(self.x / k, self.y / k, self.z / k)

    @staticmethod
    def __degree_to_radian(degree):
        return degree * math.pi / 180

    def __get_cos_and_sine(self, angle):
        radian = self.__degree_to_radian(angle)
        return math.cos(radian), math.sin(radian)

    def rotate_x(self, angle):
        cosine, sine = self.__get_cos_and_sine(angle)
        y = self.y * cosine - self.z * sine
        z = self.y * sine + self.z * cosine
        self.y, self.z = y, z
        return self

    def rotate_y(self, angle):
        cosine, sine = self.__get_cos_and_sine(angle)
        z = self.z * cosine - self.x * sine
        x = self.z * sine + self.x * cosine
        self.z, self.x = z, x
        return self

    def rotate_z(self, angle):
        cosine, sine = self.__get_cos_and_sine(angle)
        x = self.x * cosine - self.y * sine
        y = self.x * sine + self.y * cosine
        self.x, self.y = x, y
        return self

    def rotate(self, angle_x, angle_y, angle_z):
        self.rotate_x(angle_x).rotate_y(angle_y).rotate_z(angle_z)
        return self

    def project(self, win_width, win_height, camera_distance, field_of_view):
        factor = field_of_view / (camera_distance + self.z)
        x = self.x * factor + win_width / 2
        y = self.y * factor + win_height / 2
        return Point2D(x, y)
