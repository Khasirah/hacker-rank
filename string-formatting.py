def print_formatted(number):
    # your code goes here
    lj = len(bin(number)[2:])
    for i in range(1,number+1):
        j = oct(i)[2:]
        k = hex(i)[2:].upper()
        l = bin(i)[2:]
        print(f"{str(i).rjust(lj)}\t{j.rjust(lj)}\t{k.rjust(lj)}\t{l.rjust(lj)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)