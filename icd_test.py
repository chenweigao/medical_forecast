from icd import ICD

for line in open('icd.txt').readlines():
    code = ICD(line)
    result = code.get_icd_code()
    print(result)
