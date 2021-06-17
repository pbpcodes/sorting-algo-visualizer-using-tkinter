import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, colorArray(len(data), head, tail, border, border))
    time.sleep(timeTick) 

    for j in range(head,tail):
        if(data[j] < pivot):
            drawData(data, colorArray(len(data), head, tail, border, j,True))
            time.sleep(timeTick) 
            data[border], data[j] = data[j], data[border]
            border+=1
        drawData(data, colorArray(len(data), head, tail, border, j))
        time.sleep(timeTick) 

    # swapping pivot elements with border value 
    drawData(data, colorArray(len(data), head, tail, border, tail,True))
    time.sleep(timeTick) 
    data[border], data[tail] = data[tail], data[border]
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIndex = partition(data,head,tail, drawData, timeTick)

        # left partition

        quick_sort(data,head, partitionIndex-1, drawData, timeTick)

        # right partition

        quick_sort(data, partitionIndex+1, tail, drawData, timeTick)

def colorArray(dataLen, head, tail, border, currIndex, isSwap = False):
    colorArray = []
    for i in range(dataLen):

        #the base color

        if i>= head and i<= tail:
            colorArray.append("grey")
        else:
            colorArray.append("white")

        if i==tail:
            colorArray[i] == 'orange'
        elif i==border:
            colorArray[i] == 'red'
        elif i==currIndex:
            colorArray[i] == 'yellow'

        if isSwap:
            if i == border or i ==currIndex:
                colorArray[i] = 'green'
    return colorArray
