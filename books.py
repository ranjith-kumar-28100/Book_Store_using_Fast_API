from fastapi import FastAPI,Body

app = FastAPI()
BOOKS= [{'title':'My Experiments with truth','author':'Mahatma Gandhiji','category':'Biography'},
        {'title':'Nehru ka story' ,'author':'Nehru','category':'Biography'},
        {'title':'The Alchemist','author':'Paulo Cohelo','category':'Fiction'},
        {'title':'Class - 11','author':'S  Chand','category':'Science'},
        {'title':'Class - 12','author':'RS Agarwal','category':'Maths'},
        {'title':'RD Sharma Physics','author':'RD Sharma','category':'Science'}]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_name}")
async def read_book_with_name(book_name):
        for book in BOOKS:
                if book['title'].casefold()==book_name.casefold():
                        return book
        return {}

@app.get("/books/withCategory/")
async def read_book_with_category(category:str):
        books_to_return =[]
        for book in BOOKS:
                if book['category'].casefold()==category.casefold():
                        books_to_return.append(book)
        return books_to_return

@app.get("/books/withCategory/{category}/")
async def read_book_with_given_category_and_author(category:str, author:str):
        books_to_return=[]
        for book in BOOKS:
                if book['category'].casefold() == category.casefold() and book['author'].casefold()==author.casefold():
                        books_to_return.append(book)
        return books_to_return

@app.get("/books/withAuthor/{author}/")
async def read_book_with_given_author(author:str):
        books_to_return=[]
        for book in BOOKS:
                if book['author'].casefold()==author.casefold():
                        books_to_return.append(book)
        return books_to_return

@app.post('/books/create')
async def add_book(new_book=Body()):
        BOOKS.append(new_book)
        return "Book added sucessfully"

@app.put('/books/update')
async def update_book(updated_book = Body()):
        for i in range(len(BOOKS)):
                if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
                        BOOKS[i]= updated_book
                        return "Sucessfully Updated"
        return "0 records updated"


@app.delete('/books/delete/{title}')
async def delete_book(title:str):
        for i in range(len(BOOKS)):
                if BOOKS[i].get('title').casefold()==title.casefold():
                        BOOKS.pop(i)
                        return "Book Deleted Sucessfully"
        return "0 records deleted"