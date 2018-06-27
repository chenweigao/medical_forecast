class ICD():
    filepath = 'icd/icd.txt'
    icd_file = open(filepath)
    icd_datas = open(filepath).readlines()
    icd_dict = {}

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

    def get_detail(self):
        for line in self.icd_file:
            label, detail = line.split(" ", 1)
            self.icd_dict[label[:1]] = detail.strip()
        return self.icd_dict[self.label]
