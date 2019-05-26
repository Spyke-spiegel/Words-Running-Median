import statistics

filename = './wc_input/words.txt'
file = open(filename, 'r')
dic =dict()
nb = []
result = open('wc_result.txt', 'w+')

for line in file:
    line = line.rstrip().rstrip('.').rstrip(',')
    wds = line.split()
    a = [len (wds)]
    print (a)
    for b in a:
        nb.extend(a)
        print(nb)
        r = statistics.median(nb)
        print (r)
    result.write("%s\r %s\r %s\r\n" % (line, a, r) )



    # result.write("%s: %s\r\n" % (wds, r))