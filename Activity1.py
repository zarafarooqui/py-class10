class library:
    def __init__(self,list_of_books,name):
        self.booksList=list_of_books
        self.name=name
        self.lendDict={}

    def displayBooks(self):
          print(f"We have the following books in our library:{self.name}") 
          for book in self.booksList:
              print(book)  
    def lendBook(self,user,book):
         if book not in self.booksList:
              print("Sorry,we do not have that book.")
         elif book in self.lendDict:
              print(f"the book is already being used by{self.lendDict[book]}")
         else:
              self.lendDict[book]=user
              print(
                   "Lender_Book database has been updated.You can take the book now."
              )

    def addBook(self,book):
         self.booksList.append(book)
         print(f"{book} has been added to the book list.")

    def returnBook(self,book):
         if book in self.lendDict:
              del self.lendDict[book]
              print("Book has been returned.")
         else:
              print("That book wasn't borrowed from us.")

if __name__=='__main__':
     books= library(['Python','Harry Potter','Rich Dad Poor dad','Javascript','c++ Basics'],"Let's Upskill")
     user_name=input(f"Welcome to the {books.name} library.Enter your name:")
while True:
     print(
        "1. Display Books\n2. Lend a Book\n3.Add a Book\n4.Return a Book\n5. Quit"
     )
     user_choice=input("Enter your choice to continue:")

     if user_choice not in ['1','2','3','4','5']:
          print("Please enter a valid option.")
          continue
     
     if user_choice =='1':
          books.displayBooks()
     elif user_choice=='2':
          book=input("Enter the name of the book you want to lend")
          books.lendBook(user_name, book)
     elif user_choice=='3':
          book=input("Enter the name of the book you want to add")
          books.addBook( book)
     elif user_choice=='4':
          book=input("Enter the name of the book you want to return")
          books.returnBook( book)
     elif user_choice=='5':
          print(f"Thank you for using the library,{user_name}. Goodbye!")
          break