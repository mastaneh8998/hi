list1= []
    
def rooms_def1(rooms,list2):
    with open(f'texts\\room-text\\{rooms}.txt', 'r') as file:
        room1_rs2 = str(file.read())
        list2.append(room1_rs2)
    
rooms_def1("room1", list1)
rooms_def1("room2", list1)
rooms_def1("room3", list1)
print(list1)
print(list1[0])
print(list1[1])

print(list1[2])

