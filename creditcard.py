
from __future__ import division
import string

carta=[]

def Carta():
  stringa=input("Ricopia il numero della tua carta(compreso i trattini separatori)")
  stringa=stringa.split('-')
  carta_tmp=[]
  for i in stringa:
    for ele in i :
      carta_tmp.append(ele)
  if (len(carta_tmp)==16):
    return carta_tmp
  else:
    print ("Lunghezza del numero carta sbagliato!")
    carta_tmp=[]
    return carta_tmp
   


def Conteggio(carta):
  carta=Carta()
  tot=0
  pos=0
  for i in carta:
    if((pos%2)==0):
      if((i*2)>9):
        tmp=(int(i)*2)
        for z in str(tmp):
          tot=tot+int(z)
    else:
      tot=tot+int(i)
    pos=pos+1
  return tot



def Main():
  totale=Conteggio(carta)/10
  totale=str(totale)
  totale=totale.split('.')
  if (totale[1]=='0'):
    print("Carta Valida!") 
  else:
    print("Carta non Valida!") 


Main()