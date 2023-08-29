
'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.'''

def count_substring(string, sub_string):
    l1= len(string)
    l2= len(sub_string)
    i=0
    j=l2-1
    count=0
    while i<= (l1-l2+1):
        if string[i : j+1]== sub_string:
            count= count+1
        i=i+1
        j=j+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)