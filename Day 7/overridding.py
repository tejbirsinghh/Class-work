class employee:
    company="google"

    def showDetails(employee):
        print("employee block!")

class programeer(employee):
    language="python"
    company="youtube"   #overridding

    def getLanguage(self):
        print("the language is "+str(self.language))

    def showDetails(programmer):
        print("programmer block!") #overridding

ob=employee()
ob.showDetails()
p=programeer()
p.showDetails()
print(p.company)




