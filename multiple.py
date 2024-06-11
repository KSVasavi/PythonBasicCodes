class SubMarks:
    math=int(input("Enter paper marks of math"))
    de=int(input("Marks of design engg."))
    c=int(input("marks of c language"))
    eng=int(input("marks of english"))
class PractMarks:
    cpract=int(input("Enter practical marks c language"))
class Result(SubMarks,PractMarks):
    def total(self):
        if self.math>=40 and self.c>=50 and self.de>=50 and self.eng>=90 and self.cpract>=80:
            print("Pass")
        else:
            print("Backlog")
obj=Result()
obj.total()