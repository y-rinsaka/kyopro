# 002
from itertools import product

# bit全探索
# N個のものからいくつか選ぶ方法を全列挙して調べ上げることができる
def isvalid(S):
    score=0
    for c in S:
        if c=="(":
            score+=1
        else:
            score-=1

        if score<0:
            return False
    return (score==0)


# (:0 ):1
N=int(input())

# "(", ")"で構成された長さNの文字列の集合でforループ
# "ABC"と辞書順で入力すれば辞書順で返してくれる
for S in product('()', repeat=N):
    if (isvalid(S)):
        print(*S,sep="")


