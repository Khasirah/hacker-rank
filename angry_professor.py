def angryProfessor(k,a):
    # siswa datang tidak telat
    sdtt = len(list(filter(lambda tp: tp <= 0, a)))
    if sdtt < k:
        return "YES"
    
    return "NO"

if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k,a)
        print(result)
