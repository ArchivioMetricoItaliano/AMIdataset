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
        author = next(g)
        title = next(g)
        date = next(g)
        source1 = next(g)
        source2 = next(g)
        source3 = next(g)
        creator = next(g)
        contributor = next(g)
        provenance = next(g)
        publisher = next(g)
        pb = "#dc:publisher,Gruppo Padovano di Stilistica,,,# l'ente responsabile della schedatura,,,,,,,,,,,,,,\n"
        if publisher != pb:
            with open(os.path.join("dataset2",trascrizione),'w') as f2:
                f2.write(DEFINITIONS)
                f2.write(conformsTo)
                f2.write(identifier)
                f2.write(description)
                f2.write(author)
                f2.write(title)
                f2.write(date)
                f2.write(source1)
                f2.write(source2)
                f2.write(source3)
                f2.write(creator)
                f2.write(contributor)
                f2.write(publisher)
                f2.write(provenance)
                for i in g:
                    f2.write(i)  

                

