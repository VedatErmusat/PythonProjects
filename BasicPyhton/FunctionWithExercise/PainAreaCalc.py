import math
def paint_calc(width, height, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(width = test_w,height = test_h,cover = coverage)
