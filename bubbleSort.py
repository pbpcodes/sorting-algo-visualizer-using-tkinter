import time


def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]  #swapped the values
                drawData(data, ['orange' if x==j or x==j+1 else "violet" for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, ['orange' for x in range(len(data))])