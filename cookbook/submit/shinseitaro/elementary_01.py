# 1. 1から10の整数をリストを`変数x`に格納して printしてください。ただし range 関数を使うこと。さらに全要素を2乗したリストを`変数y`に格納して printしてください。

def test():
    x = list(range(1,11))
    y = [i**2 for i in x]
    print(x)
    print(y)

if __name__ == "__main__":
    test()
