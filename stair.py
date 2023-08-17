"""Stair way to heaven"""


def stairetor(human_step, stair_size):
    """https://open.spotify.com/track/5CQ30WqJwcep0pYcV4AMNc?si=99d3fbc8b7864400"""
    step_use = 0
    stair_sum = 0
    step_get = 0
    step_need = 0
    for _ in range(stair_size):
        current_stair = int(input())
        stair_sum += current_stair
        step_need += current_stair
        if stair_sum >= human_step:
            if current_stair == human_step:
                if stair_sum - current_stair != 0:
                    step_get += stair_sum
                    step_use += 2
                    stair_sum = 0
                else:
                    step_get += current_stair
                    step_use += 1
                    stair_sum = 0
            elif stair_sum == human_step:
                step_get += stair_sum
                step_use += 1
                stair_sum = 0
            elif stair_sum - current_stair < human_step:
                step_get += stair_sum - current_stair
                step_use += 1
                stair_sum = current_stair
    if stair_sum <= human_step and stair_sum != 0:
        step_use += 1
        step_get += stair_sum
    if step_need != step_get:
        print("NO")
    else:
        print(step_use)


stairetor(int(input()), int(input()))
