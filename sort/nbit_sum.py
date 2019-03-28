#alogrithm introduction　practice 2.1-4
def nbit_sum(list1,list2):
	if len(list1)!=len(list2):
		raise Exception("ミス")
	n=len(list1)
	output_list=[0]*(n+1)
	prev=0
	for i in range(len(list1)):
		tmp=list1[i]+list2[i]+prev
		
		if tmp<2:
			output_list[i]=tmp
			prev=0
		else :
			resid=tmp%2
			output_list[i]=resid
			prev=1
	
	output_list[-1]=prev
	print("{} + {} = {}".format(list1,list2,output_list))
	return output_list
if __name__=="__main__":
	output=nbit_sum([1,0,1],[1,1,1])
	#print(output)

