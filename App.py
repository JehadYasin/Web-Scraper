import requests
from pages.book_page import BookPage
from parsers.Book_parser import Parser
from bs4 import BeautifulSoup

def write_to_csv(books: list):
    with open('Books.csv', 'w') as file:
        bookcsv = []
        bookcsv.append('Name,Author,Year-Published,Link\n')
        for book in books:
            bookcsv.append(f'{book["name"]},{book["author"]},{book["year"]},{book["link"]}\n')
        file.writelines(bookcsv)
link = input("Enter the link of the webpage you want to scrap: ")

def new_func(link):
    page = requests.get(link).content
    return page

page = new_func(link)


bookobj = BookPage(page)

choice1 = input("Do you want to extract data to a CSV file?(Yes/No): \n")



if choice1.upper() == "YES":
    write_to_csv(bookobj.booklist)
    print("Data extracted to Books.csv successfully.....")
else:
    print("Ok, data will not be extracted")





