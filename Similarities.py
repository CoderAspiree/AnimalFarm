import os
import sys
import random
small=["Cat","Dog","Guinea Pig","Hamster","Mouse","Gerbil"]
big=["Elephant","Hippo","Whale","Gorilla","Shark"]
hairy = ["Monkey","Human","Yak"]
reptile=["Snake","Alligator","Crocodile","Turtle","Chameleons","Chameleon","Geckos","Gecko","Lizard"]
amph=["Frog","Salamander"]
inp=(raw_input("Enter animal.Please rememeber to start with a capital letter.\n"))
if inp in hairy:
 print hairy[1],
 print hairy[2],
 print hairy[0],
 print("are similar to your input because they are hairy")
elif inp in big:
 print big[0]
 print big[1]
 print big[2]
 print big[3]
 print big [4]
 print (" are similar to your input because they are big")
elif inp in reptile:
 print reptile[0]
 print reptile[1]
 print reptile[2]
 print reptile[3]
 print reptile[4]
 print reptile[5]
 print reptile[6]
 print reptile[7]
 print reptile[8]
 print ("are similar to your input because they are reptiles")
elif inp in amph:
    print amph[0]
    print amph[1]
    print("are similar to your input because they are amphibians")
elif inp in small:
     print  small[0]
     print small[1]
     print small[2]
     print small[3]
     print small[4]
     print ("are similar to your input because they are small")