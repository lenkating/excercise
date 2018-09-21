ourcards=[7,2,9,4,3,1,6,5,8]
j = 1


while j < 9:
	card = ourcards[j]
	i = j-1
	while i >= 0 and ourcards[i] > card:
	          ourcards[1+i] = ourcards[i]
	          i = i-1
	ourcards[i+1] = card
	j = j+1
print(ourcards)



