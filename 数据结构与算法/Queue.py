#列表实现队列
class Dqueue(object):
    '''创建一个双端队列'''
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        '''往队列头部添加一个item元素'''

        self.__list.insert(0,item)    #O(n）复杂度，头部添加元素
    def add_rear(self):
        '''往队列尾部添加一个item元素'''
        self.__list.append(item)  # O(1)复杂度,尾部添加元素


    def remove_front(self):
        '''从队列头部删除一个元素'''
        return self.__list.pop(0)

    def remove_rear(self):
        '''从队列尾部删除一个元素'''
        return self.__list.pop()


    def is_empty(self):
        '''判断队列是否为空'''
        return self.__list == []


    def size(self):
        '''返回队列大小'''
        return len(self.__list)


if __name__ == '__main__':
    s = Dqueue()
    s.add_front(1)
    s.add_front(2)
    s.add_front(3)
    print(s.remove_front())
    print(s.remove_front())
    print(s.remove_front())

