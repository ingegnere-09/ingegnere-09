#import
import datetime as dm
import time

#liste e var
mater = []
n_mat = 0
now= 0
fine = ""
ore = 0
minuti = 0
tempm = 0
temph = 0
txma = 0

#funzioni

def output():
    
    #dichiaro globali
    global mater, n_mat, now, fine, ore, minuti, tempm, temph, txma
    
    #inizio funzione
    
    #conta materie
    n_mat = len(mater)
    
    print("\nA che ora vorresti finire?(metti 0.5 per indicare ore e mezza; inserisci il valore in ore)")
    fine = input(">")
    fine = float(fine)
    
    #calcola quanto tempo si ha fino all'ora indicata
    now = dm.datetime.now()
    ore = now.hour
    minuti = now.minute
    
    tempm = (fine - ore - (minuti/60))* 60
    
    if tempm > 60:
        while True:
            if tempm < 60:
                break
            tempm = tempm -60
            temph = temph + 1
    
    #calcola quanto tempo x materia (il*60 serve perchè prima ho alterato il valore.)
    txma = (tempm + (temph*60))/n_mat
    
    #output    
    print(f"\nHai {round(temph, 1)} ore e {round(tempm, 1)} minuti per fare i compiti")
    print(f"Devi usare {round(txma, 1)} per materia.\n")
    
def guida():    
        
    #dichiaro globali
    global mater, n_mat, txma
    
    #inizio funzione (uso un while in modo da fermare quando voglio)
    
    while True:
        if n_mat > 5:
            print("Non puoi superare 5 compiti, se vuoi sviluppa il codice.")
        
        ########################################################################
        if (n_mat -1)  < 0:
            print("\nFinito!\n")
            break
        
        print(f"\nIniza a fare {mater[0]}")
        time.sleep(60*(3/4*txma))
        print(f"\nFinisci di fare {mater[0]}")
        time.sleep(60*(1/4*txma))
        print("________________________________________________________________")
        
        ########################################################################
        if (n_mat -1)  < 1:
            print("\nFinito!\n")
            break
        
        print(f"\nIniza a fare {mater[1]}")
        time.sleep(60*(3/4*txma))
        print(f"\nFinisci di fare {mater[1]}")
        time.sleep(60*(1/4*txma))
        print("________________________________________________________________")
        
        ########################################################################
        if (n_mat -1) < 2:
            print("\nFinito!\n")
            break
        
        print(f"\nIniza a fare {mater[2]}")
        time.sleep(60*(3/4*txma))
        print(f"\nFinisci di fare {mater[2]}")
        time.sleep(60*(1/4*txma))
        print("________________________________________________________________")
        
        ########################################################################
        
        if (n_mat -1)  < 3:
            print("\nFinito!\n")
            break
        
        print(f"\nIniza a fare {mater[3]}")
        time.sleep(60*(3/4*txma))
        print(f"\nFinisci di fare {mater[3]}")
        time.sleep(60*(1/4*txma))
        print("________________________________________________________________")
        
        ########################################################################
        
        if (n_mat -1)  < 4:
            print("\nFinito!\n")
            break
        
        print(f"\nIniza a fare {mater[4]}")
        time.sleep(60*(3/4*txma))
        print(f"\nFinisci di fare {mater[4]}")
        time.sleep(60*(1/4*txma))
        print("________________________________________________________________")
        
        ########################################################################
        
        if (n_mat -1)  < 5:
            print("\nFinito!\n")
            break
        
        print(f"\nIniza a fare {mater[5]}")
        time.sleep(60*(3/4*txma))
        print(f"\nFinisci di fare {mater[5]}")
        time.sleep(60*(1/4*txma))
        print("________________________________________________________________")
        
        ########################################################################
        
            
#inizio codice
print("\n\nInserisci i compiti che devi fare, (invia 'f' per termianere).\n")

while True:
    a = input(">")
    
    if a != "f":
        mater.append(a)
    else:
        output()
        
        #chiede se vuole la guida
        print("Vuoi attivare la guida x fare svolgere le attività? (s/n)?")
        b = input(">")
        if b == "s":
            guida()
            break
        else:
            break
