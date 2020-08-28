#Node Class to define a node 
class Node:
    def __init__(self,value):
        #set the value of node as theparameter passed
        
        self.value=value 
        self.next=None 
        self.prev=None
#Sentinel List class to create Sentinel list objects
class SentinelList:
    def __init__(self,*args):#constructor for Sentinel list class, self means the object which is created is itself passed as a parameter . its usage in function is similar to "this" keyword in java
    
        
        self.head=Node(0) #set the head to point to a dummy node 
        self.tail=Node(0)   #set the tail to point to a dummy node 
        self.head.next=self.tail #set the first dummt node  to point to the dummy node at the end [0]->[0] this is what the list looks like right now
        self.tail.prev=self.head #set the dummy node at the end to point to the  dummy node at start [0]<=>[0] this what the list looks like right now 

        
        self.addNode(arg) #add the nodes for the values passed 

        

    def addNode(self,*args):# *args keyword to allow the function to accept n number of arguments
        count=0 # a variable that  counts the number of items that were added to the list  after this function ends
    print("List Created")
    
        #  the "*" symbol before the word args make it a type of an iterator object.
        for arg in args: #for loop to iterate over each value passed in the *args 
            newNode=Node(arg)#creating a new node with value currently inside the arg variable during the iteration
            newNode.prev=self.tail.prev #set newnode to point towards the node that is just before the dummy node at the end 
            newNode.next=self.tail #set newnode to point toward the last dummy node
            self.tail.prev.next=newNode #set  the node that was just before the last dummy node to point towards new node
            
            self.tail.prev=newNode #set the last dummy node to point towards the new node
            count+=1#increment the count  variable as a new node was added to list just before the ending dummy node
        print(count,"Values added.")
        #print("Now the list is: ")
        #self.printForward()#call print function to view the list rightnow
    
    def printForward(self):
        current=self.head.next #set current to point towards the first node after the the starting dummy node
        while(current!=self.tail): #loop until the current node points towards the ending dummy node , 
            print(current.value) #print the value in current node 
            current=current.next # set current node to point towards the next node






slist= SentinelList(55,98,78) #creating a list
slist.addNode(5,6,77) #passing multiple  values
slist.printForward()

