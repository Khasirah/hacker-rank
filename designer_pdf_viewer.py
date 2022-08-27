def designerPdfViewer(h,w):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # huruf tertinggi
    ht = 0 
    for huruf in w:
        # index huruf
        ih = alphabet.index(huruf)
        if h[ih] > ht:
            ht = h[ih]


    print(ht)

    return ht * len(w)

if __name__ == "__main__":
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    print(result)

