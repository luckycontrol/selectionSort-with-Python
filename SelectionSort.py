import random

def fill_array(array, num):
    for i in range(num):
        array.append(random.randint(1, num))

def sort(array):
    for i in range(len(array)):
        min = i //let i be minimum element's index
        for j in range(i+1, len(array)):
            if array[min] > array[j] :
                min = j   
        array[i],array[min] = array[min],array[i]
        
def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
        if i != 0 and i % 10 == 0:
            print('')

def run():
    array = []
    num = int(input("배열의 원소 갯수를 입력하세요: "))

    fill_array(array, num)
    sort(array)
    print_array(array)

if __name__ == '__main__':
    run()
