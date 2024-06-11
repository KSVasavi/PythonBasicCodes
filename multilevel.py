class placements:
    def info(self):
        print("This is grandmother")
class academics(placements):
    def idea(self):
        self.info()
        print("This is mother")
class student(academics):
    def book(self):
        self.idea()
        print('This is Me')
pen=student()
pen.book()

