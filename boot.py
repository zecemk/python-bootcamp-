class Library:
	def __init__(self):
		self.file=open("books.txt","a+")
		
	def __del__(self):
		self.file.close()
	
	def list_books(self):
		self.file.seek(0)
		content=self.file.read()
		lines=content.splitlines()
		if len(lines)==0:
			print("There is not any data")
		else:
			for line in lines:
				elements=line.split(",")
				book_name=elements[0]
				book_author=elements[1]
				print("*Book name : "+book_name+"\nAuthor : "+book_author)
	def add_book(self):
		name=input("Enter the name of the book: ")
		author=input("Enter the author of the book: ")
		year=input("Enter the first release year of the book: ")
		page=input("Enter the number of the pages of the book: ")
		self.file.write(f"{name},{author},{year},{page}\n")
	
	def remove_book(self):
		book_remove=input("Enter the name of the book you want to remove from the file: ")
		book_names=[]
		self.file.seek(0)
		content=self.file.read()
		lines_list=content.splitlines()
		if len(lines_list)==0:
			print("There is not any data.")
		else:
			for line in lines_list:
				elements=line.split(",")
				book_names.append(elements[0])
		if book_remove in book_names:
			indeks=book_names.index(book_remove)
			complete=lines_list[indeks]
			new_content="".join(content.split(complete+"\n"))
			self.file.truncate(0)
			self.file.write(new_content)
		else:
			print("The book you want to delete doesn't occur in the list!")
lib=Library()
while True:
	a=input("***MENU***\n1)List Books\n2)Add Book\n3)Remove Book\nPress q to quit\n")
	if a=="1":
		lib.list_books()
	elif a=="2":
		lib.add_book()
	elif a=="3":
		lib.remove_book()
	elif a=="q":
		break
		
				
					
		
