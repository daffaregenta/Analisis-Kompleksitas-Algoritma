import random
import time
import timeit
#import matplotlib.pyplot as plt
import sys 

#BUBLE SORT
def bubbleSort() :
    start = timeit.default_timer() #Start Waktu Eksekusi

    n = len(E10ribu) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if E10ribu[j] > E10ribu[j+1] : 
                E10ribu[j], E10ribu[j+1] = E10ribu[j+1], E10ribu[j]

    print ("Sort: Bubble Sort")
    print('====================') 
    for i in range(len(E10ribu)): 
        print ('Dataset ke-','%d' %E10ribu[i])
    print('Sort: Bubble Sort ')
    
    stop = timeit.default_timer() #Selesai Waktu Eksekusi
    lama_eksekusi = stop - start  #Dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'Detik')

#INSERTION SORT
def insertionSort() :
    start = timeit.default_timer() #Start Waktu Eksekusi

    for i in range(1, len(E10ribu)): 
        key = E10ribu[i] 
        j = i-1
        while j >=0 and key < E10ribu[j] : 
                E10ribu[j+1] = E10ribu[j] 
                j -= 1
        E10ribu[j+1] = key 
    
    print ("Insertion Sort:")
    print('====================')
    for i in range(len(E10ribu)): 
        print ('Dataset ke-',"%d" %E10ribu[i])
    print('Sort: Insertion Sort') 

    stop = timeit.default_timer() #Selesai Waktu Eksekusi
    lama_eksekusi = stop - start  #Dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'Detik')

#SELECTION SORT
def selectionSort() :
    start = timeit.default_timer() #start

    for i in range(len(E10ribu)): 
        min_idx = i 
        for j in range(i+1, len(E10ribu)): 
            if E10ribu[min_idx] > E10ribu[j]: 
                min_idx = j 
        E10ribu[i], E10ribu[min_idx] = E10ribu[min_idx], E10ribu[i] 

    print ("Selection Sort:")
    print('====================') 
    for i in range(len(E10ribu)): 
        print('Dataset ke-',"%d" %E10ribu[i]),
    print('Sort: Selection Sort ')
        
    stop = timeit.default_timer() #selesai
    lama_eksekusi = stop - start  #dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'detik')
        

#MERGE SORT
def merge(E10ribu, l, m, r) : 
    n1 = m - l + 1
    n2 = r- m 

    L = [0] * (n1) 
    R = [0] * (n2) 

    for i in range(0 , n1): 
        L[i] = E10ribu[l + i] 
  
    for j in range(0 , n2): 
        R[j] = E10ribu[m + 1 + j] 
  
    i = 0     
    j = 0     
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            E10ribu[k] = L[i] 
            i += 1
        else: 
            E10ribu[k] = R[j] 
            j += 1
        k += 1

    while i < n1: 
        E10ribu[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        E10ribu[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(E10ribu,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(E10ribu, l, m) 
        mergeSort(E10ribu, m+1, r) 
        merge(E10ribu, l, m, r) 

def printOut_Merge() :
    n = len(E10ribu)

    start = timeit.default_timer() #Start 

    mergeSort(E10ribu,0,n-1) 
    print ('Merge Sort: ') 
    print('=================')
    for i in range(n): 
        print ('Dataset ke-',"%d" %E10ribu[i])
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
    
    quicksort(E10ribu,0,len(E10ribu))
    print ('Quick Sort: ') 
    print('=================')
    for i in range(len(E10ribu)): 
        print ('Dataset ke-',"%d" %E10ribu[i])
    print('Sort: Quick Sort ')

    stop = timeit.default_timer() #Selesai
    lama_eksekusi = stop - start  #Dalam satuan detik 
    print('Lama eksekusi: ',lama_eksekusi,'Detik')    

    #print('Setelah sort:',E10ribu)

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

E10ribu = random.sample(range(1,10000+1),10000) #GENERATE RANDOM INT 1-10.000
n = len(E10ribu)
print('Menampilkan 10.000 Elemen Dataset: ')
print('---------------------------------')
for i in E10ribu : 
    print('Dataset: ',i)
print('10.000 Dataset')

stop = timeit.default_timer() #Selesai Waktu Eksekusi
lama_eksekusi = stop - start  #Dalam satuan detik 
print('Lama eksekusi: ',lama_eksekusi,'Detik')
print('============================= ')

menu() #def menu 
