word = input('Enter your word:')
i = int(input('Enter 1 to code:'))
if i == 1:
  print('Coding...')



  if len(word) >= 3:
   

    a = (word[1:])
    b = (word[0])
    c = a + b
    
    import random
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    prefix = ''
    suffix = ''


    for i in range(3):
          prefix += random.choice(letters)
          suffix += random.choice(letters)
    encoded = prefix + c + suffix
    print(encoded)
    
    
    
elif len(word) < 3:
        a = (word[1:])
        b = (word[0])
        c = a + b
        

        import random
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        prefix = ''
        suffix = ''


        for i in range(3):
          prefix += random.choice(letters)
          suffix += random.choice(letters)
        encoded = prefix + c + suffix
        print(encoded)

h = input('Enter dc to decode your message:')
if h == 'dc':
     print('Decoding...')
     decoded = encoded[3:-3]
     original = decoded[-1] + decoded [:-1]


     print(original)
     

