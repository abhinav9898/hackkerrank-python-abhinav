#In Python, a string can be split on a delimiter.

def split_and_join(line):
    # write your code here
    l1= list(map(str, line.split(" ")))
    line= "-".join(l1)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)