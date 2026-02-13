# Pula Sapo

frog_jump, pipe_number = map(int, input().split())

pipe_heights = list(map(int, input().split()))

for i in range(pipe_number - 1):
    current_pipe = pipe_heights[i]
    next_pipe = pipe_heights[i + 1]
    if abs(next_pipe - current_pipe) > frog_jump:
        print('GAME OVER')
        break
else:
    print('YOU WIN')
