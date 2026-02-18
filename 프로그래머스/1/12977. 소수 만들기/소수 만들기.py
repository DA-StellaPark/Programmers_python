def solution(nums):
    n = len(nums)
    answer = 0
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                total = nums[i] + nums[j] + nums[k]
                
                count = 0
                for s in range(1, total+1):
                    if total % s == 0:
                        count += 1
                        
                if count == 2:   # 소수일 때만
                    answer += 1
        
    return answer