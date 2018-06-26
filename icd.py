class ICD():
    def __init__(self, icd):
        self.icd = icd
        self.label = icd[:1]
        self.detail = icd[9:]

    def get_icd_label(self):
        return self.label

    def get_icd_detail(self):
        return self.detail

    def get_icd_code(self):
        return self.label + ',' + self.detail