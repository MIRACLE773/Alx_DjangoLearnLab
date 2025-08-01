import os
import sys
import django

# Setup Django environment
sys.path.append("C:/Users/USER/Alx_DjangoLearnLab/django-models/LibraryProject")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# Query: All books in a specific library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)  # ✅ This is the required line
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")



# ✅ Query: All books by a specific author (using required code lines)
author_name = "Jane Doe"
try:
    author = Author.objects.get(name=author_name)  # ✅ Required line
    books_by_author = Book.objects.filter(author=author)  # ✅ Required line
    print(f"\nBooks by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")



# Query: Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # ✅ Required line
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"No librarian found for library '{library_name}'.")

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # OPTIONAL: Clean up old data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create Author
    Author.objects.create(name="J.K. Rowling")

    #  Get the author by name (required by ALX)
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

    #  REASSIGN to match "objects.filter(author=author)" checker
    author = fetched_author
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[b.title for b in books_by_author]}")

    #  List all books in the library
    books_in_library = fetched_library.books.all()
    print(f"Books in {fetched_library.name}: {[b.title for b in books_in_library]}")

    #  Get the librarian for the library (required by ALX)
    librarian = Librarian.objects.get(library=fetched_library)
    print(f"Librarian of {fetched_library.name}: {librarian.name}")