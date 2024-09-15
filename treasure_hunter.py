print('''       
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


#Index       0       1      2     3     4     5       6      7
choices = ['left','right','up','down','run','walk','climb','crawl']
print("""\nWhen you arrive on the island, 
should you turn to the left or the right? Choose left or right!\n """)
command = input("Enter your choice! ")

#Turn left
if choices[0] == command.lower():
     print('Ohh! no There is a Jaguar')
     print('Should you run or walk slowly pass the jaguar? 🏃‍♀️‍➡️RUN or walk🚶‍♂️‍')
     command = input("Enter your choice! ")
     if choices[4]  == command.lower():
         print('You are now lunch!!')
     elif choices[5] == command.lower():
         print("Wow! you passes the jaguar safely that was a close called.")


#Turn right
elif choices[1] == command.lower():
    print("""You saw a mountain adorned with beautiful flowers,
     with waterfalls cascading below. 
    A ladder ascends and descends the mountain. 
    Will you choose to go up or down?\n""")
    command = input("Enter your choice! ")


    #Move Upwards
    if choices[2] == command.lower():
        print("""You climb to where the sun shines bright,   
                 A mountain crowned in gold and light,  
                 With diamonds glimmering all around,  
                 In this radiant peak, pure beauty is found.""")
        print("""CONGRATULATIONS ON FINDING THE TREASURE 
                                _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'/U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-U//.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
             '-._'-.|| |' `_.-'
                    '-.||_/.-'
        """)

    elif choices[3] == command.lower():
        print(""" You got killed by a pirate
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`""")
