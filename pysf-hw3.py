from sty import fg, bg, ef, rs
import numpy as np 





color_bar = (255*(np.random.rand(27 , 3))).astype(np.int)

print(bg(0,0,0)+"space: " + bg(color_bar[26,0],color_bar[26,1],color_bar[26,2]) + " ")

a_code = ord("a")
for i in range(a_code, a_code+26):
    index = i - a_code
    print(bg(0,0,0)+chr(i)+": " + bg(color_bar[index,0],color_bar[index,1],color_bar[index,2]) + " ")
    
print(bg(0,0,0))    
text = input("please enter your text")

cursor = 0
while(cursor < len(text)):
    if cursor % 14 == 0:
        print()

    if not text[cursor] == ' ' :   
        index = ord(text[cursor]) - ord('a')
    else:
        index = 26
    print(bg(color_bar[index,0],color_bar[index,1],color_bar[index,2]) + " ", end = '')
    cursor+=1
