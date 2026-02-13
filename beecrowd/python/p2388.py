# Tacógrafo

intervals = int(input())
total_distance = 0
for _ in range(intervals):
    time_elapsed, average_speed = map(int, input().split())
    total_distance += time_elapsed * average_speed

print(total_distance)
