from io import StringIO


def save_returns(books):
    log = StringIO()

    try:
        for book in books:
            log.write(str(book) + "\n")

        print("Books saved successfully")
        print("\nRETURNS LOG:")
        print(log.getvalue())

    except (OSError, TypeError) as error:
        print("File error:", error)
    finally:
        log.close()
        print("File processing completed")


books = [
    "Python Book",
    "DBMS Book",
    "C Programming Book",
]

save_returns(books)