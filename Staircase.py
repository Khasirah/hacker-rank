def stairCase(n):
    for i in range(n):
        noUrutTangga = i + 1
        banyakJarak = n - noUrutTangga
        banyakAnakTangga = n - banyakJarak
        print(" " * banyakJarak,"#" * banyakAnakTangga)

    # for i in range(0,n):
    #     for j in range(0,n):
    #         if i + j >= n-1:
    #             print("#",end='') 
    #         else:
    #             print(" ",end='')
    #     print("\r")

if __name__ == "__main__":
    n = int(input().strip())

    stairCase(n)
