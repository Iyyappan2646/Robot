# test_robot.py

import unittest
from robot import Terrain

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain(5, 5)
        self.terrain.add_robot("R1")
        self.terrain.add_robot("R2")

    def test_initial_position(self):
        self.assertEqual(self.terrain.get_robot_position("R1"), (0, 0))

    def test_simple_move(self):
        self.terrain.move_robot("R1", "S2")
        self.assertEqual(self.terrain.get_robot_position("R1"), (2, 0))

    def test_boundary_stop(self):
        self.terrain.move_robot("R1", "N2")
        self.assertEqual(self.terrain.get_robot_position("R1"), (0, 0))  # Cannot move

    def test_collision(self):
        self.terrain.move_robot("R1", "S2")
        self.terrain.move_robot("R2", "S3")
        # R2 should stop before hitting R1
        self.assertEqual(self.terrain.get_robot_position("R2"), (1, 0))

    def test_multiple_moves(self):
        self.terrain.move_robot("R1", "S1")
        self.terrain.move_robot("R1", "E2")
        self.assertEqual(self.terrain.get_robot_position("R1"), (1, 2))

if __name__ == '__main__':
    unittest.main()
