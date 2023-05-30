#!/usr/bin/python3
'''singly linked list'''


class Node:
    '''class node'''

    def __init__(self, data, next_node=None):
        '''initialize node'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''return data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''set data'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''return next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''set next node'''
        if not isinstance(value, Node) and not (value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''class singly linked list'''
    def __init__(self):
        '''initialize linked list head'''
        self.head = None

    def __str__(self):
        '''make a printable copy of linked lists' content'''
        printable = ""
        nod = self.head
        while nod:
            printable += str(nod.data) + ('\n' if nod.next_node else "")
            nod = nod.next_node
        return printable

    def sorted_insert(self, value):
        '''insert new node in a sorted manner in linked list'''
        nod = self.head
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            return
        elif nod.data > value:
            newnode.next_node = self.head
            self.head = newnode
            return
        while nod.next_node and nod.next_node.data < value:
            nod = nod.next_node
        if nod.next_node:
            newnode.next_node = nod.next_node
        nod.next_node = newnode
