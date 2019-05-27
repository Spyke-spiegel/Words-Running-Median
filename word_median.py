import statistics
import os

nb = []
result = open('wc_result.txt', 'w+')
folderPath = './wc_input/'

#Iterating iver every file in the folder wc_input
for file in os.listdir(folderPath):
    filename = os.fsdecode(file)
    print("file find in the folder Input = " + filename)
    data = open(folderPath + filename, "r")
    result.write("\n%s\n" %(filename))

    for line in data:
        #Preparing the data for the treatment
        line = line.rstrip().rstrip('.').rstrip(',')
        wds = line.split()
        #Treating the Data
        a = [len (wds)]
        for b in a:
            nb.extend(a)
            r = statistics.median(nb)
        #Writing the data in the file wc_result.txt
        result.write("%s %s %s\r" % (line, a, r) )





    # result.write("%s: %s\r\n" % (wds, r))