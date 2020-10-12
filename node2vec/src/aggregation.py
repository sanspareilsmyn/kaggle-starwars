import numpy as np

def special_case():
    flag = 0
    txt = open('../output/interaction_feat.txt', 'r')
    s1 = list()
    for e in txt:
        tmp = list(e.split())
        s1.append(tmp[0])
    s1.pop(0)

    txt2 = open('../output/mentions_feat.txt', 'r')
    s2 = list()
    for e in txt2:
        tmp = list(e.split())
        s2.append(tmp[0])
    s2.pop(0)

    special_case = list()
    if len(s1) > len(s2):
        flag = 1
        for e in s1:
            if e not in s2:
                special_case.append(e)
    elif len(s1) < len(s2):
        flag = 2
        for e in s2:
            if e not in s1:
                special_case.append(e)

    return flag, special_case

def aggregate(flag, sc):
    result = list()

    txt1 = open('../output/interaction_feat.txt', 'r')
    s1 = list()
    for e in txt1:
        tmp = list(map(float, e.split()))
        s1.append(tmp)
    s1.pop(0)

    txt2 = open('../output/mentions_feat.txt', 'r')
    s2 = list()
    for e in txt2:
        tmp = list(map(float, e.split()))
        s2.append(tmp)
    s2.pop(0)

    # Exception Handling
    special_case = list()
    if len(sc):
        for e in sc:
            if flag == 1:
                for i in s1:
                    if i[0] == e:
                        special_case.append(i)
                        s1.remove(i)
                        break

            elif flag == 2:
                for i in s2:
                    if i[0] == e:
                        special_case.append(i)
                        s2.remove(i)
                        break
    special_case = np.array(special_case).flatten()
    result.append(special_case.tolist())

    #print(result)
    # Averaging
    for i in s1:
        for j in s2:
            if i[0] == j[0]:
                a = np.array(i)
                b = np.array(j)
                tmp = (a+b)/2
                result.append(tmp.tolist())

    for e in result:
        print(e)

    line = open('../output/aggregated_feat.txt', 'w')
    for r in result:
        for e in r:
            line.write('{}{}'.format(e, ' '))
        line.write('\n')
    line.close()

if __name__ == "__main__":
    f, sc = special_case()
    sc = [int(i) for i in sc]
    aggregate(f, sc)
