import time

def merge(input_list,p,q,r):
	#p,q,rはそれぞれindex
	#p~q-1,q~rはsortされてい
	n1=q-p
	n2=r-q+1
	L=[]
	R=[]
	output_list=[]
	for i in range(n1):
		L.append(input_list[p+i])

	for j in range(n2):
		R.append(input_list[q+j])
	L.append(float("inf"))
	R.append(float("inf"))
	i=0
	j=0
	print("L {}".format(L))
	print("R {}".format(R))

	time.sleep(3)
	for k in range(n1+n2):
		if L[i]>R[j]:
			print(R[j])
			output_list.append(R[j])
			j+=1
		else:
			print(L[i])
			output_list.append(L[i])
			i+=1
	print("output_list {}".format(output_list))
	return output_list


if __name__=="__main__":
	#merge([1,2,3,1,6,123],0,3,5)
	merge([1,2,3,1,6,123],0,3,5)