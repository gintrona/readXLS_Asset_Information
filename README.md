# Read assets information from a XLS file

I'm a small (or rather tiny) and humble investor that holds some assets on the Buenos Aires' Stock exchange.
Even though I'm not very active, less than I'd like to, I like to keep track of each of the stocks in my portfolio.

So for each of the stocks I hold, I have a plain text file that contains a table with the date, the capital invested expressed both in local currency (pesos) and in US dollars in each row of it. 

One way to retrieve this information is to download a XLS file from my personal bank online account. This file doesn't contain the pesos-dollar exchange rate.

The program reads and parse the XLS file. It then looks for the pesos-dollar exchange rate in the online version of a local newspaper (www.ambito.com). In this case, a web page is parsed and the value is extracted from the DOM object. This value is used to express the stock's market price in US dollars.

In the final stage the plain text files (one for each stock) are updated with the corresponding data.



