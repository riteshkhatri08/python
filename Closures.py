#a function that returns another function which always gives the square of
#the value pssed to outer function, sthe paramter passed is stored in closure scope of
#the outer function
def  makeSquareMethod(number):

    def square():

        return number * number #number is accessed from the closure scope of the outer function

    #outer function returning the inner function which grabbed the "number" variable from its closure scope
    return square


# makeSquareMEthod() will return a function that always give the square of the value
# that was passed as parameter to makeSquareMethod() when it was called
squareOf27 = makeSquareMethod(27)
squareOf55 = makeSquareMethod(55)

# Output will be square of 55, will is in closure scope of makeSquareMethod()
print(squareOf55())

# Output will be square of 27 , 27 will is in closure scope of makeSquareMethod()
print(squareOf27())

