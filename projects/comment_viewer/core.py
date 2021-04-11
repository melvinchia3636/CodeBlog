Z,F,L,G,D,E,H='nextContinuationData',isinstance,'continuation',',','XSRF_TOKEN',len,list
import requests as M,json as N
from ftfy import fix_text as Y
try:from .sss import ShortScale as I
except:from sss import ShortScale as I
def B(partial,key):
	C=key;A=partial
	if F(A,dict):
		for (G,E) in A.items():
			if G==C:yield E
			else:
				for D in B(E,C):yield D
	elif F(A,H):
		for I in A:
			for D in B(I,C):yield D

def A(url):
	I='var ytInitialData = ';
	O=M.Session();
	A=O.get(url).text;
	C=A.find(I);
	F=A.find('};',C);
	print(A[C+E(I):F].strip()+'}')
	P=N.loads(A[C+E(I):F].strip()+'}');
	J=H([A for A in B(P,'itemSectionRenderer')][-1].values())[0][0][Z];
	Q=[(J[L],J['clickTrackingParams'])];
	return Q.pop()

def C(url,continuation_tokens,itct):
	O='replyCount';P='authorText';Q='runs';R='publishedTimeText';S='likeCount';T='authorThumbnail';U='INNERTUBE_CONTEXT_CLIENT_VERSION';J='text';F=continuation_tokens;V=M.Session();A=V.get(url).text;C=A.find(D);K=A.find(G,C);a=A[C+E(D)+3:K-1];C=A.find(U);K=A.find(G,C);b=A[C+E(U)+3:K-1];c={'x-youtube-client-name':'1','x-youtube-client-version':b,'accept-language':'en;q=0.9'};d={'session_token':a[:-12]+'=='};W=F;e={'action_get_comments':1,'pbj':1,'ctoken':W,L:W,'itct':itct};f=V.post('https://www.youtube.com/comment_service_ajax',params=e,data=d,headers=c);X=N.loads(f.text);g=H(B(X,'commentRenderer'))
	try:F=[tuple(A[Z].values())for A in next(B(X,'itemSectionContinuation'))['continuations']]
	except:F=[()]
	return[[{'id':A['commentId'],J:Y(''.join((B[J]for B in A['contentText'][Q]))),'author':A[P]['simpleText']if A[P]else None,T:A[T]['thumbnails'][-1]['url'].split('=')[0]+'=s64',S:I(int(A[S])),'commentsCount':I(A[O])if O in A else 0,R:A[R][Q][0][J]}for A in g]]+[F.pop()]