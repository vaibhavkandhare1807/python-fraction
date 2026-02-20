from __future__ import annotations
import math
class Fraction:
    '''
    Created by: Vaibhav Kandhare
    Represents a rational number (fraction) with integer numerator and denominator.
    The fraction is always stored in its simplest form using GCD(Normalization).
    Attributes:
        __num (int): Numerator of the fraction
        __den (int): Denominator of the fraction
    '''
    __slots__ = ("__num", "__den")
    def __init__(self,n:int|float|Fraction,d:int|float|Fraction=1)->None:
        '''
        Initialize a Fraction object.
        Accepts numerator and denominator as int, float, or Fraction.
        Automatically converts float to Fraction and simplifies the result.
        '''
        if (not isinstance(n,(Fraction,int,float))) or (not isinstance(d,(Fraction,int,float))):
             raise TypeError("Numerator and denominator must be int, float, or Fraction")
        
        if isinstance(n,(float,Fraction)):
            if isinstance(n,float):
                n=Fraction.from_float(n,4)
            if isinstance(d,(float,Fraction)):
                if isinstance(d,float):
                    d=Fraction.from_float(d)
                self.__num=n.__num*d.__den
                self.__den=n.__den*d.__num
                if self.__den == 0:
                    raise ValueError("Zero in denominator is not permitted")
            else:
                self.__num=n.__num
                self.__den=n.__den*d
                if self.__den == 0:
                    raise ValueError("Zero in denominator is not permitted")
        elif isinstance(d,(Fraction,float)) and not isinstance(n,(float,Fraction)):  
            if isinstance(d,float):
                d=Fraction.from_float(d)
            self.__num=n*d.__den
            self.__den=d.__num
            if self.__den == 0:
                raise ValueError("Zero in denominator is not permitted")
        else:
            self.__num=int(n)
            self.__den=int(d)
            if self.__den == 0:
                raise ValueError("Zero in denominator is not permitted")
        gc = math.gcd(self.__num, self.__den)  
        self.__num //= gc
        self.__den //= gc
        if self.__den<0:
                    self.__num,self.__den=-self.__num,-self.__den
    def __str__(self)->str:
        '''
        Return the human-readable string representation of the fraction.
        If numerator is zero or denominator is one only numerator is displayed.
        '''
        if self.__num==0:
            return '{}'.format(int(self.__num))
        if self.__den==1:
            return '{}'.format(int(self.__num))  
        return '{a}/{b}'.format(a=int(self.__num),b=int(self.__den))

    def __repr__(self)->str:
        '''
        Return official string representation of this Fraction.
        If numerator is zero or denominator is one only numerator is displayed.
        '''
        if self.__num==0:
            return '{}'.format(int(self.__num))
        if self.__den==1:
            return '{}'.format(int(self.__num))  
        return '{a}/{b}'.format(a=int(self.__num),b=int(self.__den))
    
    def __add__(self,other:int|float|Fraction)->float|Fraction:
        '''
        Add this Fraction with int, float, or another Fraction.
        Note:
            Returns float when adding with float.
        '''     
        if isinstance(other,int):          
            return Fraction(self.__den*other+self.__num,self.__den)  
        if isinstance(other,float):
            return float(self)+other                          
        if  isinstance(other,Fraction):
            return Fraction(self.__num*other.__den+self.__den*other.__num,self.__den*other.__den)  
        return NotImplemented
    
    def __radd__(self,other:int|float|Fraction)->float|Fraction:    
        ''' 
        Perform reverse addition.  
        This method is called when the left operand's __add__ method returns NotImplemented.
        '''
        return self+other
        
    def __sub__(self,other:int|float|Fraction)->float|Fraction:     
        '''
        Subtract a value from this Fraction.
        Note:
            Returns float when subtracting float.
        '''      
        if isinstance(other,int):   
            return Fraction(self.__num-self.__den*other,self.__den) 
        if isinstance(other,float):
            return float(self)-other
        if  isinstance(other,Fraction):
            return Fraction(self.__num*other.__den-self.__den*other.__num,self.__den*other.__den)   
        return NotImplemented
    
    def __rsub__(self,other:int|float|Fraction)->float|Fraction:    
        '''
        Perform reverse subtraction.
        Called when the left operand's __sub__ method returns NotImplemented.
        '''
        return -(self-other)
    
    def __mul__(self,other:int|float|Fraction)->float|Fraction:                
        '''
        Multiply this Fraction with another value.
        Note:
            Returns float when multiplying with float.
        '''
        if isinstance(other,int):         
            return Fraction(other*self.__num,self.__den)   
        if isinstance(other,float):
            return float(self)*other
        if  isinstance(other,Fraction):
            return Fraction(self.__num*other.__num,self.__den*other.__den) 
        return NotImplemented
    
    def __rmul__(self,other:int|float|Fraction)->float|Fraction:
        '''
        Perform reverse multiplication.
        Called when the left operand's __mul__ method returns NotImplemented.
        '''
        return self*other
    
    def __truediv__(self,other:int|float|Fraction)->float|Fraction:  
        '''
            Divide this Fraction by another value.
            Raises:
                ZeroDivisionError: If division by zero occurs.
            Note:
                Returns float when dividing with float
        '''
        if isinstance(other,int): 
            if other==0:            
                raise ZeroDivisionError("Cannot divide by zero")  
            else:
                return Fraction(self.__num,other*self.__den)  
        if isinstance(other,float):
            if other==0:            
                raise ZeroDivisionError("Cannot divide by zero")
            else:
                return float(self)/other
        if  isinstance(other,Fraction):
            if other.__num==0:            
                raise ZeroDivisionError("Cannot divide by zero")
            else:
                return Fraction(self.__num*other.__den,self.__den*other.__num) 
        return NotImplemented
    
    def __rtruediv__(self,other:int|float|Fraction)->float|Fraction:   
        '''
        Called when the left operand's __truediv__ method returns NotImplemented
        Raises:
            ZeroDivisionError: If this fraction represents zero.
        '''
        if self.__num==0:
            raise ZeroDivisionError("Cannot divide by zero")  
        if isinstance(other ,int):
            return Fraction(other*self.__den,self.__num)  
        if isinstance(other,float):     
            return other/float(self)
        return NotImplemented
    
    def __lt__(self, other:int|float|Fraction)->bool:
        '''
        Check if this Fraction is less than another value(int|float|Fraction).
        Returns:
            bool: True if this Fraction is less, otherwise False.
        '''
        if isinstance(other,(float,int)):
            return float(self)<other
        if  isinstance(other,Fraction):
            return self.__num*other.__den<self.__den*other.__num
        return NotImplemented
    
    def __gt__(self, other:int|float|Fraction)->bool:
        '''
        Check if this Fraction is greater than another value.
        Returns:
            bool: True if this Fraction is greater, otherwise False.
        '''
        if isinstance(other,(float,int)):
            return float(self)>other
        if  isinstance(other,Fraction):
            return self.__num*other.__den>self.__den*other.__num
        return NotImplemented
    
    def __le__(self,other:int|float|Fraction)->bool:
        '''
        Check if this Fraction is less than or equal to another value.
        Returns:
            bool: True if this Fraction is less than or euqal, otherwise False.
        '''
        if isinstance(other,(float,int)):
            return float(self)<=other
        if  isinstance(other,Fraction):
            return self.__num*other.__den<=self.__den*other.__num
        return NotImplemented
    
    def __ge__(self,other:int|float|Fraction)->bool:
        '''
        Check if this Fraction is greater than or equal to another value.
        Returns:
            bool: True if this Fraction is greater than or equal, otherwise False.
        '''
        if isinstance(other,(float,int)):
            return float(self)>=other
        if  isinstance(other,Fraction):
            return self.__num*other.__den>=self.__den*other.__num
        return NotImplemented
    
    def __ne__(self, other:int|float|Fraction)->bool:
        '''
        Check if this Fraction is not equal to another value.
        '''
        if isinstance(other,(float,int)):
            return float(self)!=other
        if  isinstance(other,Fraction):
            return self.__num*other.__den!=self.__den*other.__num
        return NotImplemented
    
    def __eq__(self, other:int|float|Fraction)->bool:
        '''
        Check if this Fraction is equal to another value.
        '''
        if isinstance(other,(float,int)):
            return float(self)==other
        if  isinstance(other,Fraction):
            return self.__num*other.__den==self.__den*other.__num
        return NotImplemented
    
    
    def __neg__(self)->Fraction: 
        '''
        Return the negation of this Fraction.
        '''
        return Fraction(-self.__num, self.__den)
    
    def __pos__(self)->Fraction:
        '''
        Return a copy of this Fraction (unary plus operation).
        Does not change the value of Fraction
        '''
        return Fraction(self.__num,self.__den)
    
    def __abs__(self)->Fraction:  
        '''
        Return the absolute value of this Fraction.
        '''
        return Fraction(abs(self.__num),abs(self.__den))
    
    def __int__(self)->int:  
        '''
        Convert this Fraction to an integer.
        It truncates toward zero
        '''
        return -((-self.__num)//self.__den) if self.__num<0 else self.__num//self.__den
    
    def __float__(self)->float: 
        '''
        Convert this Fraction to a float.
        '''
        return self.__num/self.__den
    
    def __bool__(self)->bool:
        '''
        Return the truth value of this Fraction.
        A Fraction with value zero is considered False.
        Any Fraction other than zero is considered True
        '''
        return self.__num!=0
             
    def reciprocal(self)->Fraction:  
        '''
        Return the reciprocal of this Fraction.
        Raises:
            ValueError: If numerator is zero.
        '''
        if self.__num == 0:
            raise ValueError("Zero has no reciprocal")
        return Fraction(self.__den, self.__num) 
    
    def to_tuple(self)->tuple[int, int]:     
        '''
        Convert this Fraction to tuple form.
        Returns:
            tuple[int, int]: (numerator, denominator)
        '''
        return (self.__num,self.__den)
    
    def __hash__(self)->int:
        '''
        Return hash value of this Fraction.
        Returns:
            int: Hash value.
        '''
        return hash(self.__num / self.__den)  
    
    def is_proper(self)->bool:
        '''
        Check if this Fraction is proper.
        Returns:
            bool: True if numerator magnitude is less than denominator.
        '''
        return abs(self.__num)<abs(self.__den) 
    
    def is_improper(self)->bool:
        '''
        Check if this Fraction is improper.
        Returns:
            bool: True if numerator magnitude is greater than or equal to denominator.
        '''
        return abs(self.__num)>=abs(self.__den) 
    
    def to_string(self)->str:
        '''
        Return String conversion of this Fraction.
        Always in the form p/q unlike __str__
        '''
        return '{a}/{b}'.format(a=int(self.__num),b=int(self.__den))
    
    @classmethod
    def from_string(cls, s:str)->Fraction:  
        '''
        Create a Fraction from a string.
        Raises:
            TypeError: If input is not string.
            ValueError: If format is invalid.
        '''
        if not isinstance(s,str):
            raise TypeError('Input must be a string')
        s = s.strip()     

        if '/' in s:     
            parts = s.split('/')
            if len(parts) != 2:
                raise ValueError("Invalid format")

            try:
                n, d = map(int, parts)   
            except ValueError:
                raise ValueError("Not a valid fraction")  

            return cls(n, d) 
        else:
            try:
                return cls(int(s), 1)
            except ValueError:
                raise ValueError("Not a valid Fraction")

    @classmethod
    def from_float(cls, value:float, precision:int=4)->Fraction:
        '''
        Create a Fraction from a floating-point number.
        Precision value is by default 4 if not given any. 
        More the precision value more accurate the fraction will be.
        Raises:
            ValueError: If precision is not in [0,8].
        '''
        if not isinstance(value,float):
            raise TypeError('value must be float')
        if not isinstance(precision,int):
            raise TypeError('Precision must be an int value')
       
        if not (0 <= precision <= 8):
            raise ValueError("Precision must be between 0 and 8")
        scale = 10 ** precision
        if value<0:
            n = math.ceil(value * scale - 0.5)
        else:
            n = math.floor(value * scale +0.5)
        d = scale
        return cls(n, d)
 

