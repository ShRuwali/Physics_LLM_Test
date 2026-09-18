## dictionary consisting of system prompts for text based problems


regular_keys=["Problem_1_Regular_Q","Problem_1_Obvious_Q","Problem_1_non_Obvious_Q",
              "Problem_2_Regular_Q","Problem_2_Obvious_Q","Problem_2_non_obvious_Q",
              "Problem_3_Regular_Q","Problem_3_Obvious_Q","Problem_3_non_obvious_Q",]

## All the keys above have the same values. Basically, for all the questions, the prompts are the same. These are simple prompts.
regular_system_prompts = dict.fromkeys(regular_keys,"You are a physics expert. Based on the question that is given solve the problem.")
print(regular_system_prompts)


## Problem_1_Regular_Q:You are a physics expert. Based on the question that is given solve the problem.
## Problem_1_Obvious_Q:"You are a physics expert. Based on the question that is given solve the problem.
## Problem_1_non_obvious_Q:"You are a physics expert. Based on the question that is given solve the problem.

## Problem_2_Regular_Q":"You are a physics expert. Based on the question that is given solve the problem
## Problem_2_Obvious_Q":"You are a physics expert. Based on the question that is given solve the problem
## Problem_2_non_obvious_Q":"You are a physics expert. Based on the question that is given solve the problem

## Problem_3_Regular_Q":"You are a physics expert. Based on the question that is given solve the problem
## Problem_3_Obvious_Q":"You are a physics expert. Based on the question that is given solve the problem.
## Problem_3_non_obvious_Q":"You are a physics expert. Based on the question that is given solve the problem.
            
          
detail_keys=["Problem_1_Obvious_Q","Problem_1_non_Obvious_Q",
              "Problem_2_Obvious_Q","Problem_2_non_obvious_Q",
              "Problem_3_Obvious_Q","Problem_3_non_obvious_Q",]

## Detail prompts for keys above. The promts are again the same.

detail_system_prompts = dict.fromkeys(detail_keys,"""You are a physics expert.
                                              Based on the question that is given solve the problem, 
                                              but if there are any physical laws broken then mention it and
                                              also say of the problem can be solved or not.""")
print(detail_system_prompts)


            
##"Problem_1_Obvious_Q":"You are a physics expert. Based on the question that is given solve the problem, but if there are any physical laws broken then mention it and also say of the problem can be solved or not.",
##"Problem_1_non_obvious_Q":"You are a physics expert. Based on the question that is given solve the problem, but if there are any physical laws broken then mention it.",

#"Problem_2_Obvious_Q":"You are a physics expert. Based on the question that is given solve the problem, but if there are any physical laws broken then mention it.",
#"Problem_2_non_obvious_Q":"You are a physics expert. Based on the question that is given solve the problem, but if there are any physical laws broken then mention it.",

#"Problem_3_Obvious_Q":"You are a physics expert. Based on the question that is given solve the problem, but if there are any physical laws broken then mention it.",
#"Problem_3_non_obvious_Q":"You are a physics expert. Based on the question that is given solve the problem, but if there are any physical laws broken then mention it.",
            
            