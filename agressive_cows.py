def can_place_cows(stalls,cows,min_dist):
    count=1
    last_position = stalls[0]
    for i in range(1,len(stalls)):
        if stalls[i]-last_position>=min_dist:
            count+=1
            last_position = stalls[i]
        if count==cows:
            return True
    return False
            
def agressive_cows(stalls,cows):
    stalls.sort()
    left=stalls[0]
    right=stalls[-1]-stalls[0]
    result=0
    while left<=right:
        mid= (left+right)//2
        if can_place_cows(stalls,cows,mid):
            result=mid
            left= mid+1
        else:
            right=mid-1
    return result


stalls=[1,2,4,8,9]
cows= int(input("enter no. of cows: "))
print(f"minimum distance possible is: {agressive_cows(stalls,cows)}")