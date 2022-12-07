#!/usr/bin/env python3

with open("input") as data:
    module_masses = [int(n) for n in data]

answer = 0
for m in module_masses:
    answer += (m // 3) - 2

print()
print(answer)
