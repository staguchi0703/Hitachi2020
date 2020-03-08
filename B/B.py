# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\B\B_input.txt', 'r', encoding="utf-8")
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
import collections
A, B, M = [int(item) for item in input().split()]
A_list = [int(item) for item in input().split()]
B_list = [int(item) for item in input().split()]
M_list = [[int(item) for item in input().split()] for _ in range(M)]

res_list = collections.deque()

for a, b, c in M_list:
    res_list.append(A_list[a-1] + B_list[b-1] - c)

res_list.append(min(A_list) + min(B_list))

print(min(res_list))
