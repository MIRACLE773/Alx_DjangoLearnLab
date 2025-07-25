from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # OPTIONAL: Clean up old data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create Author
    Author.objects.create(name="J.K. Rowling")

    # Get the author by name (required by ALX)
    author_name = "J.K. Rowling"
    fetched_author = Author.objects.get(name=author_name)

    # Create Book linked to fetched_author
    book = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=fetched_author)

    # Create Library
    Library.objects.create(name="Central Library")

    # Get the library by name (required by ALX)
    library_name = "Central Library"
    fetched_library = Library.objects.get(name=library_name)

    # Add book to library's books
    fetched_library.books.add(book)

    # Create Librarian linked to Library
    Librarian.objects.create(name="John Smith", library=fetched_library)

    #  Query all books by the specific author
    books_by_author = Book.objects.filter(author=fetched_author)
    print(f"Books by {fetched_author.name}: {[b.title for b in books_by_author]}")

    #  List all books in the library
    books_in_library = fetched_library.books.all()
    print(f"Books in {fetched_library.name}: {[b.title for b in books_in_library]}")

    # Get the librarian for the library (required by ALX)
    librarian = Librarian.objects.get(library=fetched_library)
    print(f"Librarian of {fetched_library.name}: {librarian.name}")
