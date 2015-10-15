

def polin_alg1(s):
    ls = len(s);
    rev = ['' for rev in range(ls)]
    print ("%s" %(rev))
    revI = ls-1
    for i in range(ls):
        print i
        rev[revI]=s[i]
        revI=revI-1   
    print ("%s, %s" %(''.join(rev),s))       
    if revI==s:
        print True    
    return;

def polin_alg_11(s):
    rev = ''
    for i in range(len(s)-1,-1,-1):
        print i
        rev+=s[i]
    print ("%s, %s" %(s, rev))
    return;

def polin_alg2(s):
    l = len(s)/2
    half = s[:l]
    past = s[l+1:]
    rev = ''
    for i in range(l-1,-1,-1):
        rev+=half[i]
    
    print ("%s, %s" %(rev, past))
  
 
def polin_alg3(s):
    size = len(s)-1
    print size
    for i in range(size):
        first=s[i]
        last = s[size-i]
        print ("%s, %s" %(first, last))
    

'polin_alg_11("bay")
'polin_alg2("porop")
polin_alg3("paap")
