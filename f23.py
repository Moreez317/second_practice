def f23(inputlist):

    firstlist = []

    for i in inputlist:
        if i not in firstlist:
            firstlist.append(i)

    listlenght = len(firstlist)

    def delete_emty():
        for x in range(listlenght):
            firstlist[x].remove(None)


    def delete_copy():
        for x in range(listlenght):
            firstlist[x].pop(2)

    def formating():
        for x in range(listlenght):
            buff = firstlist[x][0]
            firstlist[x][0] = buff[4:12]

            buff = firstlist[x][1]
            numcut = buff.find('[at]')
            firstlist[x][1] = buff[:numcut]

            buff = float(firstlist[x][2])
            buff = str(int(buff * 100)) + '%'
            firstlist[x][2] = buff

    def transpose():
        res = []
        n = len(firstlist)
        m = len(firstlist[0])
        for j in range(m):
            tmp = []
            for i in range(n):
                tmp = tmp + [firstlist[i][j]]
            res = res + [tmp]
        firstlist[:] = res

    delete_emty()
    delete_copy()
    formating()
    transpose()
    return firstlist

#mylist = [['775‐925‐6134', 'nezman4[at]gmail.com', '775‐925‐6134', None, '0.9'],
#                 ['025‐063‐4056', 'vabak74[at]yandex.ru', '025‐063‐4056', None, '0.8'],
#                 ['850‐070‐5382', 'vigukov76[at]gmail.com', '850‐070‐5382', None, '0.9'],
#                 ['950‐257‐0137', 'lofucic71[at]rambler.ru', '950‐257‐0137', None, '0.3'],
#                 ['950‐257‐0137', 'lofucic71[at]rambler.ru', '950‐257‐0137', None, '0.3'],
#                 ['950‐257‐0137', 'lofucic71[at]rambler.ru', '950‐257‐0137', None, '0.3']
#                ]

#print(f23(mylist))

