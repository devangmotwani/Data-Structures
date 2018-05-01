# python3

#import sys, threading
#import pprint as pprint
#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self,data=None,child=[],parent=None):
        self.data=data
        self.child=child
        self.parent=parent

class TreeHeight:
        def read(self):
                self.n = int(input())#sys.stdin.readline())
                self.parent = list(map(int, input().split()))#sys.stdin.readline().split()))
        
        def compute_height(self):
                j=0
                parent_child={}
                while j<self.n:
                    if self.parent[j] in parent_child:
                        temp=parent_child[self.parent[j]].append(j)
                        #temp.append(j)
                        #parent_child[self.parent[j]]=temp
                    else:
                        #temp=[]
                        temp=[j]
                        parent_child[self.parent[j]]=temp
                    j+=1
                #return parent_child
                #print(parent_child)
                root=-1
                height = self.max_height_iterative(parent_child,root)
                #height = self.max_height_iterative(parent_child,root)
                return height
        
        def max_height_recursive(self,parent_child,root):
                if root not in parent_child:
                    #print("root",root)
                    return 0
                else:
                    h=0
                    for i in parent_child[root]:
                        #print(i)
                        temp=self.max_height_recursive(parent_child,i)
                        print("i",i)
                        print("temp",temp)
                        if temp>h:
                            h=temp
                    #print(h)
                    return 1+h
        
        def max_height_iterative(self,parent_child,root):
                queue=[]
                queue.append(parent_child[root])
                final_queue=[]
                level=[]
                while queue!=[]:
                    temp=queue.pop(0)
                    #print(temp,":",queue)
                    temp_list=[]
                    for element in temp:
                        if element in parent_child:
                            #print(element,":",parent_child[element])
                            for each in parent_child[element]:
                                level.append(each)
                    if level!=[]:
                        queue.append(level)
                        final_queue.append(level)
                    level=[]
                    #print(queue)
                #print("final",final_queue)
                return len(final_queue)+1 

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

#threading.Thread(target=main).start()

main()
