H,W=map(int, input().split())
X=[list(map(int, input().split())) for i in range(H)]
Q=int(input())

#配列Zの初期化（累積和をとるため）
Z=[[0]*(W+1) for _ in range(H+1)]

#横方向に累積和
#注意：ZはXより手前に1行1列多い
for i in range(1,H+1):
    for j in range(1,W+1):
        Z[i][j]=Z[i][j-1]+X[i-1][j-1]

#縦方向に累積和
for i in range(1,H+1):
    for j in range(1,W+1):
        Z[i][j]=Z[i-1][j]+X[i-1][j-1]

for q in range(Q):
    A,B,C,D=map(int, input().split())
    print(Z[C][D] + Z[A-1][B-1] - Z[A-1][D] - Z[C][B-1])

