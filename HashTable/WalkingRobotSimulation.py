'''
A robot on an infinite XY-plane starts at point (0, 0) facing north. 
The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. 
There are only three possible types of instructions the robot can receive:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). 
If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

Note:

There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. 
However, it will be unable to return to (0, 0) due to the obstacle.
North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.

'''

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
         # Directions represented as (dx, dy) pairs
        directions = [
            (0, 1),   # North
            (1, 0),   # East
            (0, -1),  # South
            (-1, 0)   # West
        ]

        # Start at origin (0, 0)
        x, y = 0, 0
        direction_index = 0  # Start facing North
        max_distance = 0

        # Convert obstacles list to a set for fast lookup
        obstacle_set = set(map(tuple, obstacles))  # Use set of tuples for faster lookup

        # Process each command
        for command in commands:
            if command == -2:  # Turn left 90 degrees
                direction_index = (direction_index + 3) % 4
            elif command == -1:  # Turn right 90 degrees
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = directions[direction_index]

                for _ in range(command):
                    new_x = x + dx
                    new_y = y + dy

                    if (new_x, new_y) in obstacle_set:
                        break  # Stop moving if there's an obstacle

                    x, y = new_x, new_y
                    max_distance = max(max_distance, x * x + y * y)

        return max_distance