from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # OPTIONAL: Clean up old data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create Author
    author = Author.objects.create(name="J.K. Rowling")

    # Create Book linked to Author
    book = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author)

    # Create Library
    library = Library.objects.create(name="Central Library")

    # Add book to library's books
    library.books.add(book)

    # Create Librarian linked to Library
    librarian = Librarian.objects.create(name="John Smith", library=library)

    # Query all books by an author
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[b.title for b in books_by_author]}")

    # List all books in a library
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[b.title for b in books_in_library]}")

    # Retrieve librarian for a library
    print(f"Librarian of {library.name}: {library.librarian.name}")
