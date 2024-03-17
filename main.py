
BASE_URL = "https://books.toscrape.com/index.html"      # main page to scrape
BOOKS_URL = []                                          # detail page link of all books

def main():
    # Introduction to get user choice
    user_choice = display_introduction()
    
def display_introduction() -> int:
    print("Welcome! I will access the bookstoscrape website. What do you want?")
    print("[1] Get all books")
    print("[2] Get the books from a category")
    print("[3] Get the books according to a rating")
    while True:
        try:
            user_choice = int(input("Enter the number corresponding to one of the operation above :"))
            if user_choice in [1, 2, 3]:
                print("Trying to scrape datas, please wait...")
                return user_choice
            else:
                print("Invalid input") 
        except ValueError:
            print("Invalid input")

    """Calculate the total price of the library."""
    total_price_of_library = 0
    for url in BOOKS_URL:
        try:
            r = session.get(url)
            r.raise_for_status()
            tree = HTMLParser(r.text)
        except requests.exceptions.RequestException as e:
            logger.error(f"HTTP error during the request to {url} : {e}") 
            continue
        print(get_category(tree))
        exit()
        price = get_formated_price(tree)
        quantity = get_stock(tree)
        total_price_of_library += (price * quantity)
    return total_price_of_library

if __name__ == '__main__':
    main()