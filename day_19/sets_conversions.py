def unique_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.add((min(num, diff), max(num, diff)))
        seen.add(num)
    return list(pairs)


nums = [1,3,5,7,9,11]
target =2

print(unique_pairs(nums,target))




def distinct_subsequences(nums):
    subsequences = set()  # This set will store unique subsequences as tuples.
    
    def backtrack(start, current):
        subsequences.add(tuple(current))  # Convert the list 'current' to a tuple and add it to the set.
        
        for i in range(start, len(nums)):  # Loop from 'start' index to the end of 'nums'.
            current.append(nums[i])  # Add the current element to the current subsequence.
            backtrack(i + 1, current)  # Recursively call 'backtrack' with the next starting index.
            current.pop()  # Remove the last element to backtrack and explore other subsequences.
    
    backtrack(0, [])  # Start backtracking from index 0 with an empty subsequence.
    return [list(seq) for seq in subsequences]  # Convert each tuple back to a list.

nums = [1,2,3,4,5,6,7,8]

print(distinct_subsequences(nums))



def subsets(numbers):

	if numbers == []:
		return [[]]
	x = subsets(numbers[1:])

	return x + [[numbers[0]] + y for y in x]

# wrapper function
def subsets_of_given_size(numbers, n):
	return [x for x in subsets(numbers) if len(x)==n]

if __name__ == '__main__':
	numbers = [1, 2, 3, 4]

	n = 3
	print(subsets_of_given_size(numbers, n))



def refact (n):
      if n==0:
          return 1
      else:
            p = n*refact(n-1)
      return p

print(refact(6))

def generate(n):
      t = []
      lol =[[]for i in  range(n**n)]
      helper(n,t,lol)
      return (lol)

def helper(n,t,lol):
      global j
      if len(t)==n:
            lol[j] = lol[j]+t
            j+=1
            return
      for i  in  range(1,n+1):
            t.append(i)
            helper(n,t,lol)
            t.pop()


j=0
l = generate(3)
print(l)
     
      


