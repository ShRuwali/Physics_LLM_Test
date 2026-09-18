## dictionary consisting of system prompts for image based problems

## dictionary for regular prompts for the 9 problems
from textwrap import dedent
regular_system_prompts = {
                "Problem_1_Regular_Q": """You are a physics expert. 
                                    From the figure provide a brief description and calculate the total time taken by the block to travel 5 meters""",

                "Problem_1_Obvious_Q":"""You are a physics expert.
                                    From the figure provide a brief description and calculate the total time taken by the sphere to travel 5 meters,
                                    given there is rolling with no slipping""",

                "Problem_1_non_Obvious_Q":"""You are a physics expert.
                                    From the figure provide a brief description and calculate the total time taken by the sphere to travel 5 meters,
                                    given there is rolling with no slipping""",


                "Problem_2_Regular_Q":"""You are a physics expert.
                                    From the figure provide a brief descriptin and calculate the time period of oscillation for small displacement""",

                "Problem_2_Obvious_Q":"""You are a physics expert.
                                    From the figure provide a brief description and calculate the time period of oscillation for small displacement""",

                "Problem_2_non_Obvious_Q":"""You are a physics expert.
                                    From the figure provide a brief descrption and calculate the time period of oscillation for small displacement""",


                "Problem_3_Regular_Q":"""You are a physics expert.
                                    From the figure provide a brief descrption and calculate the velocity of the solid sphere (a rigid body) at the 
                                    bottom of the plane using conservation of energy, given that the solid sphere rolls without slipping""",
                                        
                "Problem_3_Obvious_Q":"""You are a physics expert.
                                    From the figure provide a brief descrption and calculate the velocity of the solid sphere (a rigid body) at the 
                                    bottom of the plane using conservation of energy, given that the solid sphere rolls without slipping""",

                "Problem_3_non_Obvious_Q":"""You are a physics expert.
                                    From the figure provide a brief descrption and calculate the velocity of the solid sphere (a rigid body) at the 
                                    bottom of the plane using conservation of energy, given that the solid sphere rolls without slipping""",

}

print(regular_system_prompts)


## Create a set of detail prompts

detail_system_prompts= {}

for key, value in regular_system_prompts.items():
    detail_system_prompts[key] = value + """ but if there are any physical laws broken then mention it and
                                                  also say of the problem can be solved or not"""



print(detail_system_prompts)


            

            