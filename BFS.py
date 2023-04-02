
def BFS(g,goal):
    q=[[list(g.keys())[0]]]
    visited=[]

    while q:
        node=q.pop(0)
        v=node[-1]

        if v in visited:
            continue

        print(v)
        visited.append(v)

        if v==goal:
            print(node)
            break
        
        for i in g.get(v,[]):
            temp=list(node)
            temp.append(i)
            q.append(temp)

g={1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11],6:[12,13],7:[14,15]}
BFS(g,14)