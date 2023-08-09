books = {"Franz Kafka":"Der Prozess", 
         "Charles Dickens":"Eine Geschichte aus zwei Städten", 
         "J. K. Rowling":["Harry Potter und der Stein der Weisen", 
                          "Harry Potter und die Kammer des Schreckens", 
                          "Harry Potter und der Gefangene von Askaban"]}


#
print(type(books.keys()))
for key in books.keys():
    print(key)
#
print(type(books.values()))
for value in books.values():
    print(value)
# 
print(type(books.items()))
for item in books.items():
    print(item)