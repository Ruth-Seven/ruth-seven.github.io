---
title: AVL
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
categories:
date: 2020-08-07 12:26:38
---



老模板了



```c++
/** This is Code of JJ

Problem      :AVL tree
Source       :
Solution     :
AnyDetial    :

DateAndTime  :5,18
CostofTime   :17:07

**/
#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;

struct Node{
    int data, height;
    Node *lchild, *rchild;
    Node(int x)
    {
        data = x;
        height = 1;
        lchild = NULL;
        rchild = NULL;
    }
};
int getHeight(Node *root)
{
    if(!root) return 0;//! child node may be is NULL.
    else return root->height;
}
int getHeightFactor(Node *root)
{
    return getHeight(root->lchild) - getHeight(root->rchild);
}
void updateHeight(Node *root)
{
    root->height = max(getHeight(root->lchild),getHeight(root->rchild)) + 1;//!!! add 1
}

void search(Node *root, int x)
{
    if(!root) return;
    if(root->data==x)
    {
        printf("%d\n",x);
    }
    else if(root->data>x)
    {
        search(root->lchild,x);
    }
    else  search(root->rchild,x);
}

//! right rotate
void r_rotate(Node *&root)
{
    cout<<"R\n";
    Node* tmpr = root->lchild;
    root->lchild = tmpr->rchild;
    tmpr->rchild = root;
    updateHeight(root);//!!!update the height of tree
    updateHeight(tmpr);
    root = tmpr;
}
//! left rotate
void l_rotate(Node *&root)///!!! left rotating replace root with root's right child.
{
    cout<<"L\n";
    Node* tmpr = root->rchild;
    root->rchild = tmpr->lchild;
    tmpr->lchild = root;
    updateHeight(root);//!!!update the height of tree
    updateHeight(tmpr);
    root = tmpr;

}

void insert(Node *&root, int x)
{
    if(root==NULL)
    {
        root  = new Node(x);;
        return;
    }
    else if(root->data>x)
    {
        insert(root->lchild,x);
    }else{
        insert(root->rchild,x);
    }
    //!!you should update the weight after changing the number or the height of root and child;
    updateHeight(root);
    if(getHeightFactor(root)==2)
    {
        if(getHeightFactor(root->lchild)==1)
        {
            r_rotate(root);//!!! change the root
        }else if(getHeightFactor(root->lchild)==-1)
        {
            l_rotate(root->lchild);
            r_rotate(root);//!!! change the root
        }
    }
    else if(getHeightFactor(root)==-2)
    {
        if(getHeightFactor(root->rchild)==-1)
        {
            l_rotate(root);//!!! change the root
        }
        else if(getHeightFactor(root->rchild)==1)
        {
            r_rotate(root->rchild);
            l_rotate(root);//!!! change the root
        }
    }
}
 Node *create(int a[], int n)
 {
     Node * root = NULL;
     for(int i=0;i<n;i++)
     {
         insert(root,a[i]);
     }
     return root;
 }

 void preorder(Node *root)
 {
     if(!root) return;
     printf("%d ",root->data);
     preorder(root->lchild);
     preorder(root->rchild);
 }
 void pr(Node *root)
 {
     if(!root) return;
     printf("data: %3d   h:%d\n",root->data,root->height);
     pr(root->lchild);
     pr(root->rchild);
 }
int main()
{
    int a[10]={1,2,3,4,5,6,7,8,9,10};
    Node *root = create(a,10);
//    preorder(root);
    pr(root);

}
```

