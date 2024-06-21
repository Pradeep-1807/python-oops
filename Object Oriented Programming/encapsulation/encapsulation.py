class Bank:
    def __init__(self):
        self.__value=10

    def __ram(self):
        print(self.__value)
        print('Name : Ram')
        print('A/C No: 12345')
        print('Amount : 10000')
        print('Address : salem')

    def __sam(self):
        print('Name : Sam')
        print('A/C No: 12346')
        print('Amount : 20000')
        print('Address : chennai')

obj=Bank()
obj._Bank__ram()
print('\n')
obj._Bank__sam()
print('\n')
print(obj._Bank__value)

