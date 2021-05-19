def unpack(weight: list, box_name:list):
    box = {}
    for i in weight:
        print(i)
        for j in box_name:
            print(j)
            box[i] = j
            box_name.pop(0)
            break
    
    print(box)
    
    sorted_box = []
    for s in sorted(box.keys()):
       sorted_box.append(box[s])
    
    return sorted_box


user_boxes = {'weight': [4,2,18,21,14,13],
              'box_name': ['box1','box2', 'box3', 'box4', 'box5', 'box6']
             }
print(unpack(user_boxes["weight"], user_boxes["box_name"]))