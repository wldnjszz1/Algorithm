movement = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
yesno = {True:'YES', False:'NO'}

def isNear(a, b):
        return ((a[0]-b[0], a[1]-b[1]) in movement)

def isExist(word, wordTable): # word : 찾을 단어
        prev = []
        for c in word:
                if c not in wordTable: return False
                # char exist in table. 키 값이 없으면 false

                # check if the word is neighbor of previous
                if len(prev) == 0: 
                        prev = (wordTable[c]) # first case, prev에 해당 키 값 넣기
                else: 
                        # 비교해서 movement안에 값이 있으면 
                        for nextLoc in wordTable[c]:
                                for prevLoc in prev:
                                        if isNear(nextLoc, prevLoc):
                                                prev=[nextLoc] 
                if len(prev) == 0: 
                        return False
        return True



for _ in range(int(input())): # 케이스 수 입력
        # Read board
        wordTable = {}
        for i in range(5): 
                strIn = input() # 5줄 5단어 입력
                for j in range(5):
                        if strIn[j] in wordTable:
                                wordTable[strIn[j]].append( (i,j) )
                        else:
                                wordTable[strIn[j]] = [(i,j)] #wordTable에 값이 존재하지 않으면, 각 알파벳에 행과 열 부여하기
        ''' 결과(wordTable) : 
        {'U': [(0, 0)], 'R': [(0, 1), (1, 2), (4, 3)], 'L': [(0, 2)], 'P': [(0, 3), (1, 1)], 'M': [(0, 4)], 
         'X': [(1, 0), (3, 0)], 'E': [(1, 3), (2, 3)], 'T': [(1, 4), (2, 4), (3, 1)], 'G': [(2, 0)], 'I': [(2, 1)], 
         'A': [(2, 2)], 'N': [(3, 2)], 'Z': [(3, 3)], 'Y': [(3, 4)], 'W': [(4, 0)], 'O': [(4, 1)], 'Q': [(4, 2)], 
         'S': [(4, 4)]}'''

        # Read words
        for _ in range(int(input())): # 우리가 알고있는 단어의 수 입력
                word = input() # 우리가 알고있는 단어의 수 만큼 찾을 단어 입력
                print(word, yesno[isExist(word, wordTable)])