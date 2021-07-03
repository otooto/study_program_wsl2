n = 3

def hanoi(n,ffrom,to,work):

    if(n>1):
        hanoi(n-1,ffrom,work,to) #上からn-1段目の円盤を左側ffromから右側workへ移動
        print(ffrom + "から" + to + "に移動") #一番↓にある円盤を左側ffromから中央toに移動
        hanoi(n-1,work,to,ffrom) #上からn-1段目の円盤を右側workから中央toに移動
    else:
        print("再帰の終わり" + ffrom + "から" + to + "に移動")

hanoi(n,'a','b','c')

"""
プログラムとしては３ステップしかまずは書いてない。
だけど再帰で回すと、
１，ハノイ(n-1,a,c,b)
2, n番目の円盤をAからBへ
3. ハノイ(n-1,c,b,a)

を行う。

そして1を分解すると
1,ハノイ(n-2,a,b,c)
2,n-1番目の円盤をAからCへ
3,ハノイ(n-2,b,c,a)

また3を分解すると
1,1番目の円盤をAからBへ
だけ。ここで再帰をやめるポイントなのが3なのでハノイは行わない
"""