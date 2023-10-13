#Resolution 
print("The rule of Resolution:")
def resolution(lst_of_premises):
    #lst_of_premises = ['pVq','-pVr']
    #'qVr'
    print(lst_of_premises)
    if(lst_of_premises[0][0]==lst_of_premises[1][1] and lst_of_premises[0][1] == lst_of_premises[1][2]):
        lst_of_premises[0]='qVr'
        del lst_of_premises[1]
        print(lst_of_premises)
    else:
        print('not valid')

lst = ['pVq','-pVr']
resolution(lst)

print('#'*20)
print("The rule of Addition:")
#Addition  
def addition(lst_2):
    print(lst_2)
    if(lst_2[0][0]=='p'):
        lst_2[0]='pVq'
        print(lst_2)

lst_2 = ['p']
addition(lst_2)

print('#'*20)
print("The rule of Disjunction Syllogism :")
#disjunction syllogism 
def disjunction(lst_3):
    print(lst_3)

    if(lst_3[0][1]==lst_3[1][0] and lst_3[1][1]=='V'):
        lst_3[0]='q'
        del lst_3[1]
        print(lst_3)
    

lst_3 = ['-p','pVq']
disjunction(lst_3)
