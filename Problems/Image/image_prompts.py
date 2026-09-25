## dictionary for regular prompts and system prompts 

problem_1_keys = ["Problem_1_Regular_Q", "Problem_1_Obvious_Q", "Problem_1_non_Obvious_Q"]
prompt_1= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the total time taken by the block to travel 5 meters."
                     " All the necessary values required are given in the picture."                                           
)

dict_1 = dict.fromkeys(problem_1_keys , prompt_1)


problem_2_keys = ["Problem_2_Regular_Q", "Problem_2_Obvious_Q", "Problem_2_non_Obvious_Q"]
prompt_2= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the time period of oscillation for small displacements."
                     " All the necessary values required are given in the picture."  
)

dict_2 = dict.fromkeys(problem_2_keys , prompt_2)


problem_3_keys = ["Problem_3_Regular_Q", "Problem_3_Obvious_Q", "Problem_3_non_Obvious_Q"]
prompt_3= ("You are a physics expert."
                     " From the figure provide a brief description and calculate the velocity of the solid sphere (a rigid body) at the bottom of"
                     " the plane using conservation of energy given that the solid sphere rolls without slipping and starts rolling from rest"
                     " unless mentioned."
                     " All the necessary values required are given in the picture."  
)

dict_3 = dict.fromkeys(problem_1_keys , prompt_3)


regular_system_prompt = {**dict_1, **dict_2, **dict_3}
print(regular_system_prompt)


## Create a set of detail prompts

detail_system_prompt= {}

for key, value in regular_system_prompt.items():
    detail_system_prompt[key] = value + ("But if there are any physical laws broken then mention it and"
                                                  " also say of the problem can be solved or not." )

print(detail_system_prompt)

        