#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

#Example:

#high_and_low("1 2 3 4 5")  # return "5 1"
#high_and_low("1 2 -3 4 5") # return "5 -3"
#high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
	nums = []
	i = 0
	while i < len(numbers):
		if numbers[i] == '-':
			nums.append(int(numbers[i+1])*-1);
			i+=1
		elif numbers[i].isdigit():
			nums.append(int(numbers[i]))
		i+=1
	return str(max(nums)) + " " + str(min(nums))

print high_and_low("1 2 3 4 5")
print high_and_low("1 9 3 4 -5")
print high_and_low("1 2 -3 4 5");