
#Name      :       Abdalla Alzain Hamed Alzain

#        Id : 20220641

#    GAMAIL :  bdlllzn.@gmail.com

 #problem 3 task 2


def chek_winner(player ,point): 
    if point==0:
      print( player,"is win")

      
def is_squer(m):
    if int(m**0.5)==m**0.5:
        return True
    else:
       return False
    

    
N1=int(input("enter the number"))




while N1>0:
   player1=int(input(" player 1 .enter the number")) 
   while  not is_squer(player1) :
         player1=int(input(" player 1 .enter the squer number"))      
   N1=N1-player1
   print(N1)
   chek_winner("player1",N1)


   
   
   player2=int(input(" player 2 .enter the number")) 
   while  not is_squer(player2) :
         player2=int(input(" player 2 .enter the squer number"))
   N1=N1-player2
   print(N1)
   chek_winner("player2",N1)