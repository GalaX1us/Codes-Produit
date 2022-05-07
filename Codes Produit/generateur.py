nb = int(input("Combien voulez vous de code :"))
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cpt=0
with open("resultat.txt", "w") as fillout:
    while cpt<nb:
        fillout.write("{}{}{}{}{}{}\n".format(alphabet[(cpt//26**5)%26],alphabet[(cpt//26**4)%26],alphabet[(cpt//26**3)%26],alphabet[(cpt//26**2)%26],alphabet[(cpt//26)%26],alphabet[(cpt%26)]))
        cpt+=1
