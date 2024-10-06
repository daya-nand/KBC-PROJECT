#  KBC 😂😂😂
quetions=[
    ["Which of the three banks will be merged with the other two to create India’s third-largest bank?","punjab national bank","indian bank","dena bank","bank of baroda",2,]
    ,
    ["The world’s nation 5G mobile network was launched by which country?","japan","asia","south korea","malaysia",3]
    ,
    ["Vijay Singh (golf player) is from which country?","UK","USA","India","Faji",3]
    ,
    ["The green planet in the solar system is?","mars","uranus","venus","earth",2]
    ,
    [" At which place on earth are there days & nights of equal length always?","eqautor","poles","prime meridian","nowhere",1]
]

money =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000]
print ("sawagat hai aap sabhi ka kon banega crorepati me ") 
"\n"
for i in range(0,len(quetions)):

    quetion=quetions[i]
    print(quetions[i][0])
    print ("a)",quetions[i][1],"b)",quetions[i][2])
    print ("c)",quetions[i][3],"d)",quetions[i][4])
    ans =int(input("give your ans in 1 to 4 for quit enter 0 :: "))
    if ans == quetions[i][5]:
        print ("correct answer")
        print(f"congratulation you won {money[i]} rupees")
        print("here is your next question")
    elif ans ==0:
        print("thank you for play this game" )
        print(f"you won {money[i-1]}")
        break
    else:
        print ("Sorry aapka ans galat hai isliye aap aage nhi khel skte 😥")
        print(f"your money  {money[i]}")
        break
print("thank you 😍😍")