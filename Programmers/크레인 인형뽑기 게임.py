"""
2019 카카오 개발자 겨울 인턴십
크레인 인형뽑기 게임
https://programmers.co.kr/learn/courses/30/lessons/64061
풀이1
"""
def solution(board, moves):
    def catch(col):
        if not dolls[col]:
            return 0
        doll = dolls[col].pop()
        
        if not bucket:
            bucket.append(doll)
            return 0
        
        elif doll == bucket[-1]:
            bucket.pop()
            return 2
        
        else:
            bucket.append(doll)
            return 0
    
    ans = 0
    N = len(board)
    dolls = [list() for _ in range(N)]
    bucket = []
    for col in range(N):
        for row in range(N - 1, -1, -1):
            if board[row][col] == 0:
                break
            dolls[col].append(board[row][col])
    
    for move in moves:
        ans += catch(move - 1)
    
    return ans
