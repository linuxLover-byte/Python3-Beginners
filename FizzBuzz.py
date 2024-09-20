print('''███████ ██ ███████ ███████     ██████  ██    ██ ███████ ███████ 
██      ██    ███     ███      ██   ██ ██    ██    ███     ███  
█████   ██   ███     ███       ██████  ██    ██   ███     ███   
██      ██  ███     ███        ██   ██ ██    ██  ███     ███    
██      ██ ███████ ███████     ██████   ██████  ███████ ███████ ''')

total_range = int(input('\nEnter the total range: '))

for numb in range(1,total_range+1):
  if numb % 3 == 0 and numb % 5 == 0:
    print('Fizz Buzz')
  elif numb % 3 == 0:
    print('Fizz')
  elif numb % 5 == 0:
    print('Buzz')
  else:
    print(numb)
