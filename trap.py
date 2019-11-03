'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''
def water_trapped(elevation_map, start, end):
    lower_point = min(elevation_map[start], elevation_map[end])
    distance = end - (start + 1)
    area_between_elevation = sum(elevation_map[start+1:end])
    #print(f'Data for => {start}:{end}')
    #print(f'Lowerst Point : {lower_point}')
    #print(f'Distance : {distance}')
    #print(f'Area Between Elevation : {area_between_elevation}') 
    trapped_water = lower_point * distance - area_between_elevation
    #print(f'Water Trapped : {trapped_water}')
    return trapped_water


def trap(height):
    highest_elevation = max(height)
    #print(f'Highest Elevantion : {highest_elevation}')
    number_of_elevations = len(height)
    total_trapped_water = 0
    i = 0
    j = 0
    while i < number_of_elevations:
        j =  i + 1
        while j < number_of_elevations:
            if height[i] > 0:
                if height[j] >= height[i]:
                    trapped_water = water_trapped(height, i, j)
                    total_trapped_water += trapped_water
                    i = j
                    break
                else:
                    j = j + 1
                    if j < number_of_elevations:
                        continue
                    else:
                        i = i + 1
                        break
            else:
                i = i + 1
                break

        if i == number_of_elevations - 1:
            break
        

    #print(f'Total Water Trapped : {total_trapped_water}')
    return total_trapped_water


if __name__ == "__main__":
    height_map = [4,2,3]
    result = trap(height_map)
    print('Trapped Water : {}'.format(result))
