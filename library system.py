from collections import defaultdict, Counter
from datetime import datetime

class LibrarySystem:
    def __init__(self):
        # Use defaultdict to automatically create empty lists for new authors
        self.books_by_author = defaultdict(list)
        # Track book borrowing status
        self.borrowed_books = {}
        # Count genre popularity
        self.genre_counter = Counter()

    def add_book(self, title, author, genre):
        book_info = {
            'title': title,
            'genre': genre,
            'added_date': datetime.now().strftime('%Y-%m-%d')
        }
        self.books_by_author[author].append(book_info)
        self.genre_counter[genre] += 1
        print(f"Added: {title} by {author}")

    def list_books_by_author(self, author):
        if author in self.books_by_author:
            print(f"\nBooks by {author}:")
            for book in self.books_by_author[author]:
                print(f"- {book['title']} ({book['genre']})")
        else:
            print(f"No books found for {author}")

    def show_popular_genres(self):
        print("\nPopular Genres:")
        for genre, count in self.genre_counter.most_common():
            print(f"{genre}: {count} books")

# Demo usage
def main():
    library = LibrarySystem()
    
    # Add some sample books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    library.add_book("Python Programming", "John Smith", "Technical")
    library.add_book ("Beautiful Code", "John Smith", "Technical")
    library.add_book("1984", "George Orwell", "Fiction")
    
    # Show all books by an author
    library.list_books_by_author("John Smith")
    
    # Show genre statistics
    library.show_popular_genres()

if __name__ == "__main__":
    main()