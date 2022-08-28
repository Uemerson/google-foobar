# Fuel Injection Perfection
# =========================

# Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit of sabotage while you're at it -- so you took the job gladly.

# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

# The fuel control mechanisms have three operations:

# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

# The fuel control mechanisms have three operations:

# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution('15')
# Output:
#     5

# Input:
# solution.solution('4')
# Output:
#     2

# -- Java cases --
# Input:
# Solution.solution('4')
# Output:
#     2

# Input:
# Solution.solution('15')
# Output:
#     5

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.


# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child):
#         self.children.append(child)


# def solution(n):
#     root = Node(int(n))
#     level = [root]
#     aux = 0
#     seen_values = []
#     while len(level) > 0:
#         next_nodes = []
#         for node in level:
#             if node.values in seen_values:
#                 continue
#             seen_values.append(node.value)
#             if node.value == 1:
#                 return aux
#             if node.value % 2 == 0:
#                 node.add_child(Node(node.value / 2))
#             else:
#                 node.add_child(Node(node.value + 1))
#                 node.add_child(Node(node.value - 1))
#             for child in node.children:
#                 next_nodes.append(child)
#         level = next_nodes
#         aux = aux + 1


def solution(n):
    return find_solution(long(n))


def find_solution(n):
    steps = 0

    while n > 1:
        if n & 1 == 0:
            n >>= 1
        else:
            lowest_plus = (n + 1) & ~(n + 1 - 1)
            lowest_minus = (n - 1) & ~(n - 1 - 1)

            if lowest_minus > lowest_plus or lowest_minus == n - 1:
                n -= 1
            else:
                n += 1

        steps += 1

    return steps
