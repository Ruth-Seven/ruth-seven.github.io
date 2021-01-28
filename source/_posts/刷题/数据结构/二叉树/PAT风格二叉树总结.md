---
title: PAT风格二叉树总结
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-08-07 13:17:11
---

<!-- more -->



总结一下PAT出现的所有树的套路



## 前序中序转后序

```
int post[40], n, pos = 0;
vector<int> pre, in;
stack<int>s;
void dfs(int l1, int h1, int l2, int h2){
    if(l1 > h1) return;
    int k = l2;
    for(;in[k]!=pre[l1];k++);
    dfs(l1 + 1, l1 + k - l2, l2 , k - 1);
    dfs(l1 + k - l2 + 1, h1, k + 1, h2);
    post[pos++] = pre[l1];
}
int main(){
    int t;
    cin >> n;
    for(int i =0 ;i < 2 * n; i++){
        string a;
        cin >> a;
        if(a[1] == 'u'){
            cin >> t;
            s.push(t);
            pre.push_back(t);
        }else{
            in.push_back(s.top());
            s.pop();
        }
    }
    dfs(0, n - 1, 0, n - 1);
    for(int i = 0;i < n; i++){
        if(i == n - 1) cout << post[i];
        else cout << post[i] << ' ' ;
    }
}
```

## BST + CMT 转层序

```
int cbst[2000], n, pos = 1, in[2000];
int dfs(int u){
    if(u > n ) return 0;
    dfs(u * 2);
    cbst[u] = in[pos++];
    dfs(u * 2 + 1);
}
int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> in[i];
    }
    sort(in + 1, in + n + 1);
    dfs(1);
    for(int i = 1;i <= n; i++){
        if(i == n ) printf("%d", cbst[i]);
        else printf("%d ", cbst[i]);
    }
}
```

## 前序中序转后序

```
vector<int> in, post, pre;
int n, flag  = 1;
void dfs(int l1, int h1, int l2, int h2){
    if(l1 >= h1){
        if(l1 == h1) in.push_back(pre[l1]); // l1 > h1时 才能压入 否则是错误的
        return;
    }
    int k = l1 + 1;
    while(k <= h1 && pre[k] != post[h2 - 1]) k++;
    if(k == l1 + 1)
        flag = 0;
    dfs(l1 + 1, k - 1, l2, l2 + k - l1 - 2  );
    in.push_back(pre[l1]);
    dfs(k, h1, l2 + k - l1 - 1, h2 - 1 );
}
int main(){
    cin >> n;
    post.resize(n);
    pre.resize(n);
    for(int i = 0; i < n; i++) cin >> pre[i];
    for(int i = 0; i < n; i++) cin >> post[i];
    dfs(0, n - 1, 0 , n - 1);
    if(flag) cout << "Yes\n";
    else cout << "No\n";
    for(int i = 0; i < n; i++)
        if(i == n - 1) printf("%d\n", in[i]);
        else printf("%d ", in[i]);
}
```

## 层序中序转前序后序

这个问题也非常的巧妙，本来是一个层次遍历划分出一个父节点，但是下一步左右子树划分却成了问题，这个算法有一次刷新了我的世界观。使用中序遍历的思想，在层次遍历中查询每一个节点的归属父节点的左子树还是右子树

```
const ll mod = 1000000007;
int tree[40][2], val[40], n;
int  in[40];
vector<int> pre, post, lay;

int build(vector<int> lay, int l, int r){
    if(l > r) return 0;
    int k = 1;
    while(lay[0] != in[k]) k++;
    vector<int> llay, rlay;
    for(int i = 1;i < lay.size(); i++){
        int isl = 0;
        for(int j = l; j< k; j++)
        if(lay[i] == in[j]){
            isl = 1;
            break;
        }
        if(isl) llay.push_back(lay[i]);
        else rlay.push_back(lay[i]);
    }
    pre.push_back(in[k]);
    tree[k][0] =  build(llay, l, k - 1);
    tree[k][1] =  build(rlay, k + 1, r);
    post.push_back(in[k]);
    return k;
}
int main(){
    cin >> n;
    lay.resize(n);
    int root = 0;
    for(int i = 0;i < n; i++) cin >> lay[i];
    for(int i = 0;i < n; i++) cin >> in[i + 1];
    root = build(lay, 1, n);
    for(int i = 0;i < n;i++)
        if(i == n - 1) printf("%d\n", pre[i]);
        else printf("%d ", pre[i]);
    for(int i = 0;i < n;i++)
        if(i == n - 1) printf("%d\n", post[i]);
        else printf("%d ", post[i]);
}
```

## 判断完全二叉树

```
int tree[200][2], n, ingree[200], root, lastnood, flag = 1;
int bfs(int u){
    int tn = 1;
    queue<int> que;
    que.push(u);
    while(que.size()){
        int v = que.front(); que.pop();
        lastnood = v;
        if(tree[v][0] == -1){
            if(tn != n)
                flag = 0;
        }else{
            que.push(tree[v][0]);
            tn++;
        }
        if(tree[v][1] == -1){
            if(tn != n)
                flag = 0;
        }else{
            que.push(tree[v][1]);
            tn++;
        }
    }
}

int main(){
    fill(tree[0], tree[0] + 200 * 2 , - 1 );
    cin >> n;
    for(int i = 0;i < n; i++) {
        string a, b;
        cin >> a >> b;
        if(a != "-"){
            int v = atoi(a.c_str());
            tree[i][0] = v;
            ingree[v] ++;
        }
        if(b != "-") {
            int v = atoi(b.c_str());
            tree[i][1] = v;
            ingree[v] ++;
        }
    }
    for(int i = 0; i < n ;i++) if(ingree[i] == 0) root = i;
    bfs(root);
    if(flag) cout << "YES " << lastnood;
    else cout << "NO " << root;

}
```

## 静态链表建树

```
int tree[2000][3], lay[2000], n, depest, ct = 0;
int insert(int u, int val, int dep){
    depest = max(depest,dep);
//    cout << u << endl;
    if(u == 0){
        lay[dep] ++;
        tree[++ct][2] = val;
        return ct;
    }else if(val <= tree[u][2]){
        tree[u][0] = insert(tree[u][0], val, dep + 1);
    }else if(val > tree[u][2]){
        tree[u][1] = insert(tree[u][1], val, dep + 1);
    }
    return u;
 }
 int main()
 {
     int root = 0, tmp;
     cin >> n;
     for(int i = 0;i < n;i++){
        cin >> tmp;
        root = insert(root, tmp, 1);
     }
     cout << lay[depest ] << " + " <<  lay[depest - 1] << " = " <<  lay[depest] + lay[depest - 1] << endl;
 }
```

## 判断树

晴神的一道题1016

```
int tree[100][3], val[40], n,  ingree[20];
int navln, layer[23], isct = 1, switime;
stack<int> s;
//avl
int ctavl(int root){
    if(root == 0) return 0;
    int h1 = ctavl(tree[root][0]);
    int h2 =  ctavl(tree[root][1]);
    if( abs(h1 - h2) > 1) navln ++;
    return max(h1, h2) + 1;
}
//层序遍历同时存储 逆层序遍历的顺序以便调整堆！
void isctree(int root){
    int nt = 1;
    queue<int> que, lay;
    que.push(root);
    lay.push(1);
    while(que.size()){
        int u = que.front(); que.pop();
        int ll = lay.front(); lay.pop();
        s.push(u);
        layer[ll] ++;
//        cout << u << endl;
        if( tree[u][0] ){
            que.push(tree[u][0]);
            lay.push(ll + 1);
            nt ++;
        }else if(nt != n) isct = 0;
        if( tree[u][1] ){
            que.push(tree[u][1]);
            lay.push(ll + 1);
            nt ++;
        }else if(nt != n) isct = 0;
    }
}
// 向下调整 大顶堆
void downAdjust(int root){
    for(int p = tree[root][0];p !=0; p = tree[root][0]){
        int pp = tree[root][1];
        if(val[pp] > val[p]) p = pp;
        if(val[p] < val[root]) break;
        swap( val[root], val[p]);
        switime ++;
        root = p;
    }
}
int main(){
    string s1, s2;
    cin >> n;
    for(int i = 0;i < n; i++){
        cin >> val[i];
    }
    for(int i = 1;i <= n; i++){
        cin >>  s1 >> s2;
        if(s1 != "-"){
            tree[i][0] = atoi(s1.c_str());
            ingree[atoi(s1.c_str())]++;
        }
        if(s2 != "-"){
            tree[i][1] = atoi(s2.c_str());
            ingree[atoi(s2.c_str())]++;
        }
    }
    int rt = -1;
    for(int i = 0;i < n; i++)
        if( ingree[i] == 0) rt = i;
//    cout << rt ;
    ctavl(rt);
    if(navln != 0) cout << "NOT AVL TREE!!!\n" <<  navln << endl;
    else{
        isctree(rt);
        int p = 1, noden = 1;
        while(noden == layer[p]){
            noden *= 2;
            p++;
        }
        if(!isct) cout << "NOT COMPLETE TREE!!!\n" << p - 1 << endl;
        else{
            while(s.size()){
                int u = s.top(); s.pop();
                downAdjust(u);
            }
            cout << "OHHHHH HEAP!!!\n" << switime << endl;
        }
    }
}
```