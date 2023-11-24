class Nut:
    def __init__ (self, Key = None): # khoi tao phuong thuc init roi cho Key bang none la chu co gi ca
        self. khoa = khoa # dinh nghia thuoc tinh cho khoa = khoa
        self. trai = None # dinh nghia thuoc tinh cho nut trai = Nonen
        self. phai = None # dinh nghia thuoc tinh cho nut phai = none la chua co gi het
    #def
   # tai sao nut dau tien ko noi gi la self ? 
    
    # chuong hop neu nut do rong la nut dau tien
    def chen(self,khoa ):
        if Nut is None:
            nut = Nut(khoa)
            self = nut  
            return
        #if 
    #def        
    
        if khoa < self.khoa:
            if self.trai == None:
            self.trai = Nut(khoa)
        else: 
            self.trai.chen(khoa)  
        #if 
        elif khoa > self.khoa:
            if self.phai == None:
            self.phai = Nut(khoa)
        else:
            self.phai.chen(khoa)
        #if     
        else:
            print(f'Bi trung khoa {khoa}')
        #if 
    #def
#class

class CayNhiPhanTimKiem:
    def __init __(self, khoa= None):
        if khoa == None:
            self.goc = None 
        else: 
            self.goc = Nut(khoa)
        #if
    #Def 
    
    def chen(self, khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else:
            self.goc.chen(khoa)
        #if 
    #def

    def xoa(self, khoa)
        pass
    #def
    
    def duyet_trai_nut_phai(self, goc = 0 ):
        # duyet theo lnr
        
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if 
        
        if nut_ht == None:
            return []
        else: 
            kq = []
            
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for
            
            kq.append(nut_ht,khoa)
            
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for 
            
            return kq
        #if 
    #def
    
    
    
    def duyet_nut_trai_phai(self, goc = 0 ):
        # duyet theo nlr
        
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if 
        
        if nut_ht == None:
            return []
        else: 
            kq = []
            
            kq.append(nut_ht,khoa)
            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for
            
         
            
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for 
            
            return kq
        #if 
    #def
    
    def duyet_trai_phai_nut(self, goc = 0 ):
        # duyet theo LRN
        
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if 
        
        if nut_ht == None:
            return []
        else: 
            kq = []
            
            
            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for
            
         
            
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for 
            
            kq.append(nut_ht,khoa)
            
            return kq
        #if 
    #def 
    
    def tim(self, khoa):
        if self.goc == None:
            return
        #if
        
        nut_ht = self.goc
        kq = ''
        while ( nut_ht != None and nut_ht.khoa != khoa):
            kq = kq + f'{nut_ht.khoa} -> '
            if khoa <= nut_ht .khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai
            #if
        #while
        
        if nut_ht == None:
            return None
        else:
            kq = kq + f'{nut_ht.khoa}'
            return kq
        #if 
        
    #def           
#class

def main():
    SO_PHAN_TU = 10
    
    cay = CayNhiPhanTimKiem ()
    
    
    print('*** Chen vao cay')
    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri) < SO_PHAN_TU:
        gt = randint (1, 100)
        tap_gia_tri.add(gt)
    #while
    
    tap_gia_tri = list (tap_gia_tri)
    # tap_gia_tri = [66, 46, 84, 11, 81, 99, 36, 77, 83, 87, 100, 86, 85]
    
    print('chen la luot', tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)
    #for 
    
    kq = cay.duyet_trai_nut_phai()
    print('**** Duyet cay theo Trai-Nut-Phai (LNR):', Kq)
    
    kq = cay.duyet_trai_trai_phai()
    print('**** Duyet cay Nut-Trai-Phai (NLR):', Kq)
    
    
    kq = cay.duyet_trai_phai_Nut()
    print('**** Duyet cay Trai-Phai-Nut (LRN):', Kq)
    
    while True:
        nhap = input ('Nhap vao khoa can tim')
        if nhap == '':
            break
        #if  
        
        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print(f'khong tim thay {gt}')
        else
            print(f'Tim thay {gt}: {kq}')
        #if
    #while 
#def

if__name__ == '__main__':
    main ()
#if 

