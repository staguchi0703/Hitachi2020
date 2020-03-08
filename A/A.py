# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\A\A_input.txt', 'r', encoding="utf-8")
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
S = input()

res = []
if len(S) % 2 == 1:
    print('No')
else:
    for i in range(len(S)//2):
        if i % 2 == 0:
            res.append(S[2*i:2*(i+1)])
    ans = set(res)
    
    if ans == {'hi'}:
        print('Yes')
    else:
        print('No')