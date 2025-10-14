# generate_report.py
import json, csv, sys
from datetime import datetime

def load_results(path):
    with open(path,'r',encoding='utf-8') as f:
        return json.load(f)

def prioritize(item):
    sev = item.get('severity','medium')
    return {'critical':1,'high':2,'medium':3,'low':4}.get(sev,3)

def generate(results, out='bugs_report.csv'):
    rows = []
    for r in results:
        rows.append([r.get('id'), r.get('title'), r.get('severity'), r.get('status'), r.get('created')])
    rows.sort(key=lambda x: prioritize({'severity': x[2]}))
    with open(out,'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','title','severity','status','created'])
        writer.writerows(rows)
    print('Reporte generado:', out)

if __name__=='__main__':
    if len(sys.argv)<2:
        print('Uso: python generate_report.py sample_results.json')
    else:
        results = load_results(sys.argv[1])
        generate(results)
