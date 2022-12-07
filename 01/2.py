#!/usr/bin/env python3

with open("input") as data:
    module_masses = [int(n) for n in data]

def fuel_requirements(mass: int) -> int:
    fr = (mass // 3) - 2
    if (fr // 3) > 2:
        return fr + fuel_requirements(fr)
    return fr


answer = 0
for m in module_masses:
    answer += fuel_requirements(m)

print()
# 3372756 Too low
print(answer)
