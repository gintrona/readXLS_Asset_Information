import openpyxl
import datetime
import auxiliary
import sys

def main(args):

	## this parameter allows to skip the date verification: do not update the file if the current date is the same as the 
	## date in the last row of the file	
	if int(args[0])==0 or int(args[0])==1  :	
		skipDateControl = True if int(args[0])==1 else False  
	else: 
		raise ValueError("Argument skipDateControl is neither 1 (skip) nor 0 (False)")

	## Date: DD/MM/YYYY
	now = datetime.datetime.now()
	currentDate = str(now.day)+'/'+str(now.month)+'/'+str(now.year)

	## open the workbook and read sheet1
	wb= openpyxl.load_workbook('detalle.xlsx')
	sheet=wb.get_sheet_by_name('Sheet1')

	## read from this row on
	it 	= 4
	dictDenomIsKey	= {}

	while True and sheet['A'+str(it)].value != None :
		try:	
			dictElem		= {}
			stringIt 		= str(it)
			denom 			= sheet['A'+stringIt].value
			dictElem['cantidadDisp']= auxiliary.formatNumber(sheet['C'+stringIt].value)
			dictElem['precioMerc'] 	= auxiliary.formatNumber(sheet['F'+stringIt].value)
			dictElem['capitaliMerc']= auxiliary.formatNumber(sheet['G'+stringIt].value)
			dictDenomIsKey[denom]	= dictElem		
			it=it+1
		except StopIteration:
			break

	## get Dollar Exhange Rate
	dollarExchangeRate =auxiliary.getDollarExchangeRate()

	# dispatch data to files
	for elem in dictDenomIsKey.keys():
		auxiliary.writeToFile(currentDate, dollarExchangeRate ,elem, dictDenomIsKey[elem], skipDateControl)

if __name__ == "__main__":
	try:
		main(sys.argv[1:])
	except ValueError as err:
		print "Error: Check arguments", err.args
