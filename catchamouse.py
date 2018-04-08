def cat_mouse(map_, moves):
    x = 0
    y = 0
    c = False
    m = False
    cat = [0,0]
    mouse = [0,0]
    for pos in map_:
        if pos == 'C':
            print('Cat')
            cat = [x,y]
            c = True
            x += 1
        elif pos == '\n':
            print('newline')
            y += 1
            x = 0
        elif pos == 'm':
            print('Mouse')
            mouse = (x,y)
            m = True
            x += 1
        else:
            print('dot')
            x += 1
    final_x = abs(mouse[0] - cat[0])
    final_y = abs(mouse[1] - cat[1])
    final = final_x + final_y
    print(cat)
    print(mouse)

    if not c or not m:
        return 'boring without two animals'
    elif final <= moves:
        return 'Caught!'
    else:
        return 'Escaped!'

map_ = '''\
m........
.........
........C'''
x = cat_mouse(map_, 3)
print (x)
