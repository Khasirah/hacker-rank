def transformSentence(sentence):
    # new sentence
    ns = []
    # previous sentence
    ps = ''
    # sentence counter
    sc = 0
    if len(sentence) == 1:
        return sentence
    
    for i in range(len(sentence)):
        if sc == 0:
            ns.append(sentence[i])
            ps = sentence[i]
            sc += 1
            continue
        if sentence[i] == ' ':
            ps = ''
            ns.append(' ')
            sc = 0
            continue
        if ps == '':
            continue
        if ps.lower() == sentence[i] or ps.lower() == sentence[i].lower():
            ns.append(sentence[i])
            ps = sentence[i]
            continue
        if ps.lower() < sentence[i].lower():
            ns.append(sentence[i].upper())
            ps = sentence[i]
            continue 
        if ps.lower() > sentence[i].lower():
            ns.append(sentence[i].lower())
            ps = sentence[i]
            continue 

    print(ns)

    return ''.join(ns)


if __name__ == "__main__":
    sentence = input()
    result = transformSentence(sentence)
    print(result)
