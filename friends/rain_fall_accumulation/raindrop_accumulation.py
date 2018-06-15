from typing import List


def raindrop_accumulation(heights):
    if len(heights) < 2:
        return 0

    max_heights_to_left = calc_max_heights_to_left(heights)
    max_heights_to_right = calc_max_heights_to_left(heights[::-1])[::-1]
    accumulation = 0
    for i, height in enumerate(heights):
        max_fill = min(max_heights_to_left[i], max_heights_to_right[i])
        if max_fill > height:
            accumulation += max_fill - height
    return accumulation


def calc_max_heights_to_left(heights: List):
    maxes = []
    for i in range(len(heights)):
        if i == 0:
            cur_max = 0
        else:
            cur_max = max(heights[i - 1], maxes[i - 1])
        maxes.append(cur_max)
    return maxes


if __name__ == '__main__':
    assert raindrop_accumulation([1, 0, 1]) == 1
    assert raindrop_accumulation([1, 0, 1, 0, 1, 0]) == 2
    assert raindrop_accumulation([1, 0, 3, 0, 2, 0, 1]) == 1 + 2 + 1
    assert raindrop_accumulation([1, 0, 3, 0, 2, 0, 1]) == 1 + 2 + 1
