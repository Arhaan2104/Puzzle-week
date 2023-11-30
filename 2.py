# Given list of likes/dislikes
likes_dislikes = [38, 24, 8, -36, -63, 48, -5, 70, 23, 58, -93, 82, 31, 55, -28, -83, 89, 60, 86, -10, 39, -35, -92, -69, 54, -48, 88, -20, 56, -62, -66, 45, 46, -80, -53, -70, -82, 83, -87, -29, 64, 81, -19, 29, 3, 85, -67, -97, 27, -46, 67, -96, 36, 94, -4, -78, -73, -89, -18, 28, -61, 12, 61, -64, 14, 40, 52, 68, 18, -11, 21, -12, 76, 6, -68, -3, -33, -75, -88, -25, 65, 79, 62, 26, -55, -90, -59, -37, 41, -71, 49, 74, -98, -14, -7, -52, -51, -27, -81, 42, 87, 98, -76, 50, 30, -91, -57, 5, 44, 93, -60, 91, -94, -65, 7, 66, -22, -74, -41, -49, 69, -84, 34, -43, 71, -13, 57, -31, -79, -39, -56, -99, 43, 20, -24, 75, -100, 33, 25, -16, -85, -95, 1, -86, 53, -47, -30, 4, 97, 90, 11, 78, 92, 0, 99, 13, -15, 96, -17, 84, 63, -8, -6, 47, 51, 80, -38, 9, -23, -1, -72, 22, 19, 16, 35, 32, -9, -42, -54, 77, 95, 2, 59, -77, -45, -26, -44, -2, -32, -34, -21, 37, -58, 10, -40, 15, 72, 17, -50, 73]

# This problem is essentially the maximum subarray sum problem, 
# which can be solved efficiently using Kadane's algorithm.

def max_subarray_sum(arr):
    max_so_far = arr[0]
    current_max = arr[0]

    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        max_so_far = max(max_so_far, current_max)

    return max_so_far

# Calculate the maximum total utility
max_total_utility = max_subarray_sum(likes_dislikes)
max_total_utility
