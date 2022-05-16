# AMIdataset
Il respository contenente i versi analizzati dei testi dell'archivio metrico italiano all'interno delle cartella dataset in formato `.csv`. 

I dati sono strutturati seguento il seguente schema:

| sigla      | sottogruppo | numero_del_verso | metro   | schema_metrico | congedo | tipo_verso | trascrizione_verso                    | accento_01 | accento_02 | accento_03 | accento_04 | accento_05 | accento_06 | accento_07 | accento_08 | accento_09 | accento_10 | irregolarità |
|------------|-------------|------------------|---------|----------------|---------|------------|---------------------------------------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|--------------|
| Purgatorio |           1 |                1 | sonetto | ABBD           | ABBC    |         11 | A ciascun’alma presa e gentil core    | 1          | 1          | 0          | 1          | 0          | 1          | 0          | 1          | 0          | 0          | ipometro     |
| Purgatorio |           1 |                2 | sonetto | ABBD           | ABBC    |          7 | nel cui cospetto ven lo dir presente, | 0          | 1          | 0          | 1          | 0          | 0          | 0          | 0          | 0          | 0          | ipermetro    |

Gli header dei file riportano i metadata usando i termini proposti da [DublinCore](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)

## Segnalare errori nel dataset
Gli errori presenti nel dataset possono essere segnalati in due diversi modi:
 - Aprendo un nuovo `issue` nella sezione `issues` (sotto il nome del repository).
 - I file recenti dispongono nell'intestazione di un campo `#dc:source`	contenente il link ad un folgio di calcolo dove il correttore può segnalare l'errore commentando le celle in cui si verifica.

## Coreggere errori presenti nel dataset
Dopo essersi registrati gratuitamente su GitHub, è possibile correggere errori direttamente sui file `.csv`, selezionando il relativo file all'interno della cartella dataset e cliccando sull'icona ✏️`edit this file` (in alto a destra). In questo caso verrà creata una copia del repository su cui l'utente esterno al progetto può operare liberamente, qual'ora si volesse che le modifiche vengano integrate nel repository ufficiale creare una nuova [pull-request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) che potrà essere vagliata dal comitato scientifico del progetto.

## Collaborare all'archivio
È inoltre possibile collaborare nell'inserimento di nuovi testi, secondo il formato proposto da AMI, per agevolare l'utilizzo del formato proposto è possibile fare una copia del seguente [spreadsheet](https://docs.google.com/spreadsheets/d/1psXBmH2jdZQWsEPhh27vEuBPESPz9ZCIlnotYNDUW_U/edit?usp=sharing) e compilando tutti i campi neccessari.

Una volta terminata la scedatura esportare il file in `.csv` File -> Download -> Comma Separated Values (.csv). Rinominare il file con la seguente nomenclatura  `nomeautore_titolo_CognomeAutoreEdizioneAnno.csv` per esempio `Anonimo_Rime_DiGirolamo2008.csv` dove DiGirolamo è il cognome dell'autore dell'edizione di riferimento e 2008 e la data di pubblicazione dell'edizione di riferimento. Cliccare sulla cartella dataset e trasportare e rilasciare il file al suo interno. Cliccare su `commit changes`

> **N.B** Richieste non conformi al formato indicato non possono essere accettate. 
> Il comitato scientifico si riserva il diritto di decidere se ammettere il contributo. 
