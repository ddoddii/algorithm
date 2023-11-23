# 04. 거리두기 확인하기

def solution(places):
    return [check(place) for place in places]


def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            # 방향
    
            if cell != 'P': continue
            # right
            if idx_col < 4 and place[idx_row][idx_col+1] == 'P' : return 0
            if idx_col < 3 and place[idx_row][idx_col+1] != 'X'and place[idx_row][idx_col+2] == 'P' : return 0
            
            # down
            if idx_row < 4 and place[idx_row+1][idx_col] == 'P' : return 0
            if idx_row < 3 and place[idx_row+1][idx_col] != 'X' and place[idx_row+2][idx_col] == 'P' : return 0
            
            # diagonally right down
            if idx_row < 4 and idx_col < 4 and place[idx_row + 1][idx_col + 1] == 'P' and (place[idx_row][idx_col + 1] != 'X' or place[idx_row + 1][idx_col] != 'X'):
                return 0
            
            # diagonally left down
            if idx_col > 0 and idx_row < 4 and place[idx_row + 1][idx_col - 1] == 'P' and (place[idx_row + 1][idx_col] != 'X' or place[idx_row][idx_col-1] != 'X'):
                return 0
    return 1
