import PyPDF2
import re
import urllib.request, urllib.parse, urllib.error
import requests
from datetime import date

dt = date.today()
YEAR = str(dt.year)
LAST_YEAR = str(int(dt.year)-1)
url = 'http://www.prograd.ufscar.br/calendarios/academico_presenciais_'+YEAR+'.pdf'
urllib.request.urlretrieve(url, 'academico_'+YEAR+'_unificado.pdf')

pdfFileObj = open('academico_'+YEAR+'_unificado.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
pageObj2 = pdfReader.getPage(1)


#remove o texto do calendario
string = pageObj.extractText() + pageObj2.extractText()
string = string.replace('\n','')
string = string.replace('Calendário','')
string = string.replace('Acadêmico','')
string = string.replace('Unificado','')
string = string.replace('Cursos Presenciais','')
string = string.replace('D ','')
string = string.replace('S ','')
string = string.replace('T ','')
string = string.replace('Q ','')
string = string.replace('JANEIRO','')
string = string.replace('FEVEREIRO','')
string = string.replace('MARÇO','')
string = string.replace('ABRIL','')
string = string.replace('MAIO','')
string = string.replace('JUNHO','')
string = string.replace('JULHO','')
string = string.replace('AGOSTO','')
string = string.replace('SETEMBRO','')
string = string.replace('OUTUBRO','')
string = string.replace('NOVEMBRO','')
string = string.replace('DEZEMBRO','')


#remove os dias do calendario
string = re.sub(' [0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+ ','', string)
string = re.sub(' [0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+ ','', string)
string = re.sub(' [0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+ ','', string)
string = re.sub(' [0-9]+ [0-9]+ [0-9]+ [0-9]+ ','', string)
string = re.sub(' [0-9]+ [0-9]+ [0-9]+ ','', string)
string = re.sub(' [0-9]+ [0-9]+ ','', string)
string = re.sub('    [0-9]+   ','', string)

string = string.replace(YEAR+'/1','AAAA')
string = string.replace(YEAR+'/2','BBBB')
string = string.replace(LAST_YEAR+'/1','CCCC')
string = string.replace(LAST_YEAR+'/2','DDDD')
string = string.replace(LAST_YEAR,'EEEE')
string = string.replace(YEAR,'FFFF')

#coloca um \n sempre que encontrar uma data
string = re.sub(r' ([0-9][0-9])',r'\n\1', string)

#corrige o caso do formato [0-9][0-9] a [0-9][0-9]
string = re.sub('a\n',r'a ', string)
string = re.sub('e\n',r'e ', string)

string = re.sub('  ',' ', string)

string = string.replace('AAAA',YEAR+'/1')
string = string.replace('BBBB',YEAR+'/2')
string = string.replace('CCCC',LAST_YEAR+'/1')
string = string.replace('DDDD',LAST_YEAR+'/2')
string = string.replace('EEEE',LAST_YEAR)
string = string.replace('FFFF',YEAR)

# print(string)
datas_bruto = string.split('\n')

meses = ('Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro','bob')
calendario = {}
mes = 0;
ultimo_dia = -1
calendario[mes] = []

for data in datas_bruto:
    if(data[0] != ' '):
        dia = data[0]+data[1]
        if(int(dia) < ultimo_dia):
            mes = mes + 1
            calendario[mes] = []
        calendario[mes].append((dia,data))
        ultimo_dia = int(dia)

print(calendario)
