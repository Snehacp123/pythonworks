# super class
class A:
    # public data member
    var1 = None

    # protect data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self,var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("public data member:",self.var1)

    #protected member function
    def displayProtectedMembers(self):
        # accessing protected data members
        print("protected data member:",self._var2)

    # private member function
    def displayPrivateMembers(self):        # accessing private data members
        print("private data member:",self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private member function
        self.__displayPrivateMembers()

# derived class
class B(A):

    # constructor
    def __init__(self,var1,var2, var3):
        A.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMember(self):
        # accessing protcted member functions of super class
        self._displayProtectedMembers()

# creating objects of the derived class
# obj =  B("pub_red","pro_white","private_green")
#
# # callinf public member functions of the class
# obj.displayPublicMembers()
# obj.accessProtectedMember()
# obj.accessPrivateMembers()
# # obj.accessPrivateMembers()
# # object can access public member
# print("object is accessing public member:",obj.var1)
# # object can access protected member
# print("object is accessing protected  member:",obj._var1)
# # object can nott access private member, so it  will generate attribute eror
# # print(obj.__var3)
# print(obj._A__var3)#accessing name mangled variables
# # name mangling
# # A process in which any given identifier with one trailing underscore and two leading underscores
# # is textually replaced with the _Classname__Identifier is known  as name mongling.
# # in _classname__identifier name