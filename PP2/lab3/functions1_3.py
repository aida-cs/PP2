def solve(num_heads, num_legs):
    rabbits = (num_legs - 2 * num_heads) // 2
    chickens = num_heads - rabbits
    return chickens, rabbits

print(solve(35, 94))
