#!usr/bin\env python3
# -*- conding: utf-8 -*-

def main():
    n = 4
    print(expon(n))

def expon(n):

    if n > 1:#nが1以上ならべき乗計算
        print(n)
        return n * expon(n-1)
    elif n == 1:#nが1ならそこで計算を終わりにする。再帰の終了地点
        print(n)
        return n
    else:#掛け算なので0は入っていけない。ここは本来はいらないけどプログラム的に入れてる。
        return 0


if __name__ == '__main__':
    main()