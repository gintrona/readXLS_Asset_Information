import re
import os.path
from lxml import etree
from lxml.cssselect import CSSSelector

DIRECTORY = "vault/"

########
def writeToFile(date, DollarExchangeRate,fileName, dictElems, skipDateControl):

	try:
		##Capitalizacion en dolares
		capitalEnDolares = float(dictElems['capitaliMerc'])/DollarExchangeRate
		fullFileName = DIRECTORY+str(fileName)

		#open the file, create if it doesn't exist	
		if os.path.isfile(fullFileName):
			f = open(fullFileName, 'r')
			lines = f.readlines()
			##use strip in case month or month are one value
			lastDate = lines[len(lines)-1][0:10].strip()  
			if lastDate == date and not skipDateControl:
				print 'File ', fullFileName,'is up to date; nothing has been done'
				f.close()			
				return 		
			f = open(fullFileName, 'a')
		else:
			f = open(fullFileName, 'w')
			header = 'date'+'\t\t'+'precioMerc'+'\t'+'cantidadDisp'+'\t'+'capitaliMerc'+'\t'+'capitalDolares''\n'
			f.write(header)

		line = date+'\t'\
		+str(dictElems['precioMerc'])\
		+'\t\t'+str(dictElems['cantidadDisp'])\
		+'\t\t'+str(dictElems['capitaliMerc'])\
		+'\t\t'+str(capitalEnDolares)\
		+'\n'
		f.write(line)
		f.close()

	except:
		raise("Error while writing to files")

########
def formatNumber(number):
	aux_number = re.sub('\.','',str(number))
	return re.sub(',','.',aux_number)


########
def getDollarExchangeRate():
	try:	
		parser = etree.HTMLParser()
		tree = etree.parse('http://www.ambito.com/economia/mercados/monedas/dolar/',parser)
		sel 	= CSSSelector('div.columna1y2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > '\
		+'div:nth-child(3) > big:nth-child(1)')
		element = sel(tree)
		return float(re.sub(',' ,'.' , element[0].text))
	except:
		raise ValueError("Dollar Exchange rate not found")

