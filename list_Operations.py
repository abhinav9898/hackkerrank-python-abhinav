def insertele(ind, ele, l2):
    l2.insert(ind, ele)
    return l2
def removele(ele, l2):
    l2.remove(ele)
    return l2
def appendele(ele, l2):
    l2.append(ele)
    return l2

if __name__ == '__main__':
    N = int(input())
    l2= []
    for i in range(0, N):
        l1=[]
        userInput= input()
        l1= list(map(str, userInput.split()))
        if l1[0]== "insert":
            l2= insertele(int(l1[1]), int(l1[2]), l2)
        elif l1[0]== "remove":
            l2= removele(int(l1[1]), l2)
        elif l1[0]== "append":
            l2= appendele(int(l1[1]), l2)
        elif l1[0]== "print":
            print(l2)
        elif l1[0]== "sort":
            l2.sort()
        elif l1[0]== "pop":
            l2.pop()
        elif l1[0]== "reverse":
            l2.reverse()