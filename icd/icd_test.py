from icd import ICD
icd_code = 'A1223424'
code = ICD(icd_code)
code.get_detail_by_icd()

print(code.get_detail())
