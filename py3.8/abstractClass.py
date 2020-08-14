# HackerRank Day 13 Abstract Classes | Python

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCmethod):

    def __init__(self, author, title):
        self.author = author
        self.title = title

    @abstractmethod
    def display(): pass

  class MyBook(Book):

      def __init_(self, title, author, price):
          Book.__init__(self, author, title)
          self.price = price

      def display(self):
          print('Title: ', self.title)
          print('Author: ', self.author)
          print('Price: ', str(self.price))