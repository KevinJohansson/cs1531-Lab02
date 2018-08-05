def find_reverse(numbers):
    #find the reverse of the list
    return list(reversed(numbers))

def find_max(numbers):
    #find the maximum of the list
    return max(numbers)

def find_min(numbers):
    #find the minimum of the list
    return min(numbers)

def find_sum(numbers):
    #find the sum of all the numbers in the list
    return sum(numbers)

def find_average(numbers):
    #find the average of all the numbers in the list
    return (sum(numbers)/len(numbers))

def find_descending(numbers):
    #numbers sorted in descending order
    return list(sorted(numbers, reverse=True))

def second_smallest(numbers):
    #find the second smallest
	for result in numbers:
		num_smaller = 0
		for val in numbers:
			if (val < result):
				num_smaller += 1
		if (num_smaller == 1):
			return result



'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #find the kth smallest number in the list
	for result in numbers:
		num_smaller = 0
		for val in numbers:
			if (val < result):
				num_smaller += 1
		if (num_smaller == k-1):
			return result



