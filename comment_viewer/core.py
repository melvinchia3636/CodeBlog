S, H, M, L, G, F, E='nextContinuationData', isinstance, 'continuation', ',', 'XSRF_TOKEN', len, list
import requests as J,json as K; from ftfy import fix_text as R
try:from .sss import ShortScale as D
except:from sss import ShortScale as D
def B(partial,key):
    C=key;A=partial
    if H(A,dict):
        for (G,F) in A.items():
            if G==C:yield F
            else:
                for D in B(F,C): yield D
    elif H(A,E):
        for I in A:
            for D in B(I,C):yield D
def A(url):P='var ytInitialData = ';I=J.Session();A=I.get(url).text;C=A.find(G);D=A.find(L,C);Q=A[C+F(G)+3:D-1];C=A.find(P);D=A.find('};',C);N=K.loads(A[C+F(P):D].strip()+'}');H=E(E(B(N,'itemSectionRenderer'))[0].values())[0][0][S];O=[(H[M],H['clickTrackingParams'])];return O.pop()[0]
def C(url,continuation_tokens):g='replyCount';f='authorText';e='runs';d='publishedTimeText';c='likeCount';b='authorThumbnail';a='INNERTUBE_CONTEXT_CLIENT_VERSION';Q='text';H=continuation_tokens;N=J.Session();A=N.get(url).text;C=A.find(G);I=A.find(L,C);T=A[C+F(G)+3:I-1];C=A.find(a);I=A.find(L,C);U=A[C+F(a)+3:I-1];V={'x-youtube-client-name':'1','x-youtube-client-version':U,'accept-language':'en;q=0.9'};W={'session_token':T[:-12]+'=='};O=H;X={'action_get_comments':1,'pbj':1,'ctoken':O,M:O};Y=N.post('https://www.youtube.com/comment_service_ajax',params=X,data=W,headers=V);P=K.loads(Y.text);Z=E(B(P,'commentRenderer'));H=[A[M]for A in B(P,S)];return[[{'id':A['commentId'],Q:R(''.join((B[Q]for B in A['contentText'][e]))),'author':A[f]['simpleText']if A[f]else None,b:A[b]['thumbnails'][-1]['url'].split('=')[0]+'=s64',c:D(int(A[c])),'commentsCount':D(A[g])if g in A else 0,d:A[d][e][0][Q]}for A in Z]]+[H]