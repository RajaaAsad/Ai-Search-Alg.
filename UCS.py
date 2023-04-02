
cost={('s','a'):1,('s','b'):5,('s','c'):8,('a','d'):3,('a','e'):7,('a','g'):9,('b','g'):4,('c','g'):5}


def UCS(g,goal):
    q=[(0,'s')] 
    visited=[]
    

    while q:
       c,node=q.pop(0)
       v=node[-1]
       print(v)
       if v in visited:
           continue
       
       if v==goal:
           print(node,c)
           break
           

       for i in g.get(v,[]):
          temp=list(node)
          temp.append(i)
          newCost=c+cost[(v,i)]
          q.append((newCost,temp))
          q.sort()
        








g={'s':['a','b','c'],'a':['d','e','g'],'b':['g'],'c':['g']} 
UCS(g,'g')


