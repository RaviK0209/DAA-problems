def min_can(rating_list):
    n= len(rating_list)
    if n==0:
        return 0
    if n==1:
        return 1
    
    candies = [1]*n

    # LHS

    for i in range(1,n):
        if rating_list[i]> rating_list[i-1]:
            candies[i] = candies[i-1]+1

    #RHS
    for i in range(n-2,0,-1):
        if rating_list[i]>rating_list[i+1]:
            candies[i] = max(candies[i],candies[i+1]+1)

    return sum(candies)

    

rating_list=[1,2,3,2,1,4,3,2,1,2]
print(min_can(rating_list))