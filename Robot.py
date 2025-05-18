class Terrain:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.robots = {}  

    def is_cell_occupied(self, x, y, exclude_robot=None):
        for rid, robot in self.robots.items():
            if rid != exclude_robot and robot.x == x and robot.y == y:
                return True
        return False

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError(f"Robot ID {robot_id} already exists.")
        self.robots[robot_id] = Robot(robot_id, 0, 0)

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            raise ValueError("Robot not found.")
        robot = self.robots[robot_id]
        robot.move(command, self)

    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError("Robot not found.")
        return self.robots[robot_id].x, self.robots[robot_id].y


class Robot:
    DIRECTION_MAP = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
    }

    def __init__(self, robot_id, x, y):
        self.robot_id = robot_id
        self.x = x
        self.y = y

    def move(self, command, terrain):
        direction = command[0].upper()
        steps = int(command[1:])

        dx, dy = Robot.DIRECTION_MAP[direction]
        for _ in range(steps):
            new_x = self.x + dx
            new_y = self.y + dy

            # Boundary check
            if not (0 <= new_x < terrain.rows and 0 <= new_y < terrain.cols):
                break

            # Collision check
            if terrain.is_cell_occupied(new_x, new_y, self.robot_id):
                break

            self.x = new_x
            self.y = new_y
