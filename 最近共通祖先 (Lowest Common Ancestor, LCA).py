#0-index
class LcaDoubling:
    """
    links[v] = { (u, w), (u, w), ... }  (u:隣接頂点, w:辺の重み)
    というグラフ情報から、ダブリングによるLCAを構築。
    任意の2頂点のLCAおよび距離を取得できるようにする
    """
 
    def __init__(self, n, links, root=0):
        self.depths = [-1] * n
        self.distances = [-1] * n
        prev_ancestors = self._init_dfs(n, links, root)
        self.ancestors = [prev_ancestors]
        max_depth = max(self.depths)
        d = 1
        while d < max_depth:
            next_ancestors = [prev_ancestors[p] for p in prev_ancestors]
            self.ancestors.append(next_ancestors)
            d <<= 1
            prev_ancestors = next_ancestors
 
    def _init_dfs(self, n, links, root):
        q = [(root, -1, 0, 0)]
        direct_ancestors = [-1] * (n + 1)  # 頂点数より1個長くし、存在しないことを-1で表す。末尾(-1)要素は常に-1
        while q:
            v, p, dep, dist = q.pop()
            direct_ancestors[v] = p
            self.depths[v] = dep
            self.distances[v] = dist
            q.extend((u, v, dep + 1, dist + w) for u, w in links[v] if u != p)
        return direct_ancestors
 
    def get_lca(self, u, v):
        du, dv = self.depths[u], self.depths[v]
        if du > dv:
            u, v = v, u
            du, dv = dv, du
        tu = u
        tv = self.upstream(v, dv - du)
        if u == tv:
            return u
        for k in range(du.bit_length() - 1, -1, -1):
            mu = self.ancestors[k][tu]
            mv = self.ancestors[k][tv]
            if mu != mv:
                tu = mu
                tv = mv
        lca = self.ancestors[0][tu]
        assert lca == self.ancestors[0][tv]
        return lca
 
    def get_distance(self, u, v):
        lca = self.get_lca(u, v)
        return self.distances[u] + self.distances[v] - 2 * self.distances[lca]
 
    def upstream(self, v, k):
        i = 0
        while k:
            if k & 1:
                v = self.ancestors[i][v]
            k >>= 1
            i += 1
        return v
    
n, m = 6, 5
G = [[(1, 2), (5, 6)], [(0, 2), (2, 3), (4, 5)], [(1, 3), (3, 4)], [(2, 4)], [(1, 5)], [(0, 6)]]
lca = LcaDoubling(n, G)
