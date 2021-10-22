q_ans = {
    "3a-1" : 0.0, 
    "3a-2" : 3.3,
    "3a-3" : 0.0,
    "3a-4a" : 3.3,
    "3a-5" : 0.0,
    "3b-2" : 1000.0,
    "3c-1a-soft" : 0.0,
    "3c-1b-soft" : 3.3,
    "3c-1c-soft" : (2.0/3.0)*3.3,
    "3c-2a-soft" : (2.0/3.0)*3.3,
    "3c-2b-soft" : (1.0/3.0)*3.3,
    "3c-1a-hard" : 0.0,
    "3c-1b-hard" : 3.3,
    "3c-1c-hard" : (2.0/3.0)*3.3,
    "3c-2a-hard" : (2.0/3.0)*3.3,
    "3c-2b-hard" : (1.0/3.0)*3.3
}

# {
#   question_id: (
#     correct_answer_explanation,
#     wrong_answer_explanation
#   )
# }
# If there is no explanation, use None
q_exp = {
    "3a-1" : (
        "The multimeter is measuring the voltage across a single node (ground in this case), which is 0V.",
        "The multimeter is measuring the voltage across a single node (ground in this case). What is the voltage at gound?"
    ),
    "3a-2" : (
        "We're measuring across the voltage source, which is 3.3V.",
        "Think about what component we're measuring across!"
    ),
    "3a-3" : (
        "Since we're looking at an open circuit, we know that no current flows through R1. Thus, by Ohm's Law, the voltage drop across R1 must be 0.",
        "Hint: this is an open circuit! Think about what current and Ohm's law."
    ),
    "3a-4a" : (
        "As established in Step 3, there's no voltage drop across R1. Thus, the voltage at node 2 must be the same as that of the voltage source. The voltage at node 0 is the ground node, which means that the measured voltage will be Vz = V2 - V0 = 3.3V - 0V = 3.3V.",
        "Look back in the previous steps - what is the voltage drop across R1? What are the voltages at the two nodes?"
    ),
    "3a-4b" : (
        "We were looking for Vx = Vy + Vz or something equivalent. Substituting the values for Vx, Vy, and Vz, you should get 3.3V = 0V + 3.3V.",
        None
    ),
    "3a-5" : (
        "As you saw in a previous step, the voltage across R1 is 0. Since the resistance is nonzero, by Ohm's Law, the current through R1 must be 0A.",
        "Think back in the previous steps. What is the voltage across R1? What does that say about its resistance and current by Ohm's Law?"
    ),
    "3b-1" : (
        "Nodes 0 and 2 are really the same node since a wire connects them. Thus, there are only 2 distinct nodes in the circuit now.",
        "Look at node 0 and node 2. Are they distinct nodes?"
    ),
    "3b-2" : (
        "Recall that Ohm's Law states that V = IR. You should get R1 = Vy/Iy = 1000 ohms.",
        "Recall that Ohm's Law states that V = IR."
    ),
    "3b-3" : (
        "They should certainly be the same!",
        None
    ),
    "3b-4" : (
        "Once again, we have \"Vx = Vy + Vz\". Substitution yields 3.3V = 3.3V + 0V.",
        None
    ),
    "3c-1a-soft" : (
        "The ground node is defined to be 0V.",
        "Hint: it's the ground node!"
    ),
    "3c-1b-soft" : (
        "u1 is connected directly to the positive end of the voltage source, so it must be 3.3V.",
        "u1 is connected directly to the positive end of the voltage source!"
    ),
    "3c-1c-soft" : (
        None,
        "You should have gotten something different. Please check your circuit and where you're measuring."
    ),
    "3c-2a-soft" : (
        "Vz = u2 - u0 = 2.2V - 0V = 2.2V",
        "Vz = u2 - u0. What are u2 and u0?"
    ),
    "3c-2b-soft" : (
        "Vy = u1 - u2 = 3.3V - 2.2V = 1.1V",
        "Vy = u1 - u2. What are u1 and u2?"
    ),
    "3c-2c-soft" : (
        "Vz = Vs * R2/(R1 + R2) = 3.3 * 2/3 = 2.2 V\nVy = Vs * R1/(R1 + R2) = 3.3 * 1/3 = 1.1 V\nThus, voltages obtained using the voltage divider formula agree with our measurements (there might be **slight** deviation due to measurement errors).",
        None
    ),
    "3c-1a-hard" : (
        "The ground node is defined to be 0V.",
        "Hint: it's the ground node!"
    ),
    "3c-1b-hard" : (
        "u1 is connected directly to the positive end of the voltage source, so it must be 3.3V.",
        "u1 is connected directly to the positive end of the voltage source!"
    ),
    "3c-1c-hard" : (
        None,
        "You should have gotten something different. Please check your circuit and where you're measuring."
    ),
    "3c-2a-hard" : (
        "Vz = u2 - u0 = 2.2V - 0V = 2.2V",
        "Vz = u2 - u0. What are u2 and u0?"
    ),
    "3c-2b-hard" : (
        "Vy = u1 - u2 = 3.3V - 2.2V = 1.1V",
        "Vy = u1 - u2. What are u1 and u2?"
    ),
    "3c-2c-hard" : (
        "Vz = Vs * R2/(R1 + R2) = 3.3 * 2/3 = 2.2 V\nVy = Vs * R1/(R1 + R2) = 3.3 * 1/3 = 1.1 V\nThus, voltages obtained using the voltage divider formula agree with our measurements (there might be **slight** deviation due to measurement errors).",
        None
    )
}

def autograde(answer=-1, question="3a-1", no_check=False):
    tolerance_pct = 5.0 #error threshold percent
    answer = float(answer)
    correct = True
    if no_check:
        pass
    elif q_ans[question] == 0 and answer == 0:
        print("Correct!")
    elif (q_ans[question] != 0) and (abs(q_ans[question]-answer))*100.0/q_ans[question] <= tolerance_pct:
        print("Correct!")
    else:
        print("Sorry, that's not quite right.")
        correct = False
    
    exp = q_exp[question]
    if correct and exp[0]:
        print(exp[0])
    elif not correct and exp[1]:
        print(exp[1])
