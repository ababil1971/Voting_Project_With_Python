print("-----------Voting system design using python----------")

nom_1=input("Enter Nominee 1 Name: ")
nom_2=input("Enter Nominee 2 Name: ")

nom_1_vote=0
nom_2_vote=0

voter_ids=[1,2,3,4,5,6,7,8,9,10]
num_of_voters=len(voter_ids)

while True:
    if voter_ids==[]:
        print("Voting session has over.\nAnd The result is: ")
        if nom_1_vote>nom_2_vote:
            print(nom_1,"has won in election.")
        else:
            print(nom_2,"has won in election.")
        percent1=(nom_1_vote/num_of_voters)*100
        percent2=(nom_2_vote/num_of_voters)*100
        print(nom_1," got ",percent1,"% vote.")
        print(nom_2," got ",percent2,"% vote.")
        break
        
    
    else:
        voter_id=int(input("Enter your voter id: "))
        if voter_id in voter_ids:
            print("You are a voter.")
            vote= int(input("Enter your vote\n1 for Nominee 1\n2 for Nominee 2\nYour option here: "))
            if vote==1:
                nom_1_vote+=1
            elif vote==2:
                nom_2_vote+=1
            print("Thanks For Your Vote.")
            voter_ids.remove(voter_id)
        
        else:
            print("You are not a voter.\nOr already voted.")
            
            
            
            
            
            