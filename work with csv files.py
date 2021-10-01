from urllib import request


def s(d):
    response = request.urlopen(d)
    rea=response.read()
    stri=str(rea)
    lines=stri.split('\\n')
    goo=r'fef.csv'
    fw=open(goo,'w')
    for line in lines:
        fw.write(line+'\n')
    fw.close()
    dd = list(goo)
    if 'government' in dd:
        print('find')
s('https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional-csv.csv')



