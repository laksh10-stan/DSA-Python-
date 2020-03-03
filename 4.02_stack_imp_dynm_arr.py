# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:23:46 2019

@author: Lakshmendra Singh
"""
'''
Dynamic Array Implementation
First, let's consider how we im plemented a simple array based slack. We Look one index vuriable top which
points lo the index of lhc mosl rcccnlly inserted clement in the stack. To insert (or push) an element, we
increment top index and then place the new clement ut that index.
Similarly, to delete (or pop) an clement we take the clement at top index ond then decrement the top index. We
represent an empty queue with top value equal to - 1. The issue that slill needs Lo be resolved is what we do
when all the slots in the fixed size array stack arc occupied?
First try: Whal if we increment the s ize of the a rray by l every lime the s tack is full?
• Push(): increase size of Sil by l
• Pop(): decrease si;-.c of SIJ by I
Problems with this approach?
This way of incrementing the array :;i;-..c is too cxpcnsivc. Let us see the reason for this. f"or example, at n = I , w
push nn element creole a new army of si;-,c 2 and copy u ll the old array elements to the new nrray, and at I he
end add Lhe new c lement. At 11 - 2, to push an c lement c r<.:ate a n<.:w arrny of size 3 and copy all the old array
elements to the new array, and al the end add the new elemenl.
Similarly, al 11 = n - 1, if we want to push an clement create a new array of size 11 and copy all the old array
elements lo the new array and ut the end add the new clement. After n push operations the total time T(11)
(number of copy operations) is proportional to 1 + 2 + ... -I n ,,,Q(n2 ).
Alternative Approach: Repeated Doubling
Let us improve the complexity by using the array c1011bli11g technique. If the array is full, crealc a new array of
twice the size, and copy Lhe ilems. With this approach, pushing n items takes time proportional w n (not 112 ).
For simplicity. let us assume that initially we started with n = 1 and moved up to n = 32. That means, we do
the doubling at 1, 2, 4, 8, 16. The other way of analyzing the same approach is: at n = I. if we want to add (push)
an clement, double the current si7..c of the array and copy ull the clements of the old army to the new array.
At 11 = 1, we do 1 copy opera tion, ut 11 2, we do 2 copy opcralions, and 11L 11 = 4, we do 4 copy operations und
so on. By the lime we reach 11 = 32, the total number of copy operations is I+ 2 + 4 + I! I 16 = 3 1 which is
approximately equal to 211 value (32). If we observe carefully, we arc doing the doubling opcru tion lo9n times.
Now, let us generalize the discussion. For 11 push operations we double the array si;1,c log11 times. Thal means,
we will have logn terms in the expression below. The totaJ time T(n) of a series of n push operations is
proportional to
n 11 n n IL
I+ 2 + 4+8 ... +1+2+ 11 = 11 + z + 4+0 ... +4+2+ 1
(
1 I I 4 2
- 11 I + - + - I- ... I - +--1
2 '1!1 1111
= 11(2) ~ 211 = 0(11)
1'(11) is 0(11) and the amortized time of a push operation is 0(1).
'''
class Stack(object):
    def __init__ (self, limit = 10):
        self.stk = limit*[None]
        self.limit = limit
    def isEmpty(self):
        return len(self.stk) <= 0
    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print ('Stack after Push',self.stk)
    def pop(self):
        if len(self.stk) <= 0:
            print ('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()
    def peek(self):
        if len(self.stk) <= 0:
            print ('Stack Underflow!')
            return 0
        else: 
            return self.stk[-1]
    def size(self):
        return len(self.stk)
    def resize(self):
        newStk = list(self.stk)
        self.limit= 2*self.limit
        self.stk = newStk
our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("11")
our_stack.push("31")
our_stack.push("14")
our_stack.push("15")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print (our_stack.peek())
print (our_stack.pop())
print (our_stack.peek())
print (our_stack.pop())
'''
Performance
Let n be the number of elements in the stack. The complexities for operations with this representation can be
given as:
Space Complexity (for n push operations) 0(n)
Time Complexity of CreateStack() 0(1)
Time Complexity of Push() 0(1) (Average)
Time Complexity of Pop() 0(1)
Time Complexity of Top() 0(1)
Time Complexity of IsEmptyStack() 0(1)
Time Complexity of IsFullStack() 0(1)
Time Complexity of DeleteStack() 0(1)
'''