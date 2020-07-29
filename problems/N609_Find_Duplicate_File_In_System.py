import collections


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_dict = collections.defaultdict(list)
        for path in paths:
            sub_paths = path.split(' ')
            dir = sub_paths[0]
            for file in sub_paths[1:]:
                index = file.index('(')
                file_name, content = file[:index], file[index:]
                content_dict[content].append(dir + "/" + file_name)

        res = [v for k, v in content_dict.items() if len(v) > 1]
        return res
