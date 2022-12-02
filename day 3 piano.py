print('''
	       __________________________________
              /                                  \
	     /					  \__________
	    /                                                \
           /                                                  \
	  /                                                    \
         /                                                      |
        /		 _______________			|
       /                |	|	|                      /|
      /                 |=======+=======|                     / |
     /                  |_______|_______|                    /  |
    /_______________________________________________________/   |
    |                                                       |   /
    |   _   _       _   _   _       _   _       _   _   _   |  /
    |__//|_//|_____//|_//|_//|_____//|_//|_____//|_//|_//|__| /
   /  /// ///  /  /// /// ///  /  /// ///  /  /// /// ///  / /
  /  ||/ ||/  /  ||/ ||/ ||/  /  ||/ ||/  /  ||/ ||/ ||/  / /
 /___/___/___/___/___/___/___/___/___/___/___/___/___/___/ /
 |___|___|___|___|___|___|___|___|___|___|___|___|___|___|/
        \   /                                 \   /
         | ||                                  | ||
         | ||                                  | ||
         |_|/                                  |_|/
''')
print('Welcome to Piano Lesson.')
print('Your mission is to find 3 white keys in the piano with their names.') 

key_c = input('''There are 14 white keys in this picture of the piano.
The key "C" is the first one from the left. And it's the first octave. Octave is the 7 white keys together on a piano.
Do you think after how many keys the following C key will appear (including the first "C") "7" or "8"? ''')

if key_c == "8":
    print('You have found the "C" key. Keep going!')
    
    key_b = input('''The key "B" is the one from the left of the "C" key which you have found before.
Can you find after how many keys the next "B" will appear by using your previous knowledge about octaves?
Type your number here: ''')
    
    if key_b == "8":
       print('You have found the "B" key as well. It is awesome!')
       
       key_a = input('''You have figured out at which places the piano keys "C" and "B" appear.
Now you should find the key "A" and you have 4 choices here: 
1) at the right of the "C" key;
2) at the left from the "C" key;
3) any other key on the piano;
4) at the left from the "B" key;
Type your number to answer here: ''')

       if key_a == "1":
           print(
               'At the right of the "C" key is the key "D". I am sorry, but you are wrong!')
       elif key_a == "2":
           print('''At the left from the "C" key in the first octave is nothing in fact (haha), but in the second it's "D"
You are wrong, try one more time!''')
       elif key_a == "3":
           print('The simple answer, but it is not working here.')
       elif key_a == "4":
           print('''Congratulations! You have won the game.
By the way, just in case you are interested in other keys name it's "D", "E", "F" and "G" at the right from the "C" key.
Just like in the alphabet!''')

    else:
       print('You were very close, but not close enough. You have lost, unfortunately!')
       
else:
    print('You know nothing about a wonderful instrument called piano')
