import copy
import numpy as np
def Initial_state_of_matrix():                                        #Getting input for initial state
    rows = int(input("ENTER ROWS:"))
    columns = int(input("ENTER COLUMNS:"))
    matrix = []
    print("ENTER ENTRIES IN COLUMN WISE FASHION:")
    for i in range(rows):
        a =[]
        for j in range(columns):
            a.append(int(input()))
        matrix.append(a)
    return matrix

def Final_state_of_matrix():                                          #Getting input for final state
    rows = int(input("ENTER ROWS:"))
    columns = int(input("ENTER COLUMNS:" ))
    matrix = []
    print("ENTER ENTRIES IN COLUMN WISE FASHION:")
    for i in range(rows):
        a =[]
        for j in range(columns):
            a.append(int(input()))
        matrix.append(a)
    return matrix
    
def Finding_location_of_zero(matrix):                                #Finding location of zero in the matrix
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j]==0:
                location=i,j
    return location

def cell_move_upward(pos1, pos2, pop_number):
    Deep_copy=copy.deepcopy(pop_number)
    transition=Deep_copy[pos1][pos2]
    Deep_copy[pos1][pos2]=Deep_copy[pos1-1][pos2]
    Deep_copy[pos1-1][pos2]=transition
    if Deep_copy not in visitor_list:
        queue_list.append(Deep_copy)
        visitor_list.append(Deep_copy)
        pop_1 = tuple([tuple(x) for x in pop_number])
        deep_1 = tuple([tuple(x) for x in Deep_copy])
        map_dict[deep_1] = pop_1

def cell_move_downward(pos1, pos2, pop_number):
    Deep_copy=copy.deepcopy(pop_number)
    transition=Deep_copy[pos1][pos2]
    Deep_copy[pos1][pos2]=Deep_copy[pos1+1][pos2]
    Deep_copy[pos1+1][pos2]=transition
    if Deep_copy not in visitor_list:
        queue_list.append(Deep_copy)
        visitor_list.append(Deep_copy)
        pop_1 = tuple([tuple(x) for x in pop_number])
        deep_1 = tuple([tuple(x) for x in Deep_copy])
        map_dict[deep_1] = pop_1

def cell_move_leftward(pos1, pos2, pop_number):
    Deep_copy=copy.deepcopy(pop_number)
    transition=Deep_copy[pos1][pos2]
    Deep_copy[pos1][pos2]=Deep_copy[pos1][pos2-1]
    Deep_copy[pos1][pos2-1]=transition
    if Deep_copy not in visitor_list:
        queue_list.append(Deep_copy)
        visitor_list.append(Deep_copy)
        pop_1 = tuple([tuple(x) for x in pop_number])
        deep_1 = tuple([tuple(x) for x in Deep_copy])
        map_dict[deep_1] = pop_1

def cell_move_rightward(pos1, pos2, pop_number):
    Deep_copy=copy.deepcopy(pop_number)
    transition=Deep_copy[pos1][pos2]
    Deep_copy[pos1][pos2]=Deep_copy[pos1][pos2+1]
    Deep_copy[pos1][pos2+1]=transition
    if Deep_copy not in visitor_list:
        queue_list.append(Deep_copy)
        visitor_list.append(Deep_copy)
        pop_1 = tuple([tuple(x) for x in pop_number])
        deep_1 = tuple([tuple(x) for x in Deep_copy])
        map_dict[deep_1] = pop_1

def back_track_node(dicti, start, goal):
    map_dict_path=[]
    pop_1 = tuple([tuple(x) for x in start])
    deep_1 = tuple([tuple(x) for x in goal])
    dict_key=dicti[tuple(deep_1)]
    map_dict_path.append(deep_1)
    map_dict_path.append(dict_key)
    while dict_key != pop_1:
        dict_key=dicti[dict_key]
        map_dict_path.append(dict_key)
    map_dict_path.reverse()
    return map_dict_path

def list_in(info, path, start):
    list_in = []
    for i in info:
        if i == start:
            continue
        else:
            derivative = info.index(i)
            goal = tuple([tuple(x) for x in i])
            transition = path.get(goal)
            transition = info.index(list([list(x) for x in transition]))
            list_in.append([derivative, transition, i])
    return list_in

map_dict={}
queue_list=[]
  

visitor_list=[]
# print(queue_list)

def algortihm():
    Initial_state_of_matrix_hardcode =  Initial_state_of_matrix()
    Final_state_of_matrix_hardcode = Final_state_of_matrix()
    queue_list.append(Initial_state_of_matrix_hardcode) 
    while(True):
        first = queue_list.pop(0)
        
        Pos=Finding_location_of_zero(first)
        i = Pos[0]
        j = Pos[1]
        if first != Final_state_of_matrix_hardcode:
            if i-1>=0:
                cell_move_upward(i,j,first)
            if i+1<3:
                 cell_move_downward(i,j,first)
            if j-1>=0:
                cell_move_leftward(i,j,first)
            if j+1<3:
                cell_move_rightward(i,j,first)
        else:
            print("You are succesful")
            final = back_track_node(map_dict, Initial_state_of_matrix_hardcode, Final_state_of_matrix_hardcode)
            trance = []
            for i in final:
                a = np.concatenate((i))
                b = "".join(str(a)[1:-1])
                trance.append(b)
            open('nodePath.txt', 'w').write('\n'.join('%s' % x for x in trance))


            list_emp = []
            for i in visitor_list:
                trance = list(map(list, i))
                a = np.concatenate((trance))
                b = "".join(str(a)[1:-1])
                list_emp.append(b)
            open('nodes.txt', 'w').write('\n'.join('%s' % x for x in list_emp))
            last_code=list_in(visitor_list,map_dict,Initial_state_of_matrix_hardcode)
            ni = []
            for i in last_code:
                trance = list(map(list, zip(*i[2])))
                x1 = np.concatenate((trance))
                x2 = "".join(str(x1)[1:-1])
                x3 = str(i[0])
                x4 = str(i[1])
                x5 = x3 + "      "+x4+"       "+x2
                ni.append(x5)
            open('NodesInfo.txt', 'w').write('\n'.join('%s' % x for x in ni))
            break
        
        

algortihm()
print(visitor_list)