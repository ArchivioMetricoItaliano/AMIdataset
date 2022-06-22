import os 
import csv 
trascrizioniAMI = sorted([i for i in os.listdir("dataset") if i.endswith('.csv')])

for ind,trascrizione in enumerate(trascrizioniAMI):
    with open(os.path.join("dataset",trascrizione)) as g:
        print("*********")
        print(trascrizione)
        print("*********")
        idtesto= ind+1
        DEFINITIONS = next(g)
        conformsTo = next(g)
        identifier = next(g)
        description = next(g)
        desc = list(csv.reader([description]))[0]
        author = next(g) 
        aut = list(csv.reader([author]))[0][1]
        title = next(g)
        tit = list(csv.reader([title]))[0][1]
        date = next(g)
        source1 = next(g)
        source2 = next(g)
        source3 = next(g)
        creator = next(g)
        contributor = next(g)
        provenance = next(g)
        publisher = next(g)
        if desc[1] == "Fellowship Marco Praloran 2013":
            desc[1] = f"Trascrizione e analisi dei versi del componimento {tit} di {aut}. Fellowship Marco Praloran 2013. "
        else:
             desc[1] = f"Trascrizione e analisi dei versi del componimento {tit} di {aut}. Riadattato dall'archivio AMI originale. "
        with open(os.path.join("dataset2",trascrizione),'w') as f2:
            f2.write(DEFINITIONS)
            f2.write(conformsTo)
            f2.write(identifier)
            f2.write(",".join(desc)+"\n")
            f2.write(author)
            f2.write(title)
            f2.write(date)
            f2.write(source1)
            f2.write(source2)
            f2.write(source3)
            f2.write(creator)
            f2.write(contributor)
            f2.write(provenance)
            f2.write(publisher)
            for i in g:
                f2.write(i)  

                

