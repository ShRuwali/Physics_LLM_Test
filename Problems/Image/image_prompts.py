## dictionary for regular prompts and system prompts 

problem_1_keys = ["Problem_1_Regular_Q", "Problem_1_Obvious_Q", "Problem_1_non_obvious_Q"]
prompt_1= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the total time taken by the block to travel 5 meters."
                     " All the necessary values required are given in the picture."                                           
)

dict_1 = dict.fromkeys(problem_1_keys , prompt_1)
                ##########################################################################################
                ##########################################################################################

problem_2_keys = ["Problem_2_Regular_Q", "Problem_2_Obvious_Q", "Problem_2_non_obvious_Q"]
prompt_2= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the time period of oscillation for small displacements."
                     " All the necessary values required are given in the picture."  
)

dict_2 = dict.fromkeys(problem_2_keys , prompt_2)
                ##########################################################################################
                ##########################################################################################                                

problem_3_keys = ["Problem_3_Regular_Q", "Problem_3_Obvious_Q", "Problem_3_non_obvious_Q"]
prompt_3= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the velocity of the solid sphere (a rigid body) at the bottom of"
                     " the plane using conservation of energy given that the solid sphere rolls without slipping and starts rolling from rest"
                     " unless mentioned."
                     " All the necessary values required are given in the picture."  
)

dict_3 = dict.fromkeys(problem_3_keys , prompt_3)

                ##########################################################################################
                ##########################################################################################

problem_4_keys = ["Problem_4_Regular_Q", "Problem_4_Obvious_Q", "Problem_4_non_obvious_Q"]
prompt_4= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the tension in the string at the bottom the the circle."
                     " All the necessary values and conditions required are given in the picture."  
)

dict_4 = dict.fromkeys(problem_4_keys , prompt_4)

                ##########################################################################################
                ##########################################################################################

problem_5_keys = ["Problem_5_Regular_Q", "Problem_5_Obvious_Q", "Problem_5_non_obvious_Q"]
prompt_5= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the velocity of block A after the collision."
                     " All the necessary values and conditions required are given in the picture."  
)

dict_5 = dict.fromkeys(problem_5_keys , prompt_5)

                ##########################################################################################
                ##########################################################################################

problem_6_keys = ["Problem_6_Regular_Q", "Problem_6_Obvious_Q", "Problem_6_non_obvious_Q"]
prompt_6= ("You are a physics expert."
                     " From the figure provide a brief description. From Fig (a) calculate the force constant of the spring."
                     " The spring in Fig (a) is now replaced with a block as shown in Fig (b). Calculate the angular frequency"
                     " and the frequecy of the oscillation. In both the cases the force required is proportional to the displacement of the spring."
                     " All the necessary values and conditions required are given in the picture."  
)

dict_6 = dict.fromkeys(problem_6_keys , prompt_6)

                    ##########################################################################################
                    ##########################################################################################

problem_7_keys = ["Problem_7_Regular_Q", "Problem_7_Obvious_Q", "Problem_7_non_obvious_Q"]
prompt_7= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the tension (T) in the cable."
                     " All the necessary values required are given in the picture."  
)

dict_7 = dict.fromkeys(problem_7_keys , prompt_7)

                        ##########################################################################################
                        ##########################################################################################

problem_8_keys = ["Problem_8_Regular_Q", "Problem_8_Obvious_Q", "Problem_8_non_obvious_Q"]
prompt_8= ("You are a physics expert."
                     " From the figure provide a brief description and calculate gravitational force between the two bodies on each other"
                     " at the distance which is given in the figure. Consider both the bodies to be spherically symmetric."
                     " All the necessary values required are given in the picture."  
)

dict_8 = dict.fromkeys(problem_8_keys , prompt_8)

regular_system_prompt = {**dict_1, **dict_2, **dict_3, **dict_4, **dict_5, **dict_6, **dict_7, **dict_8}
print(regular_system_prompt)


## Create a set of detail prompts

detail_system_prompt= {}
for key, value in regular_system_prompt.items():
    detail_system_prompt[key] = value + (" But if there are any physical laws broken then mention it and"
                                                  " also say of the problem can be solved or not." )

## remove these keys as there are no detail prompts for these regular question
remove_keys = ["Problem_1_Regular_Q","Problem_2_Regular_Q","Problem_3_Regular_Q", 
               "Problem_4_Regular_Q","Problem_5_Regular_Q","Problem_6_Regular_Q",
                "Problem_7_Regular_Q","Problem_8_Regular_Q" ]
 

for key in remove_keys:
    detail_system_prompt.pop(key, None)     

print(detail_system_prompt)