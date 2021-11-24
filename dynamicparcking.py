#def inputmobil(inputan):

def main():
    global lahan, inputan, jumlah, slot
    while True:
        lahan=[]
        for i in range(1,200):
            inputan=""
            jumlah=[]
            slot={1,2,4,5,6,7,11,12,13}
            inputan=input("masukan jumlah mobil")
            jumlah=slot.add(inputan)
            print(slot)
        
if __name__ == '__main__':
    main()