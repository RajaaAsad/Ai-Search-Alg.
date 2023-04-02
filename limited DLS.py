def dfs(g,goal,l):
    stack=[(list(g.keys())[0],0)] #list of tuples (1,0) (node,level)
    temp,visited=[],[]
    path=[]
    childpar={1:None} #{child:parent}

    while stack:
        node,level=stack.pop()
        if node==goal:      #find the goal then Path is 
            path.append(goal)
            while goal!=1: 
                path.insert(0,childpar[goal])
                goal=childpar[goal]


        if node in visited:
            continue
    
        visited.append(node)

        for i in g.get(node,[]): #add the childern of node to stack
            if level+1<=l:       #level less then or equal the limit
                temp.append((i,level+1))
                childpar[i] = node

        while temp:
            stack.append(temp.pop())    

    print (path)




g1={1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11],6:[12,13],7:[14,15]}
dfs(g1,8,4)
