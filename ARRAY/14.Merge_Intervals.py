"""
 Merge Intervals ---- Leet Code

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
def Merge_Intervals(intervals):
    """ |---| (1,3)                                                     | Now we should join
          |-----| (2,6) <-----Here we can see that 2-6 overlaps         | |------| (1,6)
                    |---|(8,10)                                         |              |---|(8,10)
                            |----|(15,18)                               |                       |----|(15,18)
    """
    if intervals is []:
        return []

    result = []
    intervals.sort()
    print("Intervels",intervals)
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1] , interval[1])

    return result

if __name__ == "__main__":
   intervals = [[1,3],[2,6],[8,10],[15,18]] 
   result = Merge_Intervals(intervals)
   print(result)