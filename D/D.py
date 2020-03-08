# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
import numpy as np
N, T = [int(item) for item in input().split()]

shop_list = np.array([[int(item) for item in input().split()] for _ in range(N)])
inf = float('inf')
dp = np.array([[[inf for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)])

dp[1:,1] = [1 for _ in range(N+1)]


for i in range(N):
    for j in range(1, N):
        dp[i,j+1] = dp[i, j] * shop_list[i, 0] + shop_list[i, 1] + 1 
        dp[i, j+1, j] = inf
print(dp)

