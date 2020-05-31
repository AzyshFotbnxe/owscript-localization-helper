import json

def dict_gen(filename):
    out=dict()
    with open(filename, 'r', encoding='utf8') as filein:
        l1=filein.readline()
        while l1:
            if len(l1.strip()) > 0:
                l1=l1.strip()
                l2=filein.readline().strip()
                out[l1]=l2
            l1=filein.readline()
    return out

def pull_text(filename):
    out=[]
    with open(filename, 'r', encoding='utf8') as filein:
        content=filein.read()
        start=0
        while(start>=0):
            start=content.find("Custom String", start)
            if start<0 : break
            start=content.find("\"", start)
            end=content.find("\"", start+1)
            out.append(content[start+1:end].strip())
            start=end
    return out

def translate(filename, trans_dict):
    with open(filename, 'r', encoding='utf8') as filein:
        content=filein.read()
        start=0
        while(start>=0):
            start=content.find("Custom String", start)
            if start<0 : break
            start=content.find("\"", start)
            end=content.find("\"", start+1)
            t=content[start+1:end].strip()
            if t in trans_dict:
                content=content.replace(t, trans_dict[t], 1)
            start=content.find('\"', start+1)
            start+=1
        return content

def load_dict(dictname):
    with open(dictname, 'r', encoding='utf8') as dictin:
        out=json.loads(dictin.read())
        return out

def merge_text(new_text_filename, out_text_filename, prev_text_jsonname = None):
    out=dict()
    with open(new_text_filename, 'r', encoding='utf8') as newin:
        for l in newin:
            out[l.strip()]=''
        if prev_text_jsonname:
            d=load_dict(prev_text_jsonname)
            out.update(d)
        with open(out_text_filename, 'w', encoding='utf8') as newout:
            for i in out.items():
                newout.write(i[0]+'\n')
                newout.write(i[1]+'\n')
                newout.write('\n')
    return out

if __name__ == "__main__":

## pull out text 
#     maps=['script1.txt', 'script2.txt', 'script3.txt']
#     terms=[]
#     for i in maps:
#         terms += pull_text(i)
#     terms=list(set(terms))
#     with open("terms.txt", 'w', encoding='utf8') as out:
#         terms.sort(key=len)
#         for s in terms:
#             out.write(s+'\n')

## merge with previous work
#     merge_text('terms.txt', 'translate_me.txt', 'dict.json')

## generate dictionary for reuse in future.
#     tmp=dict_gen("translate_me.txt")
#     with open("dict.json", 'w', encoding='utf8') as fileout:
#       fileout.write(json.dumps(tmp))

## write translated work back to script.
#     maps=['adventure.txt', 'arreat.txt', 'conversion.txt', 'elite.txt', 'regular.txt', 'renew.txt', 'secret.txt', 'training.txt']
#     d=load_dict("dict.json")
#     for i in maps:
#       o=translate(i,d)
#       with open("./out/"+i, 'w', encoding='utf8') as out:
#         out.write(o)

    pass
