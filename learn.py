if 5<10:
    print("try to know how indentaton works ")#this is an emple of what comment looks like
    print("can you now see that all the execution statements are ll on one line ")
    
    """
    you can use this for your multiline comment
    
    """
    
    
    student="mohammed mojeed ramadan"
    course ='MSC  Arthificial Intelligence'
    
    
    x=20
    print(x)
    
    
    y=int(41916254)
    print(type(y))
    
    x,y,z ="food","water",'house'
    print(z)
    
    
    lam=34
    girls=["shade",'tope','tayo','tade']
    first,second,third,fourth =girls #this process is called unpacking collection
    print(first + second)
    print(first,second,third,fourth) 
    #print(lam+first) #this will definitely return an error.
    
    
    x=34
    x=float(34)  
    
    print(x)
    
    
    
    import random
    print(random.randrange(100,3454))\
        
        #list
        
        
    thislist =['banaba','lesson','joy','office','lesson']
    print(len(thislist))
    
    
    code= list(('noises','ate'))
    print(code)
    
    
    
    pri = ['john','tayo','tolu',404,]
    for x in pri:
      print(pri[0])
      
      
    for a in range(len(pri)):
        print(pri[a])
        
        
social = ['facebook','instagram','twitter']

i=0#initialisation
while i< len(social):#condition
    print(social[i])
    i=i+1#iteration
    
A=30 
B=50 
print('two times hcairman of the local government i come frone') if( A>30) else print('fuck t')

print('jut have to be patient') if( B>A and (B-A == 20) ) else print('national treasurer')\
    
    
print('pay officers we have in the state') if(A < 100) or ( B > A) else print ("we are tryig to do more work")

if (B != 40):
    print('B is indedd not 40')
    


stet =('every', 'second','count','crazy')
a=0

while( a < 15):
    print('heloo darkness my old friwn')
a=a=1


class staffSalary:
    def _init_(self,admin,sec,account,manager,maintenance,IT,restaurant,director):
     self.admin=admin
     self.sec=sec
     self.account=account
     self.manager=manager
     self.maintenance=maintenance
     self.IT=IT
     self.restaurant=restaurant
     self.director=director
     #this now shows an already definedclass for the payment of salary for all the staffs in the company
     
     #lets now create an payment for january
     
january= staffSalary(200,80,150,320,140,270,70,300)

february = staffSalary(200,80,120,300,115,320,70,300)
March = staffSalary(200,80,150,320,1240,50,70,320)
print(january.sec)
print(March.IT)
print(february.maintenance)


""""
this would have been done in javascript as below:

function staffSalary(admin,sec,account,manager,maintenance,IT,restaurant,director){
    this.admin=admin;
    this.sec=sec;
    this.account=account;
    this.manager=manager;
    this.maintenance=maintenance
    this.IT= IT
    this.restaurant=restaurant
    this.directory=directory
    
}


let january =new staffSalary(20,30,40,50,60,70,80)
"""

     
     
     
     
    