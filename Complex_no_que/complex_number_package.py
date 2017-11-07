from __future__ import division
import numpy as np


class Complex_Number:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        s=""
        if(self.y>=0):
            s="+"
        else:
            s=""
        self.y=abs(self.y)
        return ("{} "+s+" {}i").format(self.x,self.y)


    def __add__(self,comp2):
        x=self.x+comp2.x
        y=self.y+comp2.y
        new = Complex_Number(x, y)
        return new

    def __sub__(self,comp2):
        x = self.x - comp2.x
        y = self.y - comp2.y
        new = Complex_Number(x, y)
        return new

    def __abs__(self):
        return np.sqrt(self.x,self.y)

    def __mul__(self,comp2):

        x=(self.x*comp2.x)-(self.y*comp2.y)
        y=(self.y*comp2.x)+(self.x*comp2.y)
        new=Complex_Number(x,y)
        return new

    def __div__(self,comp2):
        if(comp2.x==0 and comp2.y==0):
            print ("error ,please enter nonzero denominator")
            return
        comp2=comp2.conjugate()
        new=self.__mul__(comp2)
        di=( (comp2.x*comp2.x) + (comp2.y*comp2.y) )
        x=new.x/di
        y=new.y/di
        new2 = Complex_Number(x, y)
        return new2

    def real(self):
        return self.x

    def imag(self):
        return self.y

    def argument(self):
        return np.tanh(self.y/self.x)

    def conjugate(self):
        new=Complex_Number(self.x,-self.y)
        return new









