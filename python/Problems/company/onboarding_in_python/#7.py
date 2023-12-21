# 친구 추천
from collections import defaultdict



def getUserFriend(friends, user):
    usr_friend = []
    
    for friend in friends:
        a = friend[0]
        b = friend[1]
        
        if a == user:
            usr_friend.append(b)
        if b == user:
            usr_friend.append(a)
    return usr_friend


def getFriendScore(friends, usr_friend, user):
    
    friend_score = {}
    
    for friend in friends:
        a = friend[0]
        b = friend[1]
        
        if a in usr_friend and b != user:
            friend_score[b] = friend_score.get(b,0) + 10
        if b in usr_friend and a != user:
            friend_score[a] = friend_score.get(a,0) + 10
            
    return friend_score

def updateFriendScore(visitors, usr_friend, friend_score):

    for visitor in visitors:
        if visitor not in usr_friend:
            try:
                friend_score[visitor] += 1
            except KeyError:
                friend_score[visitor] = 1

    return friend_score


def solution(user, friends, visitors):
    
    usr_friend = getUserFriend(friends, user)
    friend_score = getFriendScore(friends, usr_friend, user)
    visitor_friend_score = updateFriendScore(visitors, usr_friend, friend_score)

    recommend_friend_score = {name : score for name , score in visitor_friend_score.items() if name not in usr_friend and name != user}

    topFriend = []
    for name, score in recommend_friend_score.items():
        if score > 0:
            topFriend.append((name, score))

    topFriend.sort(key=lambda x: (-x[1], x[0]))

    answer = [name for name, _ in topFriend]
    return answer

user = "mrko"
friends = [ ["donut", "andole"], ["donut", "jun"], ["donut", "mrko"], ["shakevan", "andole"], ["shakevan", "jun"], ["shakevan", "mrko"] ]
visitors = ["bedi", "bedi", "donut", "bedi", "shakevan"]

print(solution(user, friends, visitors))