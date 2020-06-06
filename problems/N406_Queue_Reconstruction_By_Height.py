class Solution(object):
    # from small to large
    # the method nees to take care of duplicated number
    # o(n**2)
    def reconstructQueue_slow(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return people

        p_len = len(people)
        order = [0] * p_len
        people.sort(key=lambda x : x[0])
        for person in people:
            count = 0
            flag = person[1]
            for i in range(p_len):
                if count == flag and not order[i]:
                    break
                if order[i]:
                    if order[i][0] == person[0]:
                        count += 1
                    else :
                        continue
                else:
                    count += 1

            order[i] = person
        return order

    # for height : large to small
    # for count : small to large
    # then insert, so we can always use the count to find the right position to insert
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output