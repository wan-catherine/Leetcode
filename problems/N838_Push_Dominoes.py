class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        if not dominoes:
            return dominoes
        length = len(dominoes)
        forces = []
        force = 0
        for i in range(length):
            if dominoes[i] == 'R':
                force = length
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces.append(force)
        print(forces)
        force = 0
        for i in range(length-1, -1, -1):
            if dominoes[i] == 'L':
                force = length
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        print(forces)
        res = []
        for i in forces:
            if i == 0:
                res.append('.')
            elif i < 0:
                res.append('L')
            else:
                res.append('R')

        return ''.join(res)

    # amazing!!!
    def pushDominoes_fast(self, dominoes):
        while True:
            new = dominoes.replace("R.L", "RuL")
            new = new.replace(".L", "LL")
            new = new.replace("R.", "RR")
            if dominoes == new:
                break
            else:
                dominoes = new
        return dominoes.replace("u", ".")

