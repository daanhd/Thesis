# XML2ConLL



Directory 'input_data'
----------------------
Bevat originele data in conll formaat, scripts om de tweede kolom te exporteren naar txt-bestand en een script om de webservice van Spotlight te bevragen, met als output XML bestanden.

Directory 'xml'
----------------------
Output van Spotlight, recognition en wikification.

Bestand 'curl_dbpedia.py'
----------------------
Neemt als input xml-bestanden en gaat DBpedia gebruiken om corresponderende rdf:types te vinden die kunnen worden ingedeeld tot een bepaald type entiteit. Output zijn geclassificeerde ConLL bestanden.

Directory 'output'
----------------------
Output van curl_dbpedia.py, scripts om witte regels weg te halen.
