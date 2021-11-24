jumlah=""
slot=""
def main():
    slot={1,2,4,5,6,7,11,12,13}
    while True:
        jumlah=""
        lahan=0
        inputan=""   
        inputan=input("masukan jumlah mobil= ")
        slot.add(int(inputan))
        print(slot)
        #break
if __name__ == '__main__':
    main()