import queue
from threading import Thread
from time import sleep


class Table():
    def __init__(self, number):
        self.number = number
        self.is_busy = True


class Cafe():
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def customer_arrival(self):
        count = 1
        while count <= 20:
            self.serve_customer(count)
            sleep(1)
            count += 1

    def serve_customer(self, customer):
        print(f"Посетитель номер {customer} прибыл")
        for table in self.tables:
            if table.is_busy == True:
                table.is_busy = False
                print(f'Посетитель номер {customer} сел за стол {table.number}')
                Customer(self, customer, table).start()
                break
        else:
            self.queue.put(customer)
            print(f"Посетитель номер {customer} ожидает свободный стол")


class Customer(Thread):
    def __init__(self, cafe, customer, table):
        super().__init__()
        self.cafe = cafe
        self.customer = customer
        self.table = table

    def run(self):
        sleep(5)
        self.table.is_busy = True
        print(f"Посетитель номер {self.customer} покушал и ушёл")

        if not cafe.queue.empty():
            next_customer = self.cafe.queue.get()
            print(f"Посетитель номер {next_customer} сел за стол {self.table.number}")
            Customer(self.cafe, next_customer, self.table).start()




table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()

