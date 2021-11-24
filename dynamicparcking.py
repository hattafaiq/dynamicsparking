def main():
    #slot=0
    while True:
        #global slot
        lahan=0
        inputan=""
        slot={1,2,4,5,6,7,11,12,13}
        inputan=input("masukan jumlah mobil= ")
        slot.add(int(inputan))
        jumlah=slot
        print(jumlah)
        
if __name__ == '__main__':
    main()