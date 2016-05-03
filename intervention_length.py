
def get_IL_info(document):
    document = document.split("\n")
    count_words = 0
    max_IL = 0
    total_lines = len(document)
    for line in document:
        line = line.split()
        count_words += len(line)
        if len(line) > max_IL:
            max_IL = len(line)
    mean_IL = float(count_words) / len(document)
    return [mean_IL, max_IL, len(document)]


##all_mean_IL=[]
##all_total_IL=[]
##all_max_IL=[]
##for document in masterlist:
##    mean_IL, max_IL, total_IL = get_IL_info(document[1])
##    all_mean_IL.append(mean_IL)
##    all_max_IL.append(max_IL)
##    all_total_IL.append(total_IL)
##
##for i in range(1,10):
##    print masterlist[i][0], "Mean IL:", all_mean_IL[i], "Total # lines:", all_total_IL[i], "Max IL:", all_max_IL[i]



