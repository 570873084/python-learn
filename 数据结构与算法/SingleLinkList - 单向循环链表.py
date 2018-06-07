
class Node(object):
    '''单链表节点'''
    def __init__(self,elem,next=None):
        self.elem = elem
        self.next = next


class SingleLinkList(object):
    def __init__(self,node=None):
        self.__head =node
        #特殊情况，链表只有一个头部节点
        if node:
            node.next =self.__head



    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head ==None


    def length(self):
        '''判断链表长度'''
        if self.__head == None:
            return 0
        cur = self.__head
        count =1
        while cur.next != self.__head:
            count +=1
            cur = cur.next
        return count


    def travel(self):
        '''遍历链表'''
        if self.__head == None:
            return 0
        #cur游标，用来移动遍历节点
        cur = self.__head
        #print(cur.elem,cur.next,'3')
        while cur.next != self.__head:
            print(cur.elem,end=',')
            cur =cur.next
            #退出循环的时候，最后一个节点没有打印出来
        print(cur.elem)



    def add(self,item):
        '''链表头部添加元素'''
        node = Node(item)
        cur = self.__head
        if self.__head ==None:
            self.__head = node
            node.next = self.__head
        else:
            node.next =self.__head
            while cur.next != self.__head:
                cur =cur.next
            self.__head =node
            cur.next =self.__head




    def append(self,item):
        '''链表尾部添加元素'''
        node = Node(item)
        #print(node.elem,node.next,'1')
        if self.__head == None:
            self.__head = node
            node.next =self.__head
            #print(self.__head.elem,self.__head.next,'2')
        else:
            cur =self.__head
            while cur.next != self.__head:
                cur =cur.next
            node.next=self.__head
            cur.next=node


    def insert(self,pos,item):
        '''指定位置添加元素'''
        if pos >= self.length()-1:
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            node =Node(item)
            cur = self.__head
            count = 0
            while count <  (pos-1):
                cur =cur.next
                count +=1
            node.next =cur.next
            cur.next =node


    def remove(self,item):
        '''删除节点'''
        #设置两个游标
        if self.__head == None:
            return 0
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem ==item:
                #节点在头部，先判断
                if cur == self.__head:
                    self.__head =cur.next
                    #寻找尾节点
                    rear =self.__head
                    while rear.next != self.__head:
                        rear =rear.next
                    rear.next =self.__head
                else:
                    pre.next = cur.next              #中间节点删除
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向最后节点，删除最后节点
        if cur.elem == item :
            #只有一个节点时
            if cur == self.__head:
                self.__head =None
            else:
                pre.next = self.__head






    def search(self,item):
        '''查找节点是否存在'''
        if self.__head ==None:
            return 0
        cur =self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环的时候，最后一个节点没有打印出来
        if cur.elem == item:
            return  True
        return False





if __name__ =='__main__':
    sll =SingleLinkList()
    #print(sll.is_empty())
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.append(7)
    #sll.travel()
    sll.insert(2,11)
    sll.search(11)


    '''sll.add(1)
sll.add(2)
sll.add(3)
sll.add(6)
sll.travel()
sll.length()
ll.append(1)

sll.travel()
sll.append(2)
sll.travel()
sll.append(3)
sll.travel()
sll.append(5)
sll.append(6)
sll.append(7)
sll.travel()'''
