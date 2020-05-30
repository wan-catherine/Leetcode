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
