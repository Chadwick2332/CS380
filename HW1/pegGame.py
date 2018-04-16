class PegGame:
    def __init__(self, m=4, n=4):
        self.m = m
        self.n = n
        self.numPegs = m * n
        self.start = 9
        self.boardState = None

    def createGrid(self):
        self.boardState = (pow(2, self.numPegs) - 1) - pow(2, self.start)
        return self.boardState

    def goal(self, state=None):
        if state == None:
            state = self.boardState

        # if there is one instance of '0' and it is in index self.start
        if state == pow(2, self.start):
            return True
        else:
            return False

    def applyRule(self, rule, state=None):
        # ---------------------
        # | 15 | 14 | 13 | 12 |
        # ---------------------
        # | 11 | 10 | 09 | 08 |
        # ---------------------
        # | 07 | 06 | 05 | 04 |
        # ---------------------
        # | 03 | 02 | 01 | 00 |
        # ---------------------

        # -----------------
        # | O | X | X | X |
        # -----------------
        # | X | X | O | O |
        # -----------------
        # | O | O | X | X |
        # -----------------
        # | X | X | X | O |
        # -----------------

        # Up:           [14, 10, 06] x-m
        # Down:         [01, 05, 09] x+m
        # Left:         [11, 10, 09] x-1
        # Right:        [04, 05, 06] x+1
        # Up-Right:     [13, 10, 07] x-m+1
        # Up-Left:      [10, 05, 00] x-m-1
        # Down-Right:   [02, 05, 08] x+m-1
        # Down-Left:    [05, 10, 15] x+m+1

        if state == None:
            state = self.boardState

        binState = format(state, '0' + str(self.numPegs) + 'b')

        try: # Check Peg values
            if binState[(self.numPegs - 1) - rule[0]] == '1' and state[(self.numPegs - 1) - rule[1]] == '1' and state[(self.numPegs - 1) - rule[2]] == '0':
                if (rule[0] - rule[1]) - rule[1] == rule[2] and (rule[0] - rule[1]) == self.m: #up
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
                elif (rule[1] - rule[0]) + rule[1] == rule[2] and (rule[0] + rule[1]) == self.m: #down
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
                elif (rule[0] - rule[1]) - rule[1] == rule[2] and (rule[1] - rule[0]) == 1: #left
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
                elif (rule[1] - rule[0]) + rule[1] == rule[2] and (rule[0] - rule[1]) == 1: #right
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
                elif (rule[0] - rule[1]) - rule[1] == rule[2] and (rule[0] - rule[1]) == self.m + 1: #up-right
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
                elif (rule[0] - rule[1]) - rule[1] == rule[2] and (rule[0] - rule[1]) == self.m - 1: #up-left
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
                elif (rule[0] - rule[1]) + rule[1] == rule[2] and (rule[0] - rule[1]) == self.m - 1: #down-right
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
                elif (rule[0] - rule[1]) + rule[1] == rule[2] and (rule[0] - rule[1]) == self.m + 1: #down-left
                    self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
                    return self.boardState
        except IndexError:
            print "Invalid Arguement"





    # display reference numbers for board
    def refBoard(self):
        print '-' * (5 + (self.m * 4))
        print '|',
        for peg in reversed(range(self.numPegs)):
            print str(peg).zfill(2) + ' |',

            if peg % self.m == 0:
                print ''
                print '-' * (5 + (self.m * 4))
                if peg != 0:
                    print '|',

    # display numbers for board
    def displayBoard(self):
        for i, peg in enumerate(format(self.boardState, '0' + str(self.numPegs) + 'b')):
           if int(i) % self.m == 0:
                print ''
                print '-' * (5 + (self.m * 3))
                if peg != 0:
                    print '|',

           if peg == '1':
               print 'X |',
           elif peg == '0':
               print 'O |',

        print ''
        print '-' * (5 + ((self.m - 1) * 4))
def main():
    game = PegGame()
    # game.boardState = '0000001000000000b'
    game.createGrid()
    print game.goal(512)
    game.refBoard()
    # print game.goal()
    game.displayBoard()


if __name__ == '__main__':
    main()