# 003
N = int(input())
# G[0]→頂点0がどこと接続しているかのリスト
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1  # 0-indexed に
    # 双方向に接続
    G[a].append(b)
    G[b].append(a)

# 頂点 s から DFS (ここではスタックを使う)
def dfs(s):
    # 頂点 s からの距離
    dist = [-1] * N
    # 自身は0
    dist[s] = 0

    # スタックで DFS
    st = [s]
    while st:
        # 末尾を取得し削除
        v = st.pop()
        # vと接続されている頂点の集合G[v]の各要素について
        for nv in G[v]:
            # 距離がセットされていなかったら
            if dist[nv] == -1:
                # スタックに頂点を追加し
                st.append(nv)
                # sからnvまでの距離は、sからvまでの距離に1足したものである
                dist[nv] = dist[v] + 1

    # sからの距離リストを返す
    return dist

# 頂点 0 から
dist0 = dfs(0)
# mv: dist0のうち、最大距離（最大値）をもつものの頂点（インデックス）の一つ
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
# その頂点について再びdfsして木の中での最大距離を求める
distmv = dfs(mv)
print(max(distmv) + 1)