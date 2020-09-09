#Open the DNA.
inp = open("Datascience\Dates\Bacteria.fasta").read() 
inph = open("Datascience\Dates\human.fasta").read()
#Create a html arquive of the date.
out = open("Datascience\Dates\Bacteria.html", "w") 
outh = open("Datascience\Dates\human.html", "w")

#begin the counter of the only pars of A, T, C, G.
cont = {} 
conth = {}

#Create the pairs empty
for i in ['A', 'T', 'C', 'G']: 
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0
        conth[i+j] = 0

#The archive.fasta, have broken lines. This sketch correct the error.
inp = inp.replace("\n","") 
inph = inph.replace("\n","")

#Fills the number of pairs
for k in range(len(inp)-1): 
   cont[inp[k]+inp[k+1]] += 1 
for k in range(len(inph)-1):
   conth[inph[k]+inph[k+1]] += 1

#html
i = 1
for k in cont: 
    #Calculates the transparency of the blocks.
    transparency_b = cont[k]/max(cont.values()) 
    transparency_h = conth[k]/max(conth.values())
    #Making the block
    out.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparency_b)+"')>"+k+"</div>")
    outh.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparency_h)+"')>"+k+"</div>")
    
    if i%4 == 0: #Conditional of ordener the blocks.
        out.write("<div style='clear:both'></div>")
        outh.write("<div style='clear:both'></div>")
    i+=1 

#close the archives.
out.close() 
outh.close()


