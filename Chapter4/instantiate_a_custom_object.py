class MyFirstClass:
    print ("Who wrote this?")
    index = "Author-Book"
    def hand_list(self, philosopher,book ):
        print(MyFirstClass.index)
        self.philosopher = philosopher
        self.book = book
        print(self.philosopher + " wrote the book: " + self.book)


whodunnit = MyFirstClass()
authors_name = input("Write the name of the author: ")
name_of_the_book = input("Write the name of the book: ")
whodunnit.hand_list(authors_name, name_of_the_book)

'''
OR
'''

# Sample Solution code
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

