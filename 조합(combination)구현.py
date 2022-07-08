# combinations 내장함수 직접 구현..

def get_comb(arr, n):
    combinations = []
    if n == 0:
        return [[]]
    for i in range(0, len(arr)):
        front = arr[i]
        back = arr[i+1:]
        for c in get_comb(back, n-1):
            combinations.append([front]+c)
    return combinations

def comb(population,num):
	ans = []
    ## 정의된 값인지 확인한다.
	if num > len(population): return ans
	## Base Case
	if num == 1:
		for i in population:
			ans.append([i])
    ## General Case
	elif num>1:
		for i in range(len(population)-num+1): ## i가 시작하는 값 = len(population) - (n-1)이고 이 때 n은 lst로부터 추출할 개수와 같다.
			for temp in comb(population[i+1:],num-1):
				ans.append([population[i]]+temp)

	return ans

arr = [1, 2, 3, 4]
print(get_comb(arr, 2))
print(comb(arr, 2))
