
def insert_sort(input_list):
	print(len(input_list))
	if len(input_list)<=1:
		return input_list
	for i in range(len(input_list)-2,-1,-1):
		key=input_list[i]
		j=i
		while j<len(input_list)-1 and  input_list[j+1]<key:
			input_list[j]=input_list[j+1]
			j=j+1
			print(j)

		input_list[j]=key
	return input_list


if __name__=="__main__":
	print(insert_sort([32,123,43,1,4,11,4444,1,44444444444,333,123,1]))


