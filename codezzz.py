import sys
input = sys.stdin.read

def main():
    data = input().split()
    n:int = int(data[0])
    arr:list[int] = []
    for i in range(1,n+1):
        arr.append(int(data[i]))
    
    sum:int = 0
    sum_arr:list[int] = []
    for i in range(1,n+1):
        sum+=int(data[i])
        sum_arr.append(sum)
        
    i = n+1
    while i < len(data):
        a,b = int(data[i]),int(data[i+1])
        i+=2
        if a == 0:
            print(sum_arr[b])
        else:
            print(sum_arr[b]-sum_arr[a-1])
    
if __name__ == "__main__":
    main()