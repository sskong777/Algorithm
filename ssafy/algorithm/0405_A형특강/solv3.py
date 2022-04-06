def func1(n):
    if n ==5:
        return
    print(n)
    func1(n-1)
    print(n)


func1(10)