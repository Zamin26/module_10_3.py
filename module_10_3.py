from random import randint, random                      # генерации случайного целого числа
import time                                             # функция sleep
import threading
from threading import Thread,Lock


class Bank:

    def __init__(self):
        self.lock = Lock()                              # блокировка потока
        self.balance = 0                                # баланс


    def deposit(self):
        for i in range(100):
            result = randint(50, 500)
            self.balance += result                      # пополнение баланса
            print(f'Пополнение: {result}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked() == 1:
                self.lock.release()                     # замок lock разблокирован
            time.sleep(0.001)                           # ожидание выполнения пополнения

    def take(self):
        for i in range(100):
            result = randint(50, 500)
            print(f'Запрос на {result}')
            if result <= self.balance:
                self.balance -= result                  # снятие средств
                print(f'Снятие: {result}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
            self.lock.acquire()
        time.sleep(0.001)                               # ожидание выполнения пополнения



bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

