# a = [2, 3, 5, 9, 3,]
# print(sum(a[1::2]))


# a=[2,3,4,5,6]
# new_list=[]
# for i in range(len(a)+1//2):
#     new_list.append(a[i]*a[len(a)-1-i])
# print(new_list[0:3])


# a = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in a:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)  
# print(max-min)



n= int(input("Введите n: "))
def k(n):

	if(n > 1):
		
		k(n//2)
	
	print(n%2, end=' ')
	
if __name__ == '__main__':
	k(n)
	print("\n")
	