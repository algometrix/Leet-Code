'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''

def water_trapped(height):
    total_water_trapped = 0
    water = [0] * len(height) 
    for index, h in enumerate(height):
        max_left = max(height[:index]) if len(height[:index])  != 0 else 0
        max_right = max(height[index:]) if len(height[index:])  != 0 else 0
        min_height = min(max_left, max_right)
        #print(f'Max Left {index} : {max_left}')
        #print(f'Max Right {index} : {max_right}')
        water[index] = min_height - h if min_height - h >=0 else 0

    #print('Water Map')
    #print(water)
    return sum(water)


if __name__ == "__main__":
    height_map = [4,2,3]
    result = water_trapped(height_map)
    print('Trapped Water : {}'.format(result))
