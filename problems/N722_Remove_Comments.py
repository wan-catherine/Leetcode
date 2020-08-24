class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        self.unfinished = ''
        self.flag = False
        self.res = []

        for line in source:
            if self.flag:
                self.process_incomment(line)
            else:
                self.process_not_incomment(line)
        return self.res

    def add_line(self, line):
        self.unfinished = ''
        if line:
            self.res.append(line)

    def process_not_incomment(self, line):
        l_index = line.find('/*')
        index = line.find('//')
        if l_index == index == -1:
            self.add_line(self.unfinished + line)
            return
        if index != -1 and (l_index == -1 or index < l_index):
            self.add_line(self.unfinished + line[:index])
            return
        self.flag = True
        self.unfinished += line[:l_index]
        self.process_incomment(line[l_index + 2:])

    def process_incomment(self, line):
        r_index = line.find('*/')
        if r_index == -1:
            return
        self.flag = False
        self.process_not_incomment(line[r_index+2:])




