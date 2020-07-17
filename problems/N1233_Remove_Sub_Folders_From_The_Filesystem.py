class Solution(object):
    def removeSubfolders_double_for(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = [folder[0]]
        for f in folder[1:]:
            flag = True
            for t in res:
                if f.startswith(t + "/"):  # must add "/" , or test_removeSubfolders_2 will be failed!!!
                    flag = False
                    break
            if flag:
                res.append(f)
        return res

    """
    The reason why we don't need to loop res is the folder is sorted !
    """
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = [folder[0]]
        pre = res[-1] + "/"
        for f in folder[1:]:
            if f.startswith(pre):
                continue
            pre = f + "/"
            res.append(f)
        return res
