"""
- 하나의 딕셔너리에 모든 정보를 담으려 하지 말자.
- key : (value1, value2) 형태로도 저장 가능하다.
- enumerate(zip(value1, value2)) 를 적극활용하자.
- 변수 이름을 명확하게 짓자 ! 
"""


def solution(genres, plays):
    info = {}  # 장르 별 정보 -{장르 : (인덱스, 재생 수)}
    gens = {}  # 가장 많이 저장된 장르 - {장르 : 총 재생 수}

    for idx, (gen, play) in enumerate(zip(genres, plays)):
        if gen not in info:
            info[gen] = [(idx, play)]
        else:
            info[gen].append((idx, play))
        gens[gen] = gens.get(gen, 0) + play

    answer = []
    for (gen, _) in sorted(gens.items(), key=lambda item: item[1], reverse=True):
        for (idx, _) in sorted(info[gen], key=lambda item: item[1], reverse=True)[:2]:
            answer.append(idx)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
