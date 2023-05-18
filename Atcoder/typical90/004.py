# 004
H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
B=[[0]*W for _ in range(H)]
yoko=[sum(A[i]) for i in range(H)]
tate=[sum(i) for i in zip(*A)]

for i in range(H):
    for j in range(W):
        B[i][j]=yoko[i]+tate[j]-A[i][j]
        
    print(*B[i])