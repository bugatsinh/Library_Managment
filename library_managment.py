import json

def Add_Book():
    name = input('Enter the name of Book you want to Add: ')
    author = input('Enter the name of the author: ')
    book_data = {'Book_name':name,'author':author,'status':'available'}
    with open('books.json','r') as f:
        content = f.read()
        book_brock = json.loads(content)
        book_brock.append(book_data)
        with open('books.json','w') as f:
            f.write(f'{json.dumps(book_brock)}')
    print('Book added succesfully')

def View_books():
    with open('books.json','r') as f:
        content = f.read()

        data_book = json.loads(content)
        for line in data_book:
            print(f'book: {line['Book_name']} author: {line['author']} status: {line['status']}\n')

def borow_book():
    book_name = input('Enter the name of book you want: ')
    with open('books.json','r') as f:
        content = f.read()
        # print(data_book)
        data_book = json.loads(content)
        # print(data_book)
        # print(type(data_book))
        for line in data_book:
            if book_name == line['Book_name']:
                if line['status'] == 'available':
                    print('book borowed succesfully')
                    author = line['author']
                    data_book.remove(line)
                    data_dict = {'Book_name':book_name,'author':author,'status':'unavailable'}
                    data_book.append(data_dict)
                    with open('books.json','w') as f:
                        f.write(f'{json.dumps(data_book)}')
                elif line['status'] == 'unavailable':
                    print('book is alrady borowed')
                
def return_book():
    book_name = input('Enter the name of book you want: ')
    with open('books.json','r') as f:
        content = f.read()
        # print(data_book)
        data_book = json.loads(content)
        # print(data_book)
        # print(type(data_book))
        for line in data_book:
            if book_name == line['Book_name']:
                if line['status'] == 'unavailable':
                    print('book returned succesfully')
                    author = line['author']
                    data_book.remove(line)
                    data_dict = {'Book_name':book_name,'author':author,'status':'available'}
                    data_book.append(data_dict)
                    with open('books.json','w') as f:
                        f.write(f'{json.dumps(data_book)}')
                elif line['status'] == 'available':
                    print('book is alrady persent please try add function')

def search_book():
    search_book_Name = input('ENTER the name of book: ')
    with open('books.json','r') as f:
        content = f.read()
        data_book = json.loads(content)
        for line in data_book:
            if search_book_Name in line['Book_name']:
                print(f"book name: {line['Book_name']}\n auther: {line['author']}\n status: {line['status']}")


while True:
    system = input('''  1. for adding books
    2. for viewing books
    3. for borowing books
    4. for returning books
    5. for searching books
    6. for exit\n:''')

    if system == '1':
        Add_Book()
    elif system == '2':
        View_books()
    elif system == '3':
        borow_book()
    elif system == '4':
        return_book()
    elif system == '5':
        search_book()
    elif system == '6':
        break
    else:
        print('invalid input')
