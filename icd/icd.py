class ICD():

    icd_datas = open('icd.txt').readlines()

    def __init__(self, icd):
        self.icd = icd
        self.label = icd[:1]
        self.detail = icd[9:]

    def get_icd_label(self):
        return self.label

    def get_icd_detail(self):
        return self.detail

    def get_detail_by_icd(self):
        for icd_data in self.icd_datas:
            if icd_data[:1] == self.label:
                return icd_data[9:].strip()
