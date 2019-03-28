def hash_func(num):
	#商を計算する
	return num//7

def insert_data(input_list,save_list):
	for ele in input_list:
		num=hash_func(ele)
		while save_list[num]!=None:
			num+=1
		save_list[num]=ele
	
	print(save_list)
	return save_list


if __name__=="__main__":
	tmp=[None]*16
	input_list=[81,20,45,62,89,66,42,70,44,51,31]
	insert_data(input_list,tmp)