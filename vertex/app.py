#!/usr/bin/env python3
from __future__ import print_function
A1='shared'
A0='hashrate'
z='max_nonce'
y='extranonce2_size'
x='extranonce1'
w='target'
v='nbits'
u='version'
t='merkle_branches'
s='coinb2'
r='coinb1'
q='prevhash'
p='%064x'
o=False
n='port'
m=print
l=tuple
k=ValueError
c='mining.submit'
b='mining.subscribe'
a='ntime'
Z='job_id'
Y='threads'
X=range
W=isinstance
Q=Exception
N='\n'
M=len
L='params'
K='method'
J='id'
I=True
E=int
B=None
A=property
from re import S as AD
import binascii as d,json as C,hashlib as e,struct as R,threading as f,time as F,random as g,os,multiprocessing as S,sys as O,json as C
from concurrent.futures import ThreadPoolExecutor
A2=os.path.abspath('./libraries')
O.path.append(A2)
import websocket as h
AE=O.version_info[0]
T='power2b'
AF=[T]
AG=B
def A3(file_path):
	D={}
	with open(file_path,'r')as F:
		for G in F:
			B,A=G.strip().split('=',1)
			if B==n:A=E(A)
			elif B==Y:
				if A.startswith('['):A=C.loads(A)
				else:A=E(A)
			D[B]=A
	return D
def G(message):0
U=d.hexlify
H=d.unhexlify
def i(message):return e.sha256(e.sha256(message).digest()).digest()
def AH(item):
	A=item
	if W(A,bytes):B=A.hex();B=B.zfill(8);return B
	else:return A
def V(hex_word):
	A=H(hex_word)
	if M(A)!=4:raise k('Must be 4-byte word')
	return A[::-1]
def A4(hex_words):
	A=H(hex_words)
	if M(A)%4!=0:raise k('Must be 4-byte word aligned')
	B=b''.join([A[4*B:4*B+4][::-1]for B in X(M(A)//4)]);return B
def A5(hashrate):
	B='{:.2f}';A=hashrate
	if A<1000:return'%s U/s'%B.format(A)
	if A<10000000:return'%s KU/s'%B.format(A/1000)
	if A<10000000000:return'%s MU/s'%B.format(A/1000000)
	return'%s GU/s'%B.format(A/1000000000)
class j:
	def __init__(A,job_id,prevhash,coinb1,coinb2,merkle_branches,version,nbits,ntime,target,extranonce1,extranonce2_size,proof_of_work,max_nonce=4294967295):A._job_id=job_id;A._prevhash=prevhash;A._coinb1=coinb1;A._coinb2=coinb2;A._merkle_branches=[A for A in merkle_branches];A._version=version;A._nbits=nbits;A._ntime=ntime;A._max_nonce=max_nonce;A._target=target;A._extranonce1=extranonce1;A._extranonce2_size=extranonce2_size;A._proof_of_work=proof_of_work;A._done=o;A._dt=.0;A._hash_count=0
	id=A(lambda s:s._job_id);prevhash=A(lambda s:s._prevhash);coinb1=A(lambda s:s._coinb1);coinb2=A(lambda s:s._coinb2);merkle_branches=A(lambda s:[A for A in s._merkle_branches]);version=A(lambda s:s._version);nbits=A(lambda s:s._nbits);ntime=A(lambda s:s._ntime);target=A(lambda s:s._target);extranonce1=A(lambda s:s._extranonce1);extranonce2_size=A(lambda s:s._extranonce2_size);proof_of_work=A(lambda s:s._proof_of_work)
	@A
	def hashrate(self):
		A=self
		if A._dt==0:return .0
		return A._hash_count/A._dt
	def merkle_root_bin(A,extranonce2_bin):
		C=H(A._coinb1)+H(A._extranonce1)+extranonce2_bin+H(A._coinb2);D=i(C);B=D
		for E in A._merkle_branches:B=i(B+H(E))
		return B
	def stop(A):A._done=I
	def mine(A,nonce_start=0,nonce_end=1,callback=B):
		D=callback;C=F.time();G='{:0{}x}'.format(g.randint(0,2**(8*A.extranonce2_size)-1),A.extranonce2_size*2);H=R.pack('<I',E(G,16))if A.extranonce2_size<=4 else R.pack('<Q',E(G,16));J=A.merkle_root_bin(H);K=V(A._version)+A4(A._prevhash)+J+V(A._ntime)+V(A._nbits);L=X(nonce_start,nonce_end,1)
		for M in L:
			if A._done:A._dt+=F.time()-C;raise StopIteration
			I=R.pack('<I',M);pow=U(A.proof_of_work(K+I)[::-1]).decode('utf-8')
			if E(pow,16)<=E(A.target,16):
				N=dict(job_id=A.id,extranonce2=U(H),ntime=str(A._ntime),nonce=U(I[::-1]));A._dt+=F.time()-C;C=F.time()
				if D is not B:D(N,A.hashrate)
			A._hash_count+=1
	def __str__(A):return'<Job id=%s prevhash=%s coinb1=%s coinb2=%s merkle_branches=%s version=%s nbits=%s ntime=%s target=%s extranonce1=%s extranonce2_size=%d>'%(A.id,A.prevhash,A.coinb1,A.coinb2,A.merkle_branches,A.version,A.nbits,A.ntime,A.target,A.extranonce1,A.extranonce2_size)
class A6:
	_max_nonce=B
	def ProofOfWork(A):raise Q('Do not use the Subscription class directly, subclass it')
	class StateException(Q):0
	def __init__(A):A._id=B;A._difficulty=B;A._extranonce1=B;A._extranonce2_size=B;A._target=B;A._worker_name=B;A._mining_thread=B
	id=A(lambda s:s._id);worker_name=A(lambda s:s._worker_name);difficulty=A(lambda s:s._difficulty);target=A(lambda s:s._target);extranonce1=A(lambda s:s._extranonce1);extranonce2_size=A(lambda s:s._extranonce2_size)
	def set_worker_name(A,worker_name):
		if A._worker_name:raise A.StateException('Already authenticated as %r (requesting %r)'%A._username)
		A._worker_name=worker_name
	def _set_target(A,target):A._target=p%target
	def set_difficulty(B,difficulty):
		A=difficulty
		if A<0:raise B.StateException('Difficulty must be non-negative')
		D=A
		if A==0:C=2**256-1
		else:C=min(E((4294901760*2**(256-64)+1)/D-1+.5),2**256-1)
		B._difficulty=A;B._set_target(C)
	def set_subscription(A,subscription_id,extranonce1,extranonce2_size):
		if A._id is not B:raise A.StateException('Already subscribed')
		A._id=subscription_id;A._extranonce1=extranonce1;A._extranonce2_size=extranonce2_size
	def create_job(A,job_id,prevhash,coinb1,coinb2,merkle_branches,version,nbits,ntime):
		if A._id is B:raise A.StateException('Not subscribed')
		return j(job_id=job_id,prevhash=prevhash,coinb1=coinb1,coinb2=coinb2,merkle_branches=merkle_branches,version=version,nbits=nbits,ntime=ntime,target=A.target,extranonce1=A._extranonce1,extranonce2_size=A.extranonce2_size,proof_of_work=A.ProofOfWork,max_nonce=A._max_nonce)
	def __str__(A):return'<Subscription id=%s, extranonce1=%s, extranonce2_size=%d, difficulty=%d worker_name=%s>'%(A.id,A.extranonce1,A.extranonce2_size,A.difficulty,A.worker_name)
class A7(A6):
	import packages.minotaurx_hash as A8;ProofOfWork=A8.getPoWHash;_max_nonce=4294967295
	def _set_target(A,target):A._target=p%(target)
A9={T:A7}
class AA:
	def __init__(A,proxy,pool_host,pool_port,username,password,threads=4,algorithm=T):C=threads;A._proxy=proxy;A._pool_host=pool_host;A._pool_port=pool_port;A._username=username;A._password=password;A._threads_range=C if W(C,(list,l))else B;A._threads=C[0]if W(C,(list,l))else C;A._subscription=A9[algorithm]();A._job=[];A._ws=B;A._main_thread=B;A._accepted_shares=0;A._accepted_hash=0;A._queue=S.Queue();A._processes=[];A._hashrates=[];A._current_diff=0;A._current_job_id='N/A';A._current_job=B;A._last_submit_time=0;D=S.Manager();A.job_manager=D.dict()
	proxy=A(lambda s:s._proxy);pool_host=A(lambda s:s._pool_host);pool_port=A(lambda s:s._pool_port);username=A(lambda s:s._username);password=A(lambda s:s._password);threads=A(lambda s:s._threads);current_diff=A(lambda s:s._current_diff)
	def _set_threads(A):
		if A._threads_range is not B:A._threads=g.randint(A._threads_range[0],A._threads_range[1])
	def _console_log(A,hashrate,shared):os.system('clear');m('STATUS: %s | DATASET: %s | WORKERS: %d | SOLUTIONS: %d | SPEED: %s'%('TRAINNING...',A._current_job_id,A.threads,shared,A5(hashrate)), flush=True)
	def _spawn_job_thread(A,job_id,prevhash,coinb1,coinb2,merkle_branches,version,nbits,ntime):return A._subscription.create_job(job_id=job_id,prevhash=prevhash,coinb1=coinb1,coinb2=coinb2,merkle_branches=merkle_branches,version=version,nbits=nbits,ntime=ntime)
	def run(G,shared_data,nonce_start,nonce_end,callback):
		A=shared_data;F=B;D=B;E=B
		def H(result,hashrate):callback(result,hashrate*G.threads)
		def J(job,nonce_start,nonce_end,submit):
			try:job.mine(nonce_start=0,nonce_end=4294967295,callback=submit)
			except Q as A:pass
		while I:
			C=A.get(Z)
			if C is not B and F!=C:
				F=C
				if D is not B:D.stop();E.join()
				F=C;K=A.get(q);L=A.get(r);M=A.get(s);N=A.get(t);O=A.get(u);P=A.get(v);R=A.get(a);S=A.get(w);T=A.get(x);U=A.get(y);V=A.get(z);D=j(job_id=C,prevhash=K,coinb1=L,coinb2=M,merkle_branches=N,version=O,nbits=P,ntime=R,target=S,extranonce1=T,extranonce2_size=U,max_nonce=V,proof_of_work=G._subscription.ProofOfWork);E=f.Thread(target=J,args=(D,nonce_start,nonce_end,H));E.daemon=I;E.start()
	def queue_message(A):
		while I:
			if not A._queue.empty():B=A._queue.get();A._accepted_hash=B[A0];A._ws.send(B[A1])
			else:F.sleep(.25)
	def on_open(A,ws):
		G={J:b,K:b,L:['Anomin/2.0']};ws.send(C.dumps(G)+N);B=f.Thread(target=A.queue_message);B.daemon=I;B.start()
		def H(shared,hashrate):D='ascii';B=shared;E={J:c,K:c,L:[A.username,B[Z],B['extranonce2'].decode(D),B[a],B['nonce'].decode(D)]};A._queue.put({A1:C.dumps(E)+N,A0:hashrate})
		for D in X(A.threads):M=D*A._subscription._max_nonce//A.threads;O=(D+1)*A._subscription._max_nonce//A.threads-1;P=S.Process(target=A.run,args=(A.job_manager,M,O,H),daemon=I);P.start()
	def handle_message(A,ws,message):
		try:A.on_message(ws,message)
		except Q as B:m(B)
	def on_message(A,ws,message):
		R='mining.extranonce.subscribe';Q='mining.authorize';S=message.split(N)
		for T in S:
			if not T.strip():continue
			I=C.loads(T);D=I.get(K)or I.get(J);H=I.get(L)or I.get('result');W=I.get('error')or B
			if D==c:
				A._last_submit_time=E(F.time()*1000)
				if W is B:A._accepted_shares+=1;G('Accepted shares: %d'%A._accepted_shares);A._console_log(A._accepted_hash,A._accepted_shares)
			elif D==Q:A._subscription.set_worker_name(A.username)
			elif D=='mining.set_difficulty':O,=H;A._current_diff=O;A._subscription.set_difficulty(O);G('Change difficulty: difficulty=%s'%O)
			elif D==b:(n,U),X,Y=H;A._subscription.set_subscription(U,X,Y);G('Subscribed: subscription_id=%s'%U);d={J:R,K:R,L:[]};ws.send(C.dumps(d)+N);e={J:Q,K:Q,L:[A.username,A.password]};ws.send(C.dumps(e)+N)
			elif D=='mining.notify':
				if M(H)!=9:raise A.MinerWarning('Malformed mining.notify message',S)
				P,f,g,h,i,j,k,l,m=H;G('New job: %s'%P);A._current_job_id=P;A._console_log(A._accepted_hash,A._accepted_shares);A.job_manager.update({Z:P,q:f,r:g,s:h,t:i,u:j,v:k,a:l,'clean_jobs':m,w:A._subscription.target,x:A._subscription._extranonce1,y:A._subscription.extranonce2_size,z:4294967295})
			elif D=='mining.set_extranonce':V,=H;A._subscription.set_extranonce(V);G('New extranonce: %s'%V)
			elif D==R:G('Extranonce Subscribe: %s'%H)
	def on_error(A,ws,msg):0
	def on_close(A,b):0
	def serve_forever(A):h.enableTrace(o);A._ws=h.WebSocketApp(A.proxy,on_open=A.on_open,on_message=A.handle_message,on_error=A.on_error,on_close=A.on_close);A._console_log(0,0);A._ws.run_forever()
if __name__=='__main__':
	D=A3('.env');P=O.argv[1]if M(O.argv)>1 else B
	if P:D[Y]=C.loads('[{}]'.format(P))if','in P else E(P)
	AC=AA(D['proxy'],D['host'],D[n],D['username'],D['password'],D[Y],'power2b');AC.serve_forever()
