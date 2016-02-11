import PyPDF2
import re

pdfFileObj = open('academico_2015_unificado.pdf', 'rb')
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

string = string.replace('2015/1','AAAA')
string = string.replace('2015/2','BBBB')
string = string.replace('2014/1','CCCC')
string = string.replace('2014/2','DDDD')
string = string.replace('2014','EEEE')
string = string.replace('2015','FFFF')

#coloca um \n sempre que encontrar uma data
string = re.sub(r' ([0-9][0-9])',r'\n\1', string)

#corrige o caso do formato [0-9][0-9] a [0-9][0-9]
string = re.sub('a\n',r'a ', string)
string = re.sub('e\n',r'e ', string)

string = re.sub('  ',' ', string)

string = string.replace('AAAA','2015/1')
string = string.replace('BBBB','2015/2')
string = string.replace('CCCC','2014/1')
string = string.replace('DDDD','2014/2')
string = string.replace('EEEE','2014')
string = string.replace('FFFF','2015')

datas_bruto = string.split('\n')

meses = ('Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
calendario = {}
mes = 0;
ultimo_dia = -1
calendario[meses[mes]] = []

for data in datas_bruto:
    if(data[0] != ' '):
        dia = data[0]+data[1]
        calendario[meses[mes]].append((dia,data))
        if(int(dia) < ultimo_dia):
            mes = mes + 1
            calendario[meses[mes]] = []

print(calendario)
