from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
    {'title': 'Title Seven', 'author': 'Author Six', 'category': 'fiction'},
    {'title': 'Title Eight', 'author': 'Author Seven', 'category': 'fiction'},
    {'title': 'Title Nine', 'author': 'Author Eight', 'category': 'biography'},
    {'title': 'Title Ten', 'author': 'Author One', 'category': 'history'},
    {'title': 'Title Eleven', 'author': 'Author Three', 'category': 'science'},
    {'title': 'Title Twelve', 'author': 'Author Two', 'category': 'biography'},
    {'title': 'Title Thirteen', 'author': 'Author Nine', 'category': 'technology'},
    {'title': 'Title Fourteen', 'author': 'Author Ten', 'category': 'technology'},
    {'title': 'Title Fifteen', 'author': 'Author Five', 'category': 'fiction'},
    {'title': 'Title Sixteen', 'author': 'Author Seven', 'category': 'history'},
    {'title': 'Title Seventeen', 'author': 'Author Four', 'category': 'fiction'},
    {'title': 'Title Eighteen', 'author': 'Author Eight', 'category': 'science'},
    {'title': 'Title Nineteen', 'author': 'Author Nine', 'category': 'math'},
    {'title': 'Title Twenty', 'author': 'Author Ten', 'category': 'biography'}
]

######### GET or READ #########

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = [] # 
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
        else:
            # return 404 if no books are found
            return {"error": "No books found in this category."}
    return books_to_return


# Get all books from a specific author using path or query parameters
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


######### POST or  Create#########

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


######### DELETE #########

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
