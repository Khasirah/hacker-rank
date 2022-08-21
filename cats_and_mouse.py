def catAndMouse(x, y, z):
    d_xz = x-z if (x-z) > 0 else -1*(x-z)
    d_yz = y-z if (y-z) > 0 else -1*(y-z)
    
    if d_xz == d_yz:
        return "Mouse C"

    if d_xz > d_yz:
        return "Cat B"

    return "Cat A"

if __name__ == "__main__":
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        print(result)
