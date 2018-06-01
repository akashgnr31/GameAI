def result(game,depth):
	for i in range(0,N):
                horizontal=1
		vertical=1
		for j in range(0,N-1):
#checks horizontally
			if game[i][j]==game[i][j+1] and game[i][j]!=-1 and game[i][j+1]!=-1:
				k=game[i][j] 
				horizontal+=1
#checks vertically
			if game[j][i]==game[j+1][i] and game[j][i]!=-1 and game[j+1][i]!=-1:
				l=game[j][i]
				vertical+=1
#checking no of filled spaces	
		if horizontal==N:
			if k==maggu: 
				return -20
			elif k==chaapu:
				return 20
		elif vertical==N:
			if l==maggu : 
				return -20
			elif l==chaapu :
				return 20
#checking the diagonals straight
	j=0
	diagonal=1
	for i in range(0,N-1):
		if game[i][j]==game[i+1][j+1] and game[i][j]!=-1 and game[i+1][j+1]!=-1 :
			diagonal+=1
			k=game[i][j]
		j+=1
	if diagonal==N:
		if k==maggu:
			return -20
		elif k==chaapu:
			return 20
#checking the opposite diagonals
	j=0
	diagonal=1
	for i in range(0,N-1):
		if game[i][N-j-1]==game[i+1][N-j-2] and game[i][N-j-1]!=-1 and game[i+1][N-j-2]!=-1 :
			diagonal+=1
			k=game[i][j]
		j+=1
	if diagonal==N:
		if k==maggu:
			return -20
		elif k==chaapu:
			return 20

	return 0	
#checking the emptiness of the required space

def empty(i,j):
     if game[i][j]!=-1:
	return 1
     else:
	return 0		
			
#taking the input from input		
def usermove():
	while 1:
		i=input("Enter a row :")
		j=input("Enter a column :")
		if (i<=N and j<=N and i>=1 and j>=1):
			break
        return [i-1,j-1]
#Function to maximise the score
def maxmove(game,depth):
	if result(game,depth) :
		 return [result(game,depth),-1,-1]
	if depth>N*N:
		return [result(game,depth),-1,-1]
	maxm=[10000000,-1,-1]
	for p in range(0,N):
		for q in range(0,N):
			if empty(p,q)==1: 
				continue
			game[p][q]=maggu
			currentmove=minmove(game,depth+1)
			if currentmove[0]<maxm[0]:
				 maxm[0]=currentmove[0]
				 maxm[1]=p
				 maxm[2]=q
			game[p][q]=-1
	return maxm
#Function to minimise the score
def minmove(game,depth):
    	if result(game,depth):
		 return [result(game,depth),-1,-1]
	if depth>N*N:
		return [result(game,depth),-1,-1]

	minm=[-1000000,-1,-1]
	for m in range(0,N):	
		for n in range(0,N):
			if empty(m,n)==1:
				continue
			game[m][n]=chaapu
			currentmin=maxmove(game,depth+1)
			if currentmin[0]>minm[0]:
				minm[0]=currentmin[0]
				minm[1]=m
				minm[2]=n
			game[m][n]=-1
	return minm
	  
#main code			
N=3
game=[[0 for x in range(N)] for y in range(N)]
for i in range(0,N):
	for j in range(0,N):
		game[i][j]=-1; 
while 1:
	print("chaap ke no bol ko 0 ya 1 me se")
	chaapu=int(input())
	if chaapu==1:
		maggu=0
		break
	elif chaapu==0:
		maggu=1
		break

depth=1
while 1:
#to check the draw
	if depth>N*N:
		print("Draw")
		break
#user move
	mat=usermove()
	if game[mat[0]][mat[1]] != -1:
		continue
   	game[mat[0]][mat[1]]=chaapu
	for i in range(0,N):
		print(game[i])
#checking whether that user won or not 
	if result(game,depth)>0:
		print("You won")
		break
	depth+=1
#checking the Draw
	if(depth>N*N):
		print("Draw")
		break
#chance for computer to 
        mat=maxmove(game,depth)
	a=mat[1]	
	b=mat[2]
	print("computer is chosing the row as- "+str(a)+"  and column as- "+str(b))
	game[a][b]=maggu
#printing the game
	print("\n")
	for i in range(0,N):
		print game[i]
	if result(game,depth)<0:
     		print("haar gya tu")
		break
	elif result(game,depth)>0:
		print("jeeta hai tu")
		break
	elif depth>N*N:
		print("Draw ho to gya")
		break
	depth+=1
	



		
	
