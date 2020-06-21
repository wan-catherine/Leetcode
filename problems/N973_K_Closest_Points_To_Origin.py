import collections


class Solution(object):
    def kClosest_my_solution(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        d_points = {}
        for point in points:
            key = point[0] ** 2 + point[1] ** 2
            d_points.setdefault(key, []).append(point)

        res = []
        keys = sorted(d_points.keys())
        while K > 0:
            for key in keys:
                points_num = len(d_points[key])
                if K >= points_num:
                    res.extend(d_points[key])
                    K -= points_num
                else:
                    res.extend(d_points[key][:K])
                    K = 0
        return res

    # learn about sort method
    # learn about lambda
    def kClosest_other_fast_solution(self, points, K):
        points.sort(key = lambda x : x[0] ** 2 + x[1] ** 2)
        return points[:K]

    # bucket sort
    # because point[0]**2 + point[1]**2 maybe very large.
    # the range [min_distance, max_distance] maybe very large
    def kClosest_timeout(self, points, K):
        if not points:
            return []
        distance_points_mapping = collections.defaultdict(list)
        min_distance = points[0][0] ** 2 + points[0][1] ** 2
        max_distance = 0
        for point in points:
            key = point[0] ** 2 + point[1] ** 2
            min_distance = min(min_distance,key)
            max_distance = max(max_distance, key)
            distance_points_mapping[key].append(point)
        res = []
        while min_distance <= max_distance:
            length = len(distance_points_mapping[min_distance])
            if K >= length:
                K -= length
                res.extend(distance_points_mapping[min_distance])
                min_distance += 1
            else:
                res.extend(distance_points_mapping[min_distance][:K])
                break
        return res

