class Nut:
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None

    def chen(self, khoa):
        if self.khoa is None:
            self.khoa = khoa
        elif khoa < self.khoa:
            if self.trai is None:
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)
        elif khoa > self.khoa:
            if self.phai is None:
                self.phai = Nut(khoa)
            else:
                self.phai.chen(khoa)
        else:
            print(f'Bi trung khoa {khoa}')

class CayNhiPhanTimKiem:
    def __init__(self, khoa=None):
        self.goc = None
        if khoa is not None:
            self.goc = Nut(khoa)

    def chen(self, khoa):
        if self.goc is None:
            self.goc = Nut(khoa)
        else:
            self.goc.chen(khoa)

    def duyet_trai_nut_phai(self, goc=None):
        nut_ht = goc if goc else self.goc
        if nut_ht is None:
            return []
        else:
            kq = []

            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            kq.extend(kq_trai)

            kq.append(nut_ht.khoa)

            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            kq.extend(kq_phai)

            return kq

    def duyet_nut_trai_phai(self, goc=None):
        nut_ht = goc if goc else self.goc
        if nut_ht is None:
            return []
        else:
            kq = []

            kq.append(nut_ht.khoa)

            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            kq.extend(kq_trai)

            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            kq.extend(kq_phai)

            return kq

    def duyet_trai_phai_nut(self, goc=None):
        nut_ht = goc if goc else self.goc
        if nut_ht is None:
            return []
        else:
            kq = []

            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)
            kq.extend(kq_trai)

            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            kq.extend(kq_phai)

            kq.append(nut_ht.khoa)

            return kq

    def tim(self, khoa):
        if self.goc is None:
            return None

        nut_ht = self.goc
        kq = ''
        while nut_ht is not None and nut_ht.khoa != khoa:
            kq = f'{kq}{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai

        if nut_ht is None:
            return None
        else:
            kq = f'{kq}{nut_ht.khoa}'
            return kq

def main():
    SO_PHAN_TU = 10

    cay = CayNhiPhanTimKiem()

    print('*** Chen vao cay')
    tap_gia_tri = set()
    from random import randint

    for _ in range(SO_PHAN_TU):
        gt = randint(1, 100)
        tap_gia_tri.add(gt)

    tap_gia_tri = list(tap_gia_tri)

    print('Chen lan luot', tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)

    kq = cay.duyet_trai_nut_phai()
    print('**** Duyet cay theo Trai-Nut-Phai (LNR):', kq)

    kq = cay.duyet_nut_trai_phai()
    print('**** Duyet cay Nut-Trai-Phai (NLR):', kq)

    kq = cay.duyet_trai_phai_nut()
    print('**** Duyet cay Trai-Phai-Nut (LRN):', kq)

    while True:
        nhap = input('Nhap vao khoa can tim: ')
        if nhap == '':
            break

        gt = int(nhap)
        ket_qua_tim_kiem = cay.tim(gt)
        if ket_qua_tim_kiem is None:
            print(f'Khong tim thay {gt}')
        else:
            print(f'Tim thay {gt}: {ket_qua_tim_kiem}')

if __name__ == '__main__':
    main()
