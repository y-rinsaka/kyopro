D=int(input())
N=int(input())
L=[0]*(N)
R=[0]*(N)

# 前日比の配列
# D+2個用意するのは、日付に合わせていて、また最終日の翌日を-1する必要があるため
B=[0]*(D+2)
for i in range(N):
    L[i],R[i]=map(int, input().split())
    B[L[i]]+=1
    B[R[i]+1]-=1
    
# 累積和をとる（累計来場者数）
S=[0]*(D+2)
for d in range(1,D+1):
    # 前日の累計来場者数＋今日の来場者数
    S[d] = S[d-1] + B[d]
    print(S[d])
    
