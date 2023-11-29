# node -> (character, frequency, left, right)
import queue,operator;b=lambda m:(f:={i:m.count(i)for i in set(m)},f:={k:v for(k,v)in sorted(f.items(),key=lambda x:x[1],reverse=True)},f:=list(f.items()),s:=queue.Queue(),[s.put([None,sum(map(lambda x:x[1],f[i:])),None,[f[i][0],f[i][1],None,None]])for i in range(len(f))],t:=s.get(),c:=t,[(operator.setitem(c,2,s.get()),c:=c[2])for _ in range(s.qsize())],t)[8]
print(b("Hello World"))
