from fileinput import lineno
import os
import csv
import warnings

trascrizioniAMI = sorted([i for i in os.listdir("dataset") if i.endswith('.csv')])

errori = []
def controlla_uguale(a,b,txt,trascrizione,linea=None):
    if a != b:
        errori.append("%s riga %s  - %s" % (trascrizione, linea,txt))

def controlla_numero_colonne(riga,trascrizione):
    if len(riga.split(',')) != 19:
        errori.append("%s riga %s  - Numero di colonne errato" % (trascrizione,riga))

def controlla_righa_cominci(riga,riferimento,trascrizione):
    if not riga.startswith(riferimento):
        errori.append("%s riga %s  - Riga non inizia con %s" % (trascrizione,riga,riferimento))

def campo_richiesto(campo,trascrizione,descrizione):
    if campo == "":
        errori.append("%s riga %s  - Campo mancante %s" % (trascrizione,campo,descrizione))

class DatasetValidationError(Exception):
    pass

testicontrollati = 0
for ind,trascrizione in enumerate(trascrizioniAMI):
    with open(os.path.join("dataset",trascrizione)) as g:
        idtesto= ind+1
        DEFINITIONS = next(g)
        d = '#DEFINITIONS,dc=http://purl.org/dc/elements/1.1/,,,,,,,,,,,,,,,,,\n'
        controlla_uguale(DEFINITIONS,d,"Il campo DEFINITIONS non corrisponde",trascrizione)
        controlla_numero_colonne(DEFINITIONS,trascrizione)
        conformsTo = next(g)
        c = '#dc:conformsTo,ami.it/dataformat,,,,,,,,,,,,,,,,,\n'
        controlla_uguale(conformsTo,c,"Il campo conformsTo non corrisponde a %s"%c,trascrizione)
        controlla_numero_colonne(conformsTo,trascrizione)
        identifier = next(g)
        controlla_righa_cominci(identifier,"#dc:identifier",trascrizione)
        #assert len(identifier.split('_')) == 3
        controlla_numero_colonne(identifier,trascrizione)
        description = next(g)
        controlla_righa_cominci(description,"#dc:description",trascrizione)
        controlla_numero_colonne(description,trascrizione)
        author = list(csv.reader([next(g)]))[0]
        campo_richiesto(author[0],trascrizione,'Autore')
        controlla_righa_cominci(author[0],"#dc:author",trascrizione)
        title = list(csv.reader([next(g)]))[0]
        controlla_righa_cominci(title[0],"#dc:title",trascrizione)
        campo_richiesto(title[0],trascrizione,'Titolo')
        date = next(g)
        source1 = list(csv.reader([next(g)]))[0]
        controlla_righa_cominci(source1[0],"#dc:source",trascrizione)
        spltsource = source1[1].split(',')
        if len(spltsource) < 2:
            #errori.append("%s riga %s  - source deve contenere l'edizione nel seguente formato Autore, anno e.g. Petrocchi, 1996    " % (trascrizione,source1))
            warnings.showwarning("%s riga %s  - source deve contenere l'edizione nel seguente formato Autore, anno e.g. Petrocchi, 1996    " % (trascrizione,source1[1]),DatasetValidationError,trascrizione,lineno=9)
        source2 = next(g)
        controlla_righa_cominci(source2,"#dc:source",trascrizione)
        if not source2[1].startswith('http://'):
            warnings.showwarning("Dovrebbe contenere un permalink all'edizione possibilmente usando il catalogo ICCU e.g. http://id.sbn.it/bid/MIL0749010",DatasetValidationError,trascrizione,lineno=10)
        source3 = next(g)
        controlla_righa_cominci(source3,"#dc:source",trascrizione)
        creator = next(g)
        controlla_righa_cominci(creator,"#dc:creator",trascrizione)
        contributor = next(g)
        controlla_righa_cominci(contributor,"#dc:contributor",trascrizione)
        provenance = next(g)
        controlla_righa_cominci(provenance,"#dc:provenance",trascrizione)
        publisher = next(g)
        pb = "#dc:publisher,Gruppo Padovano di Stilistica,,,# l'ente responsabile della schedatura,,,,,,,,,,,,,,\n"
        controlla_uguale(publisher,pb,"Il campo publisher  non corrisponde a %s"%pb,trascrizione)
        dateSubmitted = next(g)
        controlla_righa_cominci(dateSubmitted,"#dc:dateSubmitted",trascrizione)
        dateAccepted = next(g)
        controlla_righa_cominci(dateAccepted,"#dc:dateAccepted",trascrizione)
        reader = csv.DictReader(g)
        readerfieldsname = ['sigla',
                    'sottogruppo',
                    'numero_del_verso',
                    'metro',
                    'schema_metrico',
                    'congedo',
                    'tipo_verso',
                    'trascrizione_verso',
                    'accento_01',
                    'accento_02',
                    'accento_03',
                    'accento_04',
                    'accento_05',
                    'accento_06',
                    'accento_07',
                    'accento_08',
                    'accento_09',
                    'accento_10',
                    'irregolarità']
        campimancanti = list(set(readerfieldsname) - set(reader.fieldnames))
        campiaggiunti = list(set(reader.fieldnames) - set(readerfieldsname))
        if len(campiaggiunti) > 0 or len(campimancanti) > 0:
            errori.append("%s - Campi mancanti: %s Campi aggiunti: %s" % (trascrizione,campimancanti,campiaggiunti))
        for line,i in enumerate(reader):
            if not i['sigla'].isdigit():
                errori.append("%s riga %s  - Sigla non numerica: %s" % (trascrizione,line,i['sigla']))
            #i['sottogruppo']
            if not i['numero_del_verso'].isdigit():
                errori.append("%s riga %s  - Numero del verso non numerico: %s" % (trascrizione,line,i['numero_del_verso']))
            i['metro']
            i['schema_metrico']
            i['congedo']
            i['tipo_verso']
            # if not i['tipo_verso'].isdigit():
            #    errori.append("%s riga %s  - Numero del verso non numerico:%s " % (trascrizione,line,i['tipo_verso']))
            if i['trascrizione_verso'] == "":
                errori.append("%s riga %s  - Trascrizione verso non può essere vuota" % (trascrizione,line))
            if i['accento_01'] not in ['1','0']: errori.append("%s riga %s  - Accento 01 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_01']))
            if i['accento_02'] not in ['1','0']: errori.append("%s riga %s  - Accento 02 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_02']))
            if i['accento_03'] not in ['1','0']: errori.append("%s riga %s  - Accento 03 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_03']))
            if i['accento_04'] not in ['1','0']: errori.append("%s riga %s  - Accento 04 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_04']))
            if i['accento_05'] not in ['1','0']: errori.append("%s riga %s  - Accento 05 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_05']))
            if i['accento_06'] not in ['1','0']: errori.append("%s riga %s  - Accento 06 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_06']))
            if i['accento_07'] not in ['1','0']: errori.append("%s riga %s  - Accento 07 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_07']))
            if i['accento_08'] not in ['1','0']: errori.append("%s riga %s  - Accento 08 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_08']))
            if i['accento_09'] not in ['1','0']: errori.append("%s riga %s  - Accento 09 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_09']))
            if i['accento_10'] not in ['1','0']: errori.append("%s riga %s  - Accento 10 deve essere o 0 o 1 è %s" % (trascrizione,line,i['accento_10']))
            i['irregolarità']
        testicontrollati+=1

print("*********")
print("File controllati %s/%s" %(testicontrollati,len(trascrizioniAMI)))
print("*********")
if len(errori)>0:
    raise DatasetValidationError("\n".join(errori))