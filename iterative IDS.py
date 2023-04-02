
def IDS(g,goal,d):
    for i in range(d):
        path=dls(g,goal,i)
    return path

def dls(g,goal,limit):
    stack=[(list(g.keys())[0],0)]
    visited,temp,path=[],[],[]
    childPar={1:None}
    
    while stack:
        node,level=stack.pop()
        

        if node==goal:
            visited.append(goal)
            path.append(goal)
            while goal!=1:
                path.insert(0,childPar[goal])
                goal=childPar[goal]
            break        
        
        if node in visited:
            continue
        visited.append(node)
        for i in g.get(node,[]):
            if level+1<=limit:
                temp.append((i,level+1))
                childPar[i]=node
        while temp:
            stack.append(temp.pop())
    print(visited)    
    return path



g={1:[2,3],2:[4,5],3:[6,7]}  
print(IDS(g,7,4))     
