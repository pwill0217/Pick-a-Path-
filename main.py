print("Welcome to Will's game")
name = input("What is Your name Player?")
age =int(input("What is your age?"))

print("Hello", name, "you are", age, "years old.")

health = 5

print("Your health is at 5")
if age >= 18: 
   print("You are old enough to play!")
   want_to_continue = input("Do you wish to continue? ")
   if want_to_continue == "no":
     print('Goodbye')
   if want_to_continue == "yes":
     print("Let the adventure begin")
   astronaut_or_cyberpunk = input("First Choice... Would you like to be an Astronaut or a Cyberpunk rebel? (Type 1 for astronaut or Type 2 For Cyperpunk rebel.)")

   if astronaut_or_cyberpunk == "1":
       ans = input("Nice! You are the lead astronaut over your space mission...You come to find out that you can't contact the space station...Do you Put on your suit and find out what's wrong from the outside of your ship(1) or try to contact the space station one last time?(2)")
       
       if ans == "1": 
         print("You put on your suit and float outside the ship to see a faulty wirecthe shorts out your suit and lost 2 health")
         ans = input("Now that you fixed the faulty wire and fixed communication with the space station...YOU WIN")
       elif ans == "2":
         print("The console sparks and blows up killing you in the blast....GAME OVER")
   if astronaut_or_cyberpunk == "2":
    ans = input("Welcome to the Cyberpunk Rebellion... You see the a member of the CyberPolice bleeding on the ground.... Do you help the officer (1) or Kill the officer just in case back up is called (2)? ")  
    if ans == "1":
      print("You help the officer and he puts in a good word for you at the police station")
      ans = input("While escorting a cyberpackage you trip and fall while running from two police officers...Do you get up run  (1) or surrender to the poilce(2)")
      
      if ans == "1":
        ans = input("As you run away you hear a gunshot go off, but it doesn't hit you because the officer you saved before takes the hit so you can deliver the package....YOU WIN!")
      if ans == "2": 
        ans = input("Since you surrendered to the police...YOU LOSE")
    if ans == "2":
      ans = input("After killing the police officer, you are now wanted by the police and you will be on the run forever...GAME OVER. ")
elif age >= 17:
  print("You can play with supervision")
  want_to_continue = input("Would you like to continue? ").lower()
  if want_to_continue == "yes":
     print("Let the adventure begin")
     astronaut_or_cyberpunk = input("First Choice... Would you like to be an Astronaut or a Cyberpunk rebel? (Type 1 for astronaut or Type 2 For Cyperpunk rebel.)")
     if astronaut_or_cyberpunk == "1":
       ans = input("Nice! You are the lead astronaut over your space mission...You come to find out that you can't contact the space station...Do you Put on your suit and find out what's wrong from the outside of your ship(1) or try to contact the space station one last time?(2)")
       
       if ans == "1": 
         print("You put on your suit and float outside the ship to see a faulty wire  shorts out your suit and lost 2 health")
         ans = input("Now that you fixed the faulty wire and fixed communication with the space station...YOU WIN")
       elif ans == "2":
         print("The console sparks and blows up killing you in the blast....GAME OVER")
  if astronaut_or_cyberpunk == "2":
    ans = input("Welcome to the Cyberpunk Rebellion... You see the a member of the CyberPolice bleeding on the ground.... Do you help the officer (1) or Kill the officer just in case back up is called (2)? ")  
    if ans == "1":
      print("You help the officer and he puts in a good word for you at the police station")
      ans = input("While escorting a cyberpackage you trip and fall while running from two police officers...Do you get up run  (1) or surrender to the poilce(2)")
      
      if ans == "1":
        ans = input("As you run away you hear a gunshot go off, but it doesn't hit you because the officer you saved before takes the hit so you can deliver the package....YOU WIN!")
      if ans == "2": 
        ans = input("Since you surrendered to the police...YOU LOSE")
    if ans == "2":
      ans = input("After killing the police officer, you are now wanted by the police and you will be on the run forever...GAME OVER. ")
  
  else:
      print("Goodbye")
elif age <= 17:
  print("Sorry You are not old enough to play...")
