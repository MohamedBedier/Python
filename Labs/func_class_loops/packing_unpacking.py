# ##############################################################
# ##############################################################
# #                                                         
# # @file    : Lec3_Lab5
# # @version : 1.00  
# # @brief   : Function packing ,unpacking arguments trainings
# # @author  : MOHAMED BEDIER MOHAMED                                                                                                            
# #                                                                                                       
# ##############################################################
# ##############################################################

# define a tuple
mytuple = ('GO', 'JS' ,'C#')

# define a dictionary
myskills = {
      'GO': "60%",
      'JS' : '80%',
      'HTML' : "30%"
}

# the implementation of the function
def show_skills (name,*skills,**skillsWithProgress):
    print(f"hello {name} \nskills without progress is ")
    # loop in the tuple
    for skill in skills :
        print(f"- {skill}")
        
    print(f"skills with progress is ")   
     # loop in the dictionary 
    for skill_key , skill_value in  skillsWithProgress.items():  

        print(f"- {skill_key} ===> {skill_value}")
        
# call the function
show_skills("mohemd",*mytuple,**myskills)

# another calling
show_skills("mohemd","c","python","c++", python = "60%")