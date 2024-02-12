# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    input_nums = map(int, input().split())
    print(hash(tuple(input_nums)))
