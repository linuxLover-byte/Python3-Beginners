line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().title() # Where do you want to put the treasure?

#Line 1
if position == 'A1':
    map[0][0] = 'X'
if position == 'B1':
     map[0][1] = 'X'
if position == 'C1':
    map[0][2] = 'X'
#____________________________
#Line 2
if position == 'A2':
    map[1][0] = 'X'
if position == 'B2':
    map[1][1] = 'X'
if position == 'C2':
    map[1][2] = 'X'
#____________________________
#Line 3
if position == 'A3':
        map[2][0] = 'X'
if position == 'B3':
        map[2][1] = 'X'
if position == 'C3':
        map[2][2] = 'X'


print(f"{line1}\n{line2}\n{line3}")
