# 001
N,L=map(int, input().split())
K=int(input())
A=list(map(int, input().split()))

# x以上に分けることは可能かをcheck
def check(x):
    # 達成回数
    num=0
    
    # 一つ前の切れ目
    pref=0
    
    for i in range(N):
        if A[i]-pref >= x:
            num+=1
            pref=A[i]
    
    # ラスト一回を忘れず
    if L-pref>=x:
        num+=1
    
    return (num>=K+1)

# 最大となるx（スコア）は何かを二分探索する（最小の最大化）
def binary_search(left, right):
    while right-left>1:
        # はじめは真ん中から
        middle=(left+right)//2
        # middle以上に分けることができれば
        if check(middle):
            left=middle
        else:
            right=middle
    return left

print(binary_search(-1, L+1))