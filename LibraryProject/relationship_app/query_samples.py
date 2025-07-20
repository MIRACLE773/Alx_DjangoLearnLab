import os
import django
import sys

# Add base directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Setup Django
django.setup()

# Now import your models
from relationship_app.models import Author, Book

# Example query
authors = Author.objects.all()
for author in authors:
    print(author.name)

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query 1: Get all books by a specific author
    author_name = "Some Author Name"  # Change this to an actual Author's name
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # Query 2: List all books in a specific library
    library_name = "Some Library Name"  # Change to an actual Library name
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in library '{library_name}':")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # Query 3: Retrieve the librarian for a specific library
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"\nLibrarian of library '{library_name}': {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for library '{library_name}'")

if __name__ == '__main__':
    run_queries()
