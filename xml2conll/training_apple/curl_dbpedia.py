#!/usr/bin/python3

## Author: Daan Disselhorst
## Usage: call python file in terminal
## Summary: this program will take annotated xml files in a folder
## from spotlight and will look up the corresponding named entity labels

from xml.dom.minidom import parse
import xml.dom.minidom
import urllib.request, urllib.error, urllib.parse
import glob
import os
import csv

def curlxml (filename,newCount):

	# Open XML document using minidom parser
	DOMTree = xml.dom.minidom.parse(filename)
	annotation = DOMTree.documentElement

	# Get all the resource being annotated
	resource = annotation.getElementsByTagName("Resource")

	########
	rootElement = DOMTree.getElementsByTagName("Annotation")

	for annoDoc in rootElement:
		if annoDoc.hasAttribute("text"):
			originalText = annoDoc.getAttribute("text")

	# Get rid of escaper (previously used for double quotes)
	cleanedText = originalText.replace("\\","")
	textSplitted = cleanedText.split()

	# Initiate lists for URIs and surfaceForms
	URIlist = []
	surfaceFormList = []

	# Print URI and tokens.
	for res in resource:
	   if res.hasAttribute("URI") and res.hasAttribute("surfaceForm"):
	      
	      surfaceForm = res.getAttribute("surfaceForm")
	      URInl = res.getAttribute("URI")
	      # remove nl. in the URL (optional!)
	      URI = URInl.replace("nl.", "")
	      
	      # add all found resources to lists
	      URIlist.append(URI)
	      surfaceFormList.append(surfaceForm)
	      
	# Concatenate surfaceForm list with URIlist
	newList = list(zip(surfaceFormList, URIlist))

	# Initiate list where surfaceForms are to be splitted on whitespace
	spaceSplittedList = list()

	# Split list on spaces which are found in the surfaceForm (e.g. "Steve Jobs")
	# Make list of tuples and add URI to each splitted surfaceForm
	for key, value in newList:
		splitSpace1 = key.split()
		for item in splitSpace1:
			spaceSplittedList.append((item,value))
			
	# Initiate lists for eventual tab separated file
	column1 = []
	column2 = []
	column3 = []

	### Curl DBpedia ###

	# count number of xml files, why -1?
	number_files = len(os.listdir("../xml"))-1

	print("DBpedia is being curled, please have some patience...")
	print("[",newCount,"/",number_files,"] "+filename)

	for key, value in spaceSplittedList:
		try: 
			curlURI = value	
			curlIT = urllib.request.urlopen(curlURI)
			content = curlIT.read()
			content2 = content.decode(encoding='utf-8',errors='ignore')

			# PRODUCT
			if "rel=\"rdf:type\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" href=\"http://dbpedia.org/ontology/Product\"An Entity of Type : <a href=\"http://dbpedia.org/ontology/Work\">work</a>" in content2 or "rel=\"rdf:type\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" href=\"http://dbpedia.org/ontology/MeanOfTransportation\"><small>dbo</small>:MeanOfTransportation</a>" in content2 or "href=\"http://dbpedia.org/ontology/Software\"><small>dbo</small>:Software</a>" in content2 or "href=\"http://dbpedia.org/ontology/InformationAppliance\"><small>dbo</small>:InformationAppliance</a>" in content2 or "http://umbel.org/umbel/rc/PhysicalDevice" in content2 or "href=\"http://dbpedia.org/ontology/Device\"><small>dbo</small>:Device" in content2 or "http://dbpedia.org/class/yago/Device100171249" in content2 or "http://dbpedia.org/class/yago/Device103183080" in content2 or "http://dbpedia.org/class/yago/Device103185562" in content2 or "http://dbpedia.org/class/yago/Device103185746" in content2 or "http://dbpedia.org/class/yago/Device107068844" in content2 or "http://dbpedia.org/class/yago/Product104007894" in content2 or "http://dbpedia.org/class/yago/Product111415842" in content2 or "http://dbpedia.org/class/yago/Product114997699" in content2 or "http://dbpedia.org/class/yago/Product104007894" in content2 or "http://dbpedia.org/class/yago/Artifact100021939" in content2 or "http://schema.org/Product" in content2 or "http://dbpedia.org/ontology/Food" in content2 or "http://www.wikidata.org/entity/Q2095" in content2 or "https://www.wikidata.org/wiki/Q1067263" in content2 or "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#FunctionalSubstance" in content2 or "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#DesignedArtifact" in content2 or "http://schema.org/CreativeWork" in content2:
				splitSpace = key.split()
				for item in splitSpace:
					column1.append(item)
					column2.append("(PRO)")
					column3.append(value)			
			
			# ORGANISATION		
			elif "rel=\"rdf:type\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" href=\"http://dbpedia.org/ontology/Organisation\"" in content2 and "href=\"http://www.w3.org/2002/07/owl#Thing\"><small>owl</small>:Thing</a>" in content2 or "rel=\"rdf:type\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" href=\"http://dbpedia.org/ontology/Company\"><small>dbo</small>:Company</a>" in content2 or "http://dbpedia.org/class/yago/Company108058098" in content2 or "http://dbpedia.org/class/yago/Company108077711" in content2 or "http://dbpedia.org/class/yago/Company108184861" in content2 or "http://dbpedia.org/class/yago/Company108187033" in content2 or "http://dbpedia.org/class/yago/Company108214272" in content2 or "http://dbpedia.org/class/yago/Company113929588" in content2 or "http://dbpedia.org/class/yago/Organization101008378" in content2 or "http://dbpedia.org/class/yago/Organization101136519" in content2 or "http://dbpedia.org/class/yago/Organization104768657" in content2 or "http://dbpedia.org/class/yago/Organization108008335" in content2 or "http://dbpedia.org/class/yago/Enterprise100796886" in content2 or "http://dbpedia.org/class/yago/Enterprise104836074" in content2 or "http://dbpedia.org/class/yago/Enterprise108056231" in content2 or "http://dbpedia.org/class/yago/Firm108059870" in content2 or "http://dbpedia.org/class/yago/Business101096245" in content2 or "http://dbpedia.org/class/yago/Business105833022" in content2 or "http://dbpedia.org/class/yago/Business105983801" in content2 or "http://dbpedia.org/class/yago/Business107966927" in content2 or "http://dbpedia.org/class/yago/Business108061042" in content2 or "http://dbpedia.org/class/yago/Venture100797878" in content2 or "http://dbpedia.org/class/yago/Venture101117164" in content2 or "http://umbel.org/umbel/rc/Business" in content2 or "http://umbel.org/umbel/rc/Organization" in content2 or "http://schema.org/Organization" in content2 or "http://www.wikidata.org/entity/Q43229" in content2:
				splitSpace = key.split()
				for item in splitSpace:
					column1.append(item)
					column2.append("(ORG)")
					column3.append(value)	
			
			# LOCATION		
			elif "rel=\"rdf:type\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" href=\"http://dbpedia.org/ontology/Location\"" in content2 or "href=\"http://dbpedia.org/ontology/Country\"><small>dbo</small>:Country" in content2 or "http://dbpedia.org/class/yago/Continent109254614" in content2 or "http://dbpedia.org/class/yago/Country108544813" in content2 or "http://dbpedia.org/class/yago/Country108644722" in content2 or "http://dbpedia.org/class/yago/Nation108166552" in content2 or "http://dbpedia.org/class/yago/Nation108303692" in content2 or "http://dbpedia.org/class/yago/Region105997814" in content2 or "http://dbpedia.org/class/yago/Region108630039" in content2 or "http://dbpedia.org/class/yago/Region108630985" in content2 or "http://dbpedia.org/class/yago/Region113759146" in content2 or "http://dbpedia.org/class/yago/City108226335" in content2 or "http://dbpedia.org/class/yago/City108524735" in content2 or "http://dbpedia.org/class/yago/City108540903" in content2 or "http://dbpedia.org/class/yago/Location100027167" in content2 or "http://dbpedia.org/class/yago/Location103682189" in content2 or "http://dbpedia.org/class/yago/Economy108366753" in content2 or "http://dbpedia.org/class/yago/Economy105644727" in content2 or "http://dbpedia.org/class/yago/Economy104893787" in content2 or "http://dbpedia.org/class/yago/Economy100192613" in content2 or "http://dbpedia.org/class/yago/State108168978" in content2 or "http://dbpedia.org/class/yago/State100024720" in content2 or "http://dbpedia.org/class/yago/State108178547" in content2 or "http://dbpedia.org/class/yago/State108654360" in content2 or "http://dbpedia.org/class/yago/State113988498" in content2 or "http://dbpedia.org/class/yago/WorldOrganization108294696" in content2 or "http://dbpedia.org/class/yago/YagoGeoEntity" in content2 or "http://schema.org/Country" in content2 or "http://schema.org/Place" in content2 or "http://www.wikidata.org/entity/Q3455524" in content2 or "http://www.wikidata.org/entity/Q486972" in content2 or "http://umbel.org/umbel/rc/PopulatedPlace" in content2 or "http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing" in content2:
				splitSpace = key.split()
				for item in splitSpace:
					column1.append(item)
					column2.append("(LOC)")
					column3.append(value)	
			
			# PERSON		
			elif "rel=\"rdf:type\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" href=\"http://dbpedia.org/ontology/Person\"" in content2 or "href=\"http://xmlns.com/foaf/0.1/Person\"><small>foaf</small>:Person" in content2 or "http://dbpedia.org/class/yago/Person100007846" in content2 or "http://dbpedia.org/class/yago/Person105217688" in content2 or "http://dbpedia.org/class/yago/Person106326797" in content2 or "http://schema.org/Person" in content2 or "http://www.wikidata.org/entity/Q215627" in content2 or "http://www.wikidata.org/entity/Q5" in content2:
				splitSpace = key.split()
				for item in splitSpace:
					column1.append(item)
					column2.append("(PER)")
					column3.append(value)	

			# FIN		
			elif "http://umbel.org/umbel/rc/Currency" in content2 or "http://dbpedia.org/class/yago/Currency113385913" in content2 or "http://dbpedia.org/class/yago/Currency104765586" in content2 or "stock market index" in content2 or "stock market indices" in content2:
				splitSpace = key.split()
				for item in splitSpace:
					column1.append(item)
					column2.append("(FIN)")
					column3.append(value)	
					
			else:
				splitSpace = key.split()
				for item in splitSpace:
					column1.append(item)
					column2.append("_")
					column3.append("_")
		
		# Error handling, n/a URL and special char mis-encoding
		except (urllib.error.HTTPError, urllib.error.URLError, UnicodeEncodeError) as err:
			splitSpace = key.split()
			for item in splitSpace:
				column1.append(item)
				column2.append("_")
				column3.append("_")


	# print contents of xml and annotated entities
	#print("\n")
	#print(textSplitted)
	#print("\n")
	#print(column1)
	#print("\n")
	
	# initiate counters
	i = 0
	j = 0

	# we have to compare annotated entities (column1) with contents xml
	while j < len(column1):
		# if entity is same (as surfaceForm) do nothing, since they are already labeled!
	    if textSplitted[i] == column1[j]:
	        i+=1
	        j+=1
	    # if entity is not the same (as surfaceForm), no annotation has been performed, add underscore char
	    elif textSplitted[i] != column1[j]:
	        column2.insert(i,"_")
	        column3.insert(i,"_")
	        i+=1

	while i < len(textSplitted):
	    column2.append("_")
	    column3.append("_")
	    i+=1


	# write three columns to csv file
	with open('../output/'+filename+'.ne', 'w') as f:
		writer = csv.writer(f, delimiter='\t')
		writer.writerows(zip(textSplitted,column2,column3))

	# confirm file written
	print("File written! \n")

def main():
	# choose correct directory
	os.chdir("xml")
	# for every xml file do curl xml
	# pass counter for counting status
	newCount = 0
	for file in glob.iglob("*.xml"):
		newCount+=1
		curlxml (file,newCount)


if __name__ == "__main__":
    main()

