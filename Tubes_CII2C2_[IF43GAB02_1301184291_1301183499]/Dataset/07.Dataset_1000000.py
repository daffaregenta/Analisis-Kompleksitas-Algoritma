import random
import time
import timeit
#import matplotlib.pyplot as plt
import sys 

#BUBLE SORT
def bubbleSort() :
    start = timeit.default_timer() #Start Waktu Eksekusi

    n = len(E1juta) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if E1juta[j] > E1juta[j+1] : 
                E1juta[j], E1juta[j+1] = E1juta[j+1], E1juta[j]

    print ("Sort: Bubble Sort")
    print('====================') 
    for i in range(len(E1juta)): 
        print ('Dataset ke-','%d' %E1juta[i])
    print('Sort: Bubble Sort ')
    
    stop = timeit.default_timer() #Selesai Waktu Eksekusi
    lama_eksekusi = stop - start  #Dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'Detik')

#INSERTION SORT
def insertionSort() :
    start = timeit.default_timer() #Start Waktu Eksekusi

    for i in range(1, len(E1juta)): 
        key = E1juta[i] 
        j = i-1
        while j >=0 and key < E1juta[j] : 
                E1juta[j+1] = E1juta[j] 
                j -= 1
        E1juta[j+1] = key 
    
    print ("Insertion Sort:")
    print('====================')
    for i in range(len(E1juta)): 
        print ('Dataset ke-',"%d" %E1juta[i])
    print('Sort: Insertion Sort') 

    stop = timeit.default_timer() #Selesai Waktu Eksekusi
    lama_eksekusi = stop - start  #Dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'Detik')

#SELECTION SORT
def selectionSort() :
    start = timeit.default_timer() #start

    for i in range(len(E1juta)): 
        min_idx = i 
        for j in range(i+1, len(E1juta)): 
            if E1juta[min_idx] > E1juta[j]: 
                min_idx = j 
        E1juta[i], E1juta[min_idx] = E1juta[min_idx], E1juta[i] 

    print ("Selection Sort:")
    print('====================') 
    for i in range(len(E1juta)): 
        print('Dataset ke-',"%d" %E1juta[i]),
    print('Sort: Selection Sort ')
        
    stop = timeit.default_timer() #selesai
    lama_eksekusi = stop - start  #dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'detik')
        

#MERGE SORT
def merge(E1juta, l, m, r) : 
    n1 = m - l + 1
    n2 = r- m 

    L = [0] * (n1) 
    R = [0] * (n2) 

    for i in range(0 , n1): 
        L[i] = E1juta[l + i] 
  
    for j in range(0 , n2): 
        R[j] = E1juta[m + 1 + j] 
  
    i = 0     
    j = 0     
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            E1juta[k] = L[i] 
            i += 1
        else: 
            E1juta[k] = R[j] 
            j += 1
        k += 1

    while i < n1: 
        E1juta[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        E1juta[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(E1juta,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(E1juta, l, m) 
        mergeSort(E1juta, m+1, r) 
        merge(E1juta, l, m, r) 

def printOut_Merge() :
    n = len(E1juta)

    start = timeit.default_timer() #Start 

    mergeSort(E1juta,0,n-1) 
    print ('Merge Sort: ') 
    print('=================')
    for i in range(n): 
        print ('Dataset ke-',"%d" %E1juta[i])
    print('Sort: Merge Sort ')

    stop = timeit.default_timer() #Selesai
    lama_eksekusi = stop - start  #Dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'Detik')    

#QUICK SORT
def partition(l, bwh, atas):
    pivot = l[bwh]
    pos_batas = bwh+1
    for j in range(bwh+1,atas):
        if l[j] < pivot:
            l[pos_batas],l[j]=l[j],l[pos_batas]
            pos_batas += 1
    l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
    return pos_batas

def quicksort(l, bwh, atas):
    if atas <= bwh:
        return
    q = partition(l, bwh, atas)
    quicksort(l, bwh, q-1)
    quicksort(l, q, atas)
    return l

def printOut_Quick() :
    start = timeit.default_timer() #Start 
    
    quicksort(E1juta,0,len(E1juta))
    print ('Quick Sort: ') 
    print('=================')
    for i in range(len(E1juta)): 
        print ('Dataset ke-',"%d" %E1juta[i])
    print('Sort: Quick Sort ')

    stop = timeit.default_timer() #Selesai
    lama_eksekusi = stop - start  #Dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'Detik')    

    #print('Setelah sort:',E1juta)

#MENU
def menu() :
    print('Pilih Sorting: [1] Bubble Sort')
    print('               [2] Insertion Sort')
    print('               [3] Selection Sort')
    print('               [4] Merge Sort')
    print('               [5] Quick Sort')
    print('               [0] Exit')
    pil = input('Pilihan: ')
    if pil == '1' : 
        bubbleSort()
        print('============================= ')
        menu()
    elif pil == '2' :
        insertionSort()
        print('============================= ')
        menu()
    elif pil == '3' : 
        selectionSort()
        print('============================= ')
        menu()
    elif pil == '4' :
        printOut_Merge()
        print('============================= ')
        menu()
    elif pil == '5' :
        printOut_Quick()
        print('============================= ')
        menu()
    else:
        exit


#MAIN PROGRAM
start = timeit.default_timer() #Start Waktu Eksekusi

E1juta = random.sample(range(1,1000000+1),1000000) #GENERATE RANDOM INT 1-1.000.000
n = len(E1juta)
print('Menampilkan 1.000.000 Elemen Dataset: ')
print('---------------------------------')
for i in E1juta : 
    print('Dataset: ',i)
print('1.000.000 Dataset')

stop = timeit.default_timer() #Selesai Waktu Eksekusi
lama_eksekusi = stop - start  #Dalam satuan detik 
print('Lama eksekusi: ',lama_eksekusi,'Detik')
print('============================= ')

menu() #def menu 
