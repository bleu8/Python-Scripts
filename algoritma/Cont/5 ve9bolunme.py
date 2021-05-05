for i in range(1,101):
    if i %5 ==0 and i%9==0:
        print(f"{i }hem 9 hem 5e bolunuyo")

    elif i %5==0 or i%9==0:
        print(f" {i} ikisinden birine bolunuyo")

    else:
        print("hicbiri")

