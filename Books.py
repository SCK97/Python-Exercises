#In a new python file:
    #Initialise a new 'books' dictionary, with author names as keys and lists of book titles as values.
    #Write a program which asks the user for an author name and prints, as a string, the list of books by that author 
    #(hint: remember the join() method).
    #Stretch goal: Display the list of books in alphabetical order

booksDict = {
    "J. R. R. Tolkien" : "The Hobbit",
    "J. R. R. Tolkien" : "The Silmarillion",
    "J. R. R. Tolkien" : "The Fellowship of the Ring",
    "J. R. R. Tolkien" : "The Two Towers",
    "J. R. R. Tolkien" : "The Return of the King",
    "George R. R. Martin" : "A Game of Thrones",
    "George R. R. Martin" : "A Clash of Kings",
    "George R. R. Martin" : "A Storm of Swords",
    "George R. R. Martin" : "A Feast for Crows",
    "George R. R. Martin" : "A Dance with Dragons",
    "George R. R. Martin" : "The Winds of Winter",
    "George R. R. Martin" : "A Dream of Spring",
    "George R. R. Martin" : "Fire and Blood",
    "Andrzei Sapkowski" : "The Last Wish",
    "Andrzei Sapkowski" : "Sword of Destiny",
    "Andrzei Sapkowski" : "Blood of Elves",
    "Andrzei Sapkowski" : "Time of Contempt",
    "Andrzei Sapkowski" : "Baptism of Fire",
    "Andrzei Sapkowski" : "The Tower of the Swallow",
    "Andrzei Sapkowski" : "The Lady of the Lake",
    "Andrzei Sapkowski" : "Season of Storms",
}

author = input("Choose one of the available authors: J. R. R, Tolkein, George R. R. Martin, Andrzei Sapkowski ")

titles = ""

for author in booksDict:
    titles.join(booksDict)

print(titles)

#doesn't work yet