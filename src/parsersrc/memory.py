class Memory:
    def __init__(self):
        self.mem = []

    def store(self, ch, value):
        for i in range(len(self.mem)):
            if self.mem[i][0] == ch:
                self.mem[i] = [ch, value]
                return
        self.mem.append([ch, value])

    def get(self, ch):
        for item in self.mem:
            if item[0] == ch:
                return item[1]

