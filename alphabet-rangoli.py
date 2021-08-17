import string
def print_rangoli(size):
    # your code goes here
    # membuat list alphabet nya
    alphabet = list(string.ascii_lowercase)
    # mencari panjang
    panjang = len('-'.join(alphabet[n-1::-1] + alphabet[1:n]))

    # perulangan mencetak setiap baris
    
    for i in range(1, n):
        print('-'.join(alphabet[n-1:n-i:-1] + alphabet[n-i:n]).center(panjang,'-'))
    for i in range(n,0,-1):
        print('-'.join(alphabet[n-1:n-i:-1] + alphabet[n-i:n]).center(panjang,'-'))    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)