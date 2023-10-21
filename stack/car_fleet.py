"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""
import numpy as np
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        sorted_positions = {position[key]:speed[key] for key in np.argsort(position)[::-1]}
        stack = []
        for position, speed in sorted_positions.items():
            if not stack:
                stack.append([position, speed])
            else:
                if speed > stack[-1][1]:  # if current speed is greater than stacked speed
                    left_distance = target - position
                    left_distance_stack = target - stack[-1][0]
                    if left_distance / speed <= left_distance_stack /stack[-1][1]:
                        continue
                    else:
                        stack.append([position, speed])
                else:
                    stack.append([position, speed])

        return len(stack)
    
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

target1 = 10
position1 = [3]
speed1 = [3]

target2 = 100
position2 = [0,2,4]
speed2 = [4,2,1]

sol = Solution()

print(sol.carFleet(target, position, speed))
print(sol.carFleet(target1, position1, speed1))
print(sol.carFleet(target2, position2, speed2))
