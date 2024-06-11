class placements:
    def info(self):
        print("This is grandmother")
class academics(placements):
    def idea(self):
        self.info()
        print("This is mother")
class Faculty(placements):
    def book(self):
        self.info()
        print('This is Me')
pen=Faculty()
paper=academics()
pen.book()
paper.idea()