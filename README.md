# Robot
# Robot Movement Simulation

Simulates multiple robots moving in a 2D grid terrain based on directional commands like `N2`, `E3`, etc.

## 📦 Features
- Multiple robots with unique IDs
- Collision detection
- Grid-bound movement
- Unit tests

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/robot-movement.git
   cd robot-movement


Install Python (version >= 3.7)

Run the unit tests:



python -m unittest test_robot.py


example 
terrain = Terrain(5, 5)
terrain.add_robot("R1")
terrain.move_robot("R1", "E3")
terrain.move_robot("R1", "S1")
print(terrain.get_robot_position("R1"))  # Output: (1, 3)

