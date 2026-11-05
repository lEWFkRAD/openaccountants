import subprocess
for f in ['skills/us-states/ny/ny-estimated-tax.md','skills/us-states/ny/ny-income-tax.md']:
    orig=subprocess.run(['git','show','4d26c15a2:'+f],capture_output=True,text=True).stdout.split('\n')
    cur=open(f).read().split('\n')
    o=orig[2].replace('IT-2105.9','IT-2105 line 9'); c=cur[2]
    p=0
    while p<min(len(o),len(c)) and o[p]==c[p]: p+=1
    tail=o[p:]
    if tail:
        for i,l in enumerate(cur):
            if i!=2 and tail[:30] in l:
                cur.remove(l)
                cur[2]=c+l
                break
    open(f,'w').write('\n'.join(cur))
    print('repaired',f,'desc len',len(cur[2]))
