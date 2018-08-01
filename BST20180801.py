# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:36:06 2018

@author: lenovo
"""

#start at 10:23 Wednesday 20180801 at nju xianlin campus
# paused at 11:10 
# restart at 16:50 
# finished at 17:22  about 1.5 hours to finish not bad 

#------------------------------------------------------------------------------
class NODE:
    def __init__(self, val = 0):
        self.val = val
        self.p = None
        self.l = None
        self.r = None
#------------------------------------------------------------------------------
class BST:
    def __init__(self):
        self.root = NODE()

    def minimum(self,r):
#        r = self.root
        while r and r.l != None:
            r = r.l
        return r
    def maximum(self, r):
#        r = self.root
        while r and r.r:
            r = r.r
        return r
    def predecessor(self, i):
        '''
        caution: return value maybe None, means i does not have predecessor Node
        '''
#        root = self.root
        if i.l:
            return self.maximum(i.l)
        else:
            y = i.p
            while y and y.l == i:
                i = y
                y = i.p
            return y
            
    def successor(self, i):
        '''
        caution: return value maybe None, means i does not have predecessor Node
        '''
        if i.r:
            return self.minimum(i.r)
        else:
            y = i.p
            while y and y.r == i:
                i = y
                y = i.p
            return y
    def inorder(self, r):
#        root = self.root
        if r:
            
            self.inorder(r.l)
            print(r.val)
            self.inorder(r.r)
    def search(self, r, key):
        '''
        caution: here the key is the Node's attribute val, not the Node itself
        '''
        root = r
        if root == None:
            return None
        if root.val == key:
            return root
        elif key > root.val:
            self.search(root.r, key)
        else:
            self.search(root.l, key)
            
    def insert(self, x):
        '''
        caution： here x means NODE , assume that x.p x.l x.r == None
        '''
        r = self.root
        y = None
        while r :
            y = r
            if x.val <= r.val:
                r = r.l
            else:
                r = r.r
        x.p = y
        if y == None:
            self.root = x
        elif x.val <= y.val:
            y.l = x
        else:
            y.r = x
    def trans(self, u, v):
        '''
        assume that u is not None
        '''        
        if u.p == None:
            self.root = v
        elif u.p.l == u:
            u.p.l = v
        else:
            u.p.r = v
        if v:
            v.p = u.p
    def delete1(self, z):
        '''
        assume that u is not None
        '''
        if z.l == None:
            self.trans(z,z.r)
        elif z.r == None:
            self.trans(z,z.l)
        else:
            y = self.successor(z)
            if y.p != z:
                self.trans(y,y.r)
                y.r = z.r
                y.r.p = y
            self.trans(z,y)
            y.l = z.l
            y.l.p = y
#------------------------------------------------------------------------------
a = NODE(1)
b = NODE(2)
c = NODE(3)
d = NODE(4)
e = NODE(5)
ee = NODE(2.5)
bb = b
b.l = a
b.r = e
a.p = b
e.p = b
e.l = c
c.p = e
c.r = d
d.p = c

tree = BST()
tree.root = b
#tree.inorder(b)
#print(tree.search(b,2))
#print(tree.minimum().val)

#print(tree.maximum().val)

#print(tree.successor(tree.maximum()).val)
tree.insert(ee)
tree.inorder(b)
tree.delete1(ee)
tree.inorder(b)
print('---------------')
tree.delete1(b)
print(tree.root.val)
#print(tree.minimum().val)

            
            
            
        
    
        
    
