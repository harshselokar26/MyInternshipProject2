#Logical operators  and ,or ,not:-----------------------

#AND-------------------------------------------

print(True and True)#true
print(True and False)#false
print(False and True)#false
print(False and False) #false
print()# for spacing
print()



#OR----------------------------------------------------


print(True or True)
print(True or False)
print(False or True)
print(False or False) 
print()# for spacing
print()



#not operators-----------------------------------------------------------------------------


print(not False)
print(not True)


#  Bitwise operators (Strictly for int and boolean or else error )=======================================
#&,|,^,~,<<,>>

#And opertor
# 1&1---1
# 1&0-----0
# 0&1-----0
# 0&0-----0


#Or opertor
# 1|1---1
# 1|0-----0
# 0|1-----0
# 0|0-----0





print(7&8)#------------------------------------1 1 1--------->7
                                             # 0 0 0-----------8
                                             #---------
                                             #000 using  and operation
print(7|8)

print(7^8)

print(13&14)

print(13|14)

print(13^14)       #--------1101
                   #========1110
                   #-----------------
                          # 0011     same raha toh "zero" same nhi raha toh "one"





#  "~ "  tilt operator
 #0 is +ve
 #1 is -ve

 # 1's compliment
 # 2's compliment is used     0 1 1
                     #     +      1
                     #  --------------
                     #        1 0 0
                     #             1
                     # --------------
                     #        101   2's compliment taken twice because 1 is the last bit

print(~15)
print(~23)





# SHIFT Operators  "<<" left shift opertor /// ">>"Right shift operator

print(10<<2)
print(10>>2)

print(-10>>2)  #------------shifting will always be positive
print(-8<<2)  
#in negative answer after shifting, again find its 2's compliment that will be the final answer
#the shifting depends on sign bit if it is "-ve"ten 11///if "+ve"then 00



#ASSIGNMENT OPERATOR


# Addition assignment
a = 10
a += 2
print(a)   # Expected output: 12

# Subtraction assignment
a = 10
a -= 2
print(a)   # Expected output: 8

# Multiplication assignment
a = 10
a *= 5
print(a)   # Expected output: 50

# Division assignment
a = 10
a /= 9
print(a)   # Expected output: 1.1111111111111112

# Floor division assignment
a = 10
a //= 2
print(a)   # Expected output: 5

# Modulus assignment
a = 10
a %= 2
print(a)   # Expected output: 0

# Bitwise AND assignment
a = 10
a &= 2
print(a)   # Expected output: 2

# Bitwise OR assignment
a = 10
a |= 2
print(a)   # Expected output: 10

# Bitwise XOR assignment
a = 10
a ^= 2
print(a)   # Expected output: 8

# Left shift assignment
a = 10
a <<= 2
print(a)   # Expected output: 40

# Right shift assignment
a = 10
a >>= 2
print(a)   # Expected output: 2


##----------TERNARY OPERATOR//CONDITIONAL OPERATOR--------------------

#SYNTAX

#a=10 b=20
# x=first_variable if condition else second_variable

a=int(input())
b=int(input())
c=int(input())
4#x=a if a>b else b
x=a if a>b and a>c else b if b>c else c
print(x)



