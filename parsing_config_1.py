import json


#def parsing_config(fin, fout):
def parsing_config_read(fin):
    with open(fin) as f:
        dic = {}
        for row in f:
            row = row.strip('\n').split('=')
            if len(row) > 1:
                key = row[0]
                value = row[1]
                dic[key] = value
    
    return dic
        
"""                
        with open(fout, 'w') as f:
            f.write(json.dumps(dic, indent=4))
            print('ok')
"""            

def parsing_config_write(fout):
    with open(fout, 'w') as f:
        par = {
        'key1': 1,
        'key2': 2,
        'key3': 3,       
        'key4': 4     
              }
        f.write(json.dumps(par, indent=4))

    #return 'ok'


#print(parsing_config_write('us_out.json'))
#print(parsing_config_read('config.ini'))

 
