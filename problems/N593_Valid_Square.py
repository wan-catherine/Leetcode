class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        nodes = set()
        nodes.add(tuple(p1))
        nodes.add(tuple(p2))
        nodes.add(tuple(p3))
        nodes.add(tuple(p4))
        if len(nodes) < 4:
            return False
        def get_side_length(node1, node2):
            return (node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2

        l = [get_side_length(p1, p2), get_side_length(p1, p3), get_side_length(p1, p4)]
        l.sort()
        if l[0] != l[1] or l[0] + l[1] != l[2]:
            return False

        l1 = [get_side_length(p1, p2), get_side_length(p2, p3), get_side_length(p2, p4)]
        l1.sort()
        if l1[0] != l1[1] or l1[0] + l1[1] != l1[2]:
            return False

        l2 = [get_side_length(p1, p3), get_side_length(p2, p3), get_side_length(p3, p4)]
        l2.sort()
        if l2[0] != l2[1] or l2[0] + l2[1] != l2[2]:
            return False
        return True