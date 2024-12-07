def getDiffSum():
    with open("day1input.txt", 'r') as file:
        lines = file.readlines()
        list1, list2 = [], []
        for x in lines:
            line = x.split()
            list1.append(line[0])
            list2.append(line[-1])
        list1.sort()
        list2.sort()
        sum = 0
        for i in range(len(list1)):
            diff = abs(int(list1[i]) - int(list2[i]))
            sum += diff
        return sum
    
def getSimmilarityScore():
    with open("day1input.txt", 'r') as file:
        lines = file.readlines()
        list1, list2 = [], []
        for x in lines:
            line = x.split()
            list1.append(line[0])
            list2.append(line[-1])
        list1.sort()
        list2.sort()
    simScore = 0
    for i in range(len(list1)):
        simScore += int(list2.count(list1[i])) * int(list1[i])
    return simScore

print(getDiffSum(), getSimmilarityScore())