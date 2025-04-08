def rep_char(c, n):
    print (c*n)

def draw_line_string(msg1, msg2):
    nstr = len(msg1) if(len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr + 4)
    print(f'  {msg1}')
    print(f'  {msg2}')
    rep_char('-', nstr + 4)

name = input('Input his/her name: ')
msg1 = f'Hello {name}.'
msg2 = 'welcome to seoul'

draw_line_string(msg1, msg2)
    
    
