D7='Referer'
D6='liveapi2'
D5='playUrl'
D4='mimeType'
D3='codecid'
D2='192000'
D1='media_ft'
D0='media_bangumi'
C_='stream'
Cz='playurl_info'
Cy='\u3000UID：'
Cx='是否关注$ '
Cw='vod_list'
Cv='\u3000👥 '
Cu='➖取关$2_notplay_follow'
Ct='➕关注$1_notplay_follow'
Cs='bilidanmu'
Cr='setting'
Cq='Reply_jump'
Cp='https://b23.tv/'
Co='message'
Cn='totalrank'
Cm='room_id'
Cl='featured'
Ck='favorite'
Cj='attention'
Ci='\u3000💬'
Ch='videos'
Cg='  个人主页'
Cf='quicksearch'
Ce='oldest'
Cd='user_cover'
Cc='roomid'
Cb='text_small'
Ca='watched_show'
CZ='live_status'
CY='offset'
CX='查看直播细化标签'
CW='fav_list'
CV='https://api.bilibili.com/x/web-interface/nav'
CU='bangumi_pay_parse'
CT='bangumi_vip_parse'
CS='bangumi_horizontal_cover'
CR='hide_bangumi_vip_badge'
CQ='hide_bangumi_preview'
CP='raw_cookie_vip'
CO='raw_cookie_line'
CL='header'
CK='vodTMPQn'
CJ='wts'
CI='csrf'
CH='dur'
CG='playurl'
CF='ver'
CE='checkUpdate'
CD='interaction'
CC='vod_director'
CB='vod_area'
CA='vod_year'
C9='title_type'
C8='000'
C7='bili_user'
C6='sort'
C5='season_status'
C4='special'
C3='悄悄关注'
C2='最近关注'
C1='bangumi'
C0='coin'
B_='like_num'
Bz='part'
By='  💬'
Bx='play'
Bw='vod_pc'
Bv='module_author'
Bu='https://www.bilibili.com'
Bt='isVIP'
Bs='isLogin'
Br='https://'
Bq='每周必看'
Bp='排行榜'
Bo='showLiveFilterTag'
Bn='vodDefaultCodec'
Bm='favMode'
Bl='maxHomeVideoContent'
Bk='currentVersion'
Bj=round
Bf='audio'
Be='format'
Bd='codec'
Bc='status'
Bb='vod_actor'
Ba='redirect_url'
BZ='edgeid'
BY='$ '
BX='BV'
BW='all'
BV='最近访问'
BU='最常访问'
BT='稍后再看'
BS='vod_count'
BR='episodes'
BQ='stat'
BP='  ▶'
BO='content'
BN='archive'
BM='UP主'
BL='modules'
BK='items'
BJ='分区'
BI='type_name'
BH='搜索'
BG='历史'
BF='关注'
BE='rankingLis'
BD='tuijianLis'
BC='heartbeatInterval'
BB=float
BA=open
B9='contentType'
B8='s_title'
B7='graph_version'
B6='fromep'
B5='ssid'
B4='seasons'
B3='特别关注'
B2='正在直播'
B1='like'
B0='new_ep'
A_='index_show'
Az='view'
Ay='pic'
Ax='keyword'
Aw='channel_list'
Av='userid'
Au='utf-8'
At='cateManual'
As='show_vod_hot_reply'
Ar='vodDefaultAudio'
Aq='vodDefaultQn'
Ap='@@@'
Ao='season_title'
An='parse'
Am='Reply'
Al='danmaku'
Ak='fans'
Aj='following'
Ai='pubdate'
Ah='  🆙'
Ag='mlid'
Af='收藏'
Ae='频道'
Ad='影视'
Ac='vod_content'
Ab='\u3000'
Aa='desc'
AZ='up'
AY='season_id'
AX='owner'
AW='live'
AV='4'
AU=None
AT='cateLive'
AS='vip'
AR='3'
AP='newVersion'
AO='vod_play_url'
AN='vod_play_from'
AM='result'
AL=' '
AK='"'
AJ='&quot;'
AI='动态'
AH='直播'
AG='推荐'
AF=True
AE='_tmp'
AD='﹩'
AC='﹟'
AB='video'
AA='/'
A9='User-Agent'
A8='uname'
A7='face'
A6='UP'
A5='cateManualLiveExtra'
A4='cookies_dic'
A3=dict
A2='tid'
A1='2'
A0='ep'
z='cateManualLive'
y='热门'
w='$'
v='av'
u='limit'
t='pagecount'
s=list
r='type'
q='ss'
p='total'
o='url'
n='cid'
m='id'
l='</em>'
k='<em class="keyword">'
i='cover'
h='page'
g='master'
f=map
e='$$$'
d='duration'
c='users'
b='order'
a='aid'
Z='filter'
Y='page_size'
X='vod_remarks'
W='mid'
V=len
U='vod_pic'
T='1'
S='key'
R='title'
Q='vod_id'
P='fake'
O='vod_name'
N='#'
M='code'
L='0'
G='value'
K='_'
J='name'
H='list'
F=int
E='data'
D='n'
C='v'
B=''
A=str
import sys,os,json as I
from base.spider import Spider
from requests import session as Bg,utils as Bh,get as CM
from requests.adapters import HTTPAdapter as D8,Retry
from concurrent.futures import ThreadPoolExecutor as D9,as_completed as Bi
import threading as j,hashlib,time as x,random
from functools import reduce
from urllib.parse import quote,urlencode as CN
sys.path.append('..')
AQ,DA=os.path.split(os.path.abspath(__file__))
sys.path.append(AQ)
class Spider(Spider):
	defaultConfig={Bk:'20231004_1',CO:B,CP:B,Bl:AR,Bm:L,Y:10,BC:'15',Aq:'80',Bn:'7',Ar:'30280',As:AF,CQ:AF,CR:AF,CS:AF,CT:AF,CU:AF,Bo:L,At:[AG,Ad,AH,AI,Ae,Af,BF,BG,BH],BD:[AG,y,Bp,Bq,'入站必刷','番剧时间表','国创时间表'],BE:['动画','音乐','舞蹈','游戏','鬼畜','知识','科技','运动','生活','美食','动物','汽车','时尚','娱乐',Ad,'原创','新人']}
	focus_on_up_list=[{"n":"LexBurner", "v":"777536"},{"n":"真栗", "v":"210752"},{"n":"黑色脑回路", "v":"121895315"},{"n":"JOKER鹏少", "v":"92678046"}]
	focus_on_search_key=['经典无损音乐合集','帕梅拉','太极拳','健身','舞蹈','音乐','歌曲','MV4K','演唱会4K','白噪音4K','知名UP主','说案','解说','演讲','探索发现超清','纪录片超清','平面设计教学','软件教程','实用教程','旅游','风景4K','食谱','美食超清','搞笑','球星','动物世界超清','相声小品','戏曲','儿童','小姐姐4K','荒野求生超清']
	def getName(A):return'哔哩哔哩'
	def load_config(A):
		try:
			with BA(f"{AQ}/config.json",encoding=Au)as D:A.userConfig=I.load(D)
			E={g:'cookie_dic',AS:'cookie_vip_dic',P:'cookie_fake_dic'}
			for(F,C)in E.items():
				C=A.userConfig.get(C)
				if C:
					if not A.userConfig.get(c):A.userConfig[c]={}
					A.userConfig[c][F]={A4:C}
			B=A.userConfig.get(c,{})
			if B.get(g)and B[g].get(A4):A.session_master.cookies=Bh.cookiejar_from_dict(B[g][A4]);A.userid=B[g][Av]
			if B.get(P)and B[P].get(A4):A.session_fake.cookies=Bh.cookiejar_from_dict(B[P][A4])
		except:A.userConfig={}
		A.userConfig={**A.defaultConfig,**A.userConfig}
	dump_config_lock=j.Lock()
	def dump_config(A):
		F=[c,Aw,AT,z,A5];C={}
		for(B,D)in A.userConfig.items():
			E=A.defaultConfig.get(B)
			if E!=AU and D!=E or B in F:C[B]=D
		A.dump_config_lock.acquire()
		with BA(f"{AQ}/config.json",'w',encoding=Au)as G:H=I.dumps(C,indent=1,ensure_ascii=False);G.write(H)
		A.dump_config_lock.release()
	pool=D9(max_workers=8);task_pool=[]
	def homeContent(A,filter):
		A.pool.submit(A.add_live_filter);A.pool.submit(A.add_channel_filter);A.pool.submit(A.add_search_key);A.pool.submit(A.add_focus_on_up_filter);A.pool.submit(A.get_tuijian_filter);A.pool.submit(A.add_fav_filter);F=[Ae,AI,Af,BF,BG];B=A.userConfig[At]
		if not A.userid and not A6 in B or not AI in B and not A6 in B:B+=[A6]
		D=[]
		for C in B:
			if C in F and not A.userid:continue
			D.append({BI:C,'type_id':C})
		A.add_focus_on_up_filter_event.wait()
		if A6 in B:A.config[Z].update({A6:A.config[Z].pop(AI)})
		E={'class':D};A.add_live_filter_event.wait();A.add_channel_filter_event.wait();A.add_fav_filter_event.wait();A.add_search_key_event.wait()
		if filter:E['filters']=A.config[Z]
		A.pool.submit(A.dump_config);A.pool.submit(A._checkUpdate,L);return E
	userid=csrf=B;session_master=Bg();session_vip=Bg();session_fake=Bg();con=j.Condition();getCookie_event=j.Event();retries=Retry(total=5,backoff_factor=.1);adapter=D8(max_retries=retries);session_master.mount(Br,adapter);session_vip.mount(Br,adapter);session_fake.mount(Br,adapter)
	def getCookie_dosth(B,co):
		A=co.strip().split('=',1)
		if not'%'in A[1]:A[1]=quote(A[1])
		return A
	def getCookie(A,_type=g):
		D=_type;G=CO
		if D==AS:G=CP
		G=A.userConfig.get(G);K=A.userConfig.get(c,{});C=K.get(D,{})
		if not G and not C:
			if D==g:A.getCookie_event.set()
			with A.con:A.con.notifyAll()
			return
		J=C.get(A4,{})
		if G:J=A3(f(A.getCookie_dosth,G.split(';')))
		L=Bh.cookiejar_from_dict(J);N=CV;O=A.fetch(N,headers=A.header,cookies=L);H=I.loads(O.text);C[Bs]=0
		if H[M]==0:
			C[Bs]=1;C[Av]=H[E][W];C[A7]=H[E][A7];C[A8]=H[E][A8];C[A4]=J;C[Bt]=F(H[E]['vipStatus'])
			if D==g:A.session_master.cookies=L;A.userid=C[Av];A.csrf=J['bili_jct']
			if C[Bt]:A.session_vip.cookies=L
		else:A.userid=B
		K[D]=C
		with A.con:
			if V(C)>1:A.userConfig.update({c:K})
			if D==g:A.getCookie_event.set()
	getFakeCookie_event=j.Event()
	def getFakeCookie(A,fromSearch=AU):
		if A.session_fake.cookies:A.getFakeCookie_event.set()
		C={};C[A9]=A.header[A9];B=A.fetch(Bu,headers=C);A.session_fake.cookies=B.cookies;A.getFakeCookie_event.set()
		with A.con:D=A.userConfig.get(c,{});D[P]={A4:A3(B.cookies)};A.userConfig.update({c:D})
		if not fromSearch:
			A.getCookie_event.wait()
			if not A.session_master.cookies:A.session_master.cookies=B.cookies
	def get_fav_list_dict(E,fav):A={D:fav[R].replace(k,B).replace(l,B).replace(AJ,AK).strip(),C:fav[m]};return A
	add_fav_filter_event=j.Event()
	def add_fav_filter(B):
		N=B.userConfig.get(c,{})
		if N.get(g)and N[g].get(Av):F=B.userConfig[c][g][Av]
		else:B.getCookie_event.wait();F=B.userid
		K=[]
		if F:
			P='https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=%s&jsonp=jsonp'%A(F);Q=B._get_sth(P);L=I.loads(Q.text)
			if L[M]==0 and L.get(E):R=L[E].get(H);K=s(f(B.get_fav_list_dict,R))
		U=[{D:'追番',C:T},{D:'追剧',C:A1}];O=B.config[Z].get(Af)
		if O:O.insert(0,{S:Ag,J:BJ,G:U+K})
		B.add_fav_filter_event.set();B.userConfig[CW]=K
	def get_channel_list_dict(F,channel):A=channel;E={D:A[J].replace(k,B).replace(l,B).replace(AJ,AK).strip(),C:A[m]};return E
	def get_channel_list(A):
		C='https://api.bilibili.com/x/web-interface/web/channel/category/channel/list?id=100&offset=0&page_size=15';D=A._get_sth(C,P);B=I.loads(D.text);G=[]
		if B[M]==0:F=B[E].get('channels');A.userConfig[Aw]=s(f(A.get_channel_list_dict,F))
		return A.userConfig[Aw]
	add_channel_filter_event=j.Event()
	def add_channel_filter(A):
		C=A.userConfig.get(Aw,B);E=A.pool.submit(A.get_channel_list)
		if not C:C=E.result()
		D=A.config[Z].get(Ae,[])
		if D:D.insert(0,{S:n,J:BJ,G:C})
		A.config[Z][Ae]=D;A.add_channel_filter_event.set()
	add_focus_on_up_filter_event=j.Event()
	def add_focus_on_up_filter(B):
		P='上个视频的UP主';N=[{D:P,C:P}];F=[]
		if not B.session_master.cookies:B.getCookie_event.wait()
		if B.session_master.cookies:
			Q='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&page=1';R=B._get_sth(Q);H=I.loads(R.text)
			if H[M]==0 and H.get(E):T=H[E].get(BK,[]);F=s(f(lambda x:{D:x[BL][Bv][J],C:A(x[BL][Bv][W])},T));N.insert(0,{D:'我的动态',C:L})
		if V(B.focus_on_up_list)>0:
			U=s(f(lambda x:x[C],B.focus_on_up_list))
			for O in F:
				if O[C]in U:F.remove(O)
			F.extend(B.focus_on_up_list)
		X=[{D:'登录与设置',C:'登录'}];F=N+F+X;K=B.config[Z].get(AI,[])
		if K:K.insert(0,{S:W,J:BM,G:F})
		B.config[Z][AI]=K;B.add_focus_on_up_filter_event.set()
	def get_live_parent_area_list(N,parent_area):B=parent_area;E=B[J];id=A(B[m]);F=B[H];I=s(f(lambda area:{D:area[J],C:A(area['parent_id'])+K+A(area[m])},F));L={S:A2,J:E,G:I};M={m:id+'_0',G:L};return E,M
	def get_live_list(A):
		C='https://api.live.bilibili.com/xlive/web-interface/v1/index/getWebAreaList?source_id=2';D=A._get_sth(C,P);B=I.loads(D.text);G={}
		if B[M]==0:F=B[E][E];A.userConfig[AT]=A3(A.pool.map(A.get_live_parent_area_list,F))
		return A.userConfig[AT]
	def set_default_cateManualLive(A):
		B=[{D:AG,C:AG},{D:y,C:y}]
		for E in A.userConfig[AT]:F={D:E,C:A.userConfig[AT][E][m]};B.append(F)
		A.defaultConfig[z]=B;return B
	add_live_filter_event=j.Event()
	def add_live_filter(A):
		C=A.userConfig.get(AT,{});E=A.pool.submit(A.get_live_list)
		if not C:C=E.result()
		H=A.pool.submit(A.set_default_cateManualLive);A.config[Z][AH]=[];B=A.userConfig.get(z,[])
		if not B:B=H.result()
		if B:I={S:A2,J:BJ,G:B};A.config[Z][AH].append(I)
		if F(A.userConfig[Bo]):
			for D in C.values():
				if V(D[G][G])==1:continue
				A.config[Z][AH].append(D[G])
		A.add_live_filter_event.set()
	add_search_key_event=j.Event()
	def add_search_key(A):
		B=A.focus_on_search_key;L='https://api.bilibili.com/x/web-interface/search/square?limit=10&platform=web';N=A._get_sth(L,P);F=I.loads(N.text);Q={}
		if F[M]==0:O=F[E]['trending'].get(H,[]);B+=s(f(lambda x:x[Ax],O))
		K={S:Ax,J:'搜索词',G:[]};K[G]=s(f(lambda i:{D:i,C:i},B));A.config[Z][BH].insert(0,K);A.add_search_key_event.set()
	def get_tuijian_filter(E):
		K={'番剧时间表':'10001','国创时间表':'10004',Bp:L,'动画':T,'音乐':AR,'舞蹈':'129','游戏':AV,'鬼畜':'119','知识':'36','科技':'188','运动':'234','生活':'160','美食':'211','动物':'217','汽车':'223','时尚':'155','娱乐':'5',Ad:'181','原创':'origin','新人':'rookie'};M=[{D:BD,C:BJ},{D:BE,C:Bp}];F=[]
		for H in M:
			I={S:A2,J:H[C],G:[]};N=E.userConfig.get(H[D],[])
			for A in N:
				B=K.get(A)
				if not B:B=A
				O={D:A,C:B};I[G].append(O)
			F.append(I)
		E.config[Z][AG]=F
	def __init__(A):A.load_config();A.pool.submit(A.getCookie);A.pool.submit(A.getFakeCookie);A.pool.submit(A.getCookie,AS)
	def init(A,extend=B):print('============{0}============'.format(extend))
	def isVideoFormat(A,url):0
	def manualVideoCheck(A):0
	def format_img(B,img):
		A=img;A+='@672w_378h_1c.webp'
		if not A.startswith('http'):A='https:'+A
		return A
	def pagination(A,array,pg):B=A.userConfig[Y]*F(pg);C=B-A.userConfig[Y];return array[C:B]
	def zh(D,num):
		C=num
		if F(C)>=100000000:B=Bj(BB(C)/BB(100000000),1);B=A(B)+'亿'
		elif F(C)>=10000:B=Bj(BB(C)/BB(10000),1);B=A(B)+'万'
		else:B=A(C)
		return B
	def second_to_time(D,a):
		a=F(a)
		if a<3600:C=x.strftime('%M:%S',x.gmtime(a))
		else:C=x.strftime('%H:%M:%S',x.gmtime(a))
		if A(C).startswith(L):C=A(C).replace(L,B,1)
		return C
	def str2sec(E,x):
		x=A(x)
		try:D,B,C=x.strip().split(':');return F(D)*3600+F(B)*60+F(C)
		except:B,C=x.strip().split(':');return F(B)*60+F(C)
	def filter_duration(B,vodlist,key):
		D=vodlist;C=key
		if C==L:return D
		else:E=[D for D in D if B.time_diff1[C][0]<=B.str2sec(A(D[X]))<B.time_diff1[C][1]];return E
	def find_bangumi_id(C,url):
		B=A(url).strip().split(AA)[-1]
		if not B:B=A(url).strip().split(AA)[-2]
		B=B.split('?')[0];return B
	def get_Login_qrcode(D,pg):
		R='setting_login_';N='https://www.bilibili.com/favicon.ico';A={}
		if F(pg)!=1:return A
		G=[{Q:'setting_tab&filter',O:'标签与筛选',U:N},{Q:'setting_liveExtra',O:CX,U:N}];K='https://passport.bilibili.com/x/passport-login/web/qrcode/generate';S=D._get_sth(K,P);J=I.loads(S.text)
		if J[M]==0:
			id=J[E]['qrcode_key'];K=J[E][o];T={g:'主账号',AS:'副账号'};V={0:'未登录',1:'已登录'};W={0:B,1:'👑'};Y=D.userConfig.get(c,{})
			for(Z,a)in T.items():
				C=Y.get(Z)
				if C:G.append({Q:R+id,O:C[A8],U:D.format_img(C[A7]),X:W[C[Bt]]+a+AL+V[C[Bs]]})
			L={'qrcode':'https://passport.bilibili.com/h5-app/passport/login/scan?qrcode_key='+id+'&navhide=1'};L['qr_chs']='208x117';G.append({Q:R+id,U:'http://jm92swf.s1002.xrea.com/?'+CN(L)})
		A[H]=G;A[h]=1;A[t]=1;A[u]=1;A[p]=1;return A
	time_diff1={T:[0,300],A1:[300,900],AR:[900,1800],AV:[1800,3600],'5':[3600,0x4ee2d6d415b85acef80ffffffff]};time_diff=L;dynamic_offset=B
	def get_dynamic(C,pg,mid,order):
		if mid==L:
			D={}
			if F(pg)==1:C.dynamic_offset=B
			S='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&offset=%s&page=%s'%(C.dynamic_offset,pg);T=C._get_sth(S);K=I.loads(T.text)
			if K[M]==0:
				C.dynamic_offset=K[E].get(CY);P=[];V=K[E][BK]
				for N in V:
					if not N['visible']:continue
					W=N[BL][Bv][J];G=N[BL]['module_dynamic']['major'][BN];Y=A(G[a]).strip();Z=G[R].strip().replace(k,B).replace(l,B);b=G[i].strip();c=A(C.second_to_time(C.str2sec(G['duration_text']))).strip()+Ah+A(W).strip();P.append({Q:v+Y,O:Z,U:C.format_img(b),X:c})
				D[H]=P;D[h]=pg;D[t]=9999;D[u]=99;D[p]=999999
			return D
		else:return C.get_up_videos(mid=mid,pg=pg,order=order)
	def get_found_vod(D,vod):
		C=vod;E=C.get(a,B)
		if not E:E=C.get(m,B)
		F=C.get('goto',B)
		if not F or F and F==v:E=v+A(E).strip()
		elif F=='ad':return[]
		M=C[R].strip();N=C[Ay].strip();P=C.get('is_followed')
		if F==AW:
			K=C['room_info'];H=B;S=K.get(CZ,B)
			if S:H='直播中  '
			else:return[]
			H+='👁'+K[Ca][Cb]+Ah+C[AX][J].strip()
		else:
			I=C.get('rcmd_reason',B)
			if I and type(I)==A3 and I.get(BO):
				G='  🔥'+I[BO].strip()
				if'人气飙升'in G:G='  🔥人气飙升'
			elif P:G='  已关注'
			else:G=Ah+C[AX][J].strip()
			H=A(D.second_to_time(C[d])).strip()+BP+D.zh(C[BQ][Az])+G
		L=[{Q:E,O:M,U:D.format_img(N),X:H}]
		for T in D.pool.map(D.get_found_vod,C.get('others',[])):L.extend(T)
		return L
	_popSeriesInit=0
	def get_found(B,tid,rid,pg):
		J=pg;G=tid;K={}
		if G==AG:T=B.encrypt_wbi(fresh_type=4,feed_version='V3',brush=1,fresh_idx=J,fresh_idx_1h=J,ps=B.userConfig[Y]);C=f"https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?{T}"
		else:
			C='https://api.bilibili.com/x/web-interface/ranking/v2?rid={0}&type={1}'.format(rid,G)
			if G==y:C='https://api.bilibili.com/x/web-interface/popular?pn={0}&ps={1}'.format(J,B.userConfig[Y])
			elif G=='入站必刷':C='https://api.bilibili.com/x/web-interface/popular/precious'
			elif G==Bq:
				if not B._popSeriesInit or F(J)==1:C='https://api.bilibili.com/x/web-interface/popular/series/list';Q=B._get_sth(C,P);L=I.loads(Q.text);N=B._popSeriesInit=L[E][H][0]['number'];B._popSeriesNum=[F(N),1]
				else:N=B._popSeriesNum[0]
				C='https://api.bilibili.com/x/web-interface/popular/series/one?number='+A(N)
		Q=B._get_sth(C);L=I.loads(Q.text)
		if L[M]==0:
			S=[];D=L[E].get('item')
			if not D:D=L[E][H]
			if V(D)>B.userConfig[Y]:
				if G==Bq:
					O=F(B._popSeriesNum[1]);R=V(D)/B.userConfig[Y]-O
					if R>0:R+=1
					if not F(R):B._popSeriesNum=[F(N)-1,1]
					else:B._popSeriesNum[1]=O+1
				else:O=J
				D=B.pagination(D,O)
			for U in B.pool.map(B.get_found_vod,D):S.extend(U)
			K[H]=S;K[h]=J;K[t]=9999;K[u]=99;K[p]=999999
		return K
	def get_bangumi(D,tid,pg,order,season_status):
		a='first_ep';Z='first_ep_info';W=order;G=tid;J={}
		if W=='追番剧':K='https://api.bilibili.com/x/space/bangumi/follow/list?type={0}&vmid={1}&pn={2}&ps={3}'.format(G,D.userid,pg,D.userConfig[Y]);b=D._get_sth(K)
		else:
			K='https://api.bilibili.com/pgc/season/index/result?type=1&season_type={0}&page={1}&order={2}&season_status={3}&pagesize={4}'.format(G,pg,W,season_status,D.userConfig[Y])
			if W==y:
				if G==T:K='https://api.bilibili.com/pgc/web/rank/list?season_type={0}&day=3'.format(G)
				else:K='https://api.bilibili.com/pgc/season/rank/web/list?season_type={0}&day=3'.format(G)
			b=D._get_sth(K,P)
		S=I.loads(b.text)
		if S[M]==0:
			if E in S:L=S[E][H]
			else:L=S[AM][H]
			if V(L)>D.userConfig[Y]:L=D.pagination(L,pg)
			c=[]
			for C in L:
				e=A(C[AY]).strip();f=C[R];N=C.get('ss_horizontal_cover')
				if not N or G==T and not D.userConfig[CS]:
					if C.get(Z)and i in C[Z]:N=C[Z][i]
					elif C.get(a)and i in C[a]:N=C[a][i]
					else:N=C[i].strip()
				F=C.get(A_,B)
				if not F and C.get(B0)and C[B0].get(A_):F=C[B0][A_]
				F=F.replace('更新至','🆕');d=C.get(BQ)
				if d:F='▶'+D.zh(d.get(Az))+'  '+F
				c.append({Q:q+e,O:f,U:D.format_img(N),X:F})
			J[H]=c;J[h]=pg;J[t]=9999;J[u]=90;J[p]=999999
		return J
	def get_timeline(E,tid,pg):
		a='pub_index';Z='ep_cover';D={};b='https://api.bilibili.com/pgc/web/timeline/v2?season_type={0}&day_before=2&day_after=4'.format(tid);c=E._get_sth(b,P);d=c.text;F=I.loads(d)
		if F[M]==0:
			T=[];G=F[AM]['latest']
			for C in G:J=A(C[AY]).strip();K=C[R].strip();N=C[Z].strip();S='🆕'+C[a]+'  ❤ '+C['follows'].replace('系列',B).replace('追番',B);T.append({Q:q+J,O:K,U:E.format_img(N),X:S})
			W=[];Y=F[AM]['timeline']
			for e in range(V(Y)):
				G=Y[e][BR]
				for C in G:
					if A(C['published'])==L:J=A(C[AY]).strip();K=A(C[R]).strip();N=A(C[Z]).strip();f=A(x.strftime('%m-%d %H:%M',x.localtime(C['pub_ts'])));S=f+'   '+C[a];W.append({Q:q+J,O:K,U:E.format_img(N),X:S})
			D[H]=W+T;D[h]=1;D[t]=1;D[u]=90;D[p]=999999
		return D
	def get_live(G,pg,parent_area_id,area_id):
		V='recommend_room_list';K=parent_area_id;D={}
		if K==AG:J='https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getList?platform=web&page=%s'%pg;N=G._get_sth(J)
		else:
			J='https://api.live.bilibili.com/xlive/web-interface/v1/second/getList?platform=web&parent_area_id=%s&area_id=%s&sort_type=online&page=%s'%(K,area_id,pg)
			if K==y:J='https://api.live.bilibili.com/room/v1/room/get_user_recommend?page=%s&page_size=%s'%(pg,G.userConfig[Y])
			N=G._get_sth(J,P)
		S=I.loads(N.text)
		if S[M]==0:
			T=[];C=S[E]
			if V in C:C=C[V]
			elif H in C:C=C[H]
			for F in C:
				W=A(F[Cc]).strip();Z=F[R].replace(k,B).replace(l,B).replace(AJ,AK);L=F.get(Cd)
				if not L:L=F.get(i)
				a='👁'+F[Ca][Cb].strip()+Ah+F[A8].strip();T.append({Q:W,O:Z,U:G.format_img(L),X:a})
			D[H]=T;D[h]=pg;D[t]=9999;D[u]=99;D[p]=999999
		return D
	get_up_videos_result={}
	def get_up_videos(C,mid,pg,order):
		S=order;L=pg;D=mid;G={}
		if not D.isdigit():
			if F(L)==1:
				C.get_up_videos_mid=D=C.detailContent_args.get(W,B)
				if not D in C.get_up_videos_result:C.get_up_videos_result.clear();C.get_up_videos_result[D]=[]
			else:D=C.get_up_videos_mid
		if F(L)==1:C.get_up_info_event.clear();C.pool.submit(C.get_up_info,D)
		T=V=B
		if S==Ce:V=S;S=Ai
		elif S==Cf:
			T='投稿: ';K=C.get_up_videos_result.get(D,[])
			if K:G[H]=K;return G
		Z=L
		if V:C.get_up_info_event.wait();Z=C.up_info[D][Bw]-F(L)+1
		e=C.encrypt_wbi(mid=D,pn=Z,ps=C.userConfig[Y],order=S);f=f"https://api.bilibili.com/x/space/wbi/arc/search?{e}";g=C._get_sth(f,P);i=g.text;b=I.loads(i);K=[]
		if b[M]==0:
			j=b[E][H]['vlist']
			for N in j:
				m=A(N[a]).strip();n=N[R].strip().replace(k,B).replace(l,B);o=N[Ay].strip();c=C.second_to_time(C.str2sec(A(N['length']).strip()))+BP+C.zh(N[Bx])
				if not T:c+=By+C.zh(N['video_review'])
				K.append({Q:v+m,O:T+n,U:C.format_img(o),X:c})
			if V:K.reverse()
			if F(L)==1:
				C.get_up_info_event.wait();d=C.up_info[D][J]+Cg
				if T:d='UP: '+C.up_info[D][J]
				q={Q:AZ+A(D),O:d,U:C.format_img(C.up_info[D][A7]),X:C.up_info[D][Aj]+'  👥'+C.up_info[D][Ak]+'  🎬'+A(C.up_info[D][BS])};K.insert(0,q)
			if T:C.get_up_videos_result[D]=K
			G[H]=K;G[h]=L;G[t]=99;G[u]=99;G[p]=999999
		return G
	history_view_at=0
	def get_history(D,type,pg):
		W='progress';G={}
		if F(pg)==1:D.history_view_at=0
		Z='https://api.bilibili.com/x/web-interface/history/cursor?ps={0}&view_at={1}&type={2}'.format(D.userConfig[Y],D.history_view_at,type)
		if type==BT:Z='https://api.bilibili.com/x/v2/history/toview'
		e=D._get_sth(Z);T=I.loads(e.text)
		if T[M]==0:
			b=[];V=T[E].get(H,[])
			if type==BT:V=D.pagination(V,pg)
			else:D.history_view_at=T[E]['cursor']['view_at']
			for C in V:
				J=C.get('history',B)
				if J:K=J['business'];N=A(J['oid']).strip();c=C[i].strip();S=A(J[Bz]).strip()
				else:K=BN;N=A(C[a]).strip();c=C[Ay].strip();S=A(C[h][Bz]).strip()
				if K=='article':continue
				elif K=='pgc':N=A0+A(J['epid']);d=C[p];S=C.get('show_title')
				elif K==BN:N=v+N;d=C[Ch]
				f=C[R].replace(k,B).replace(l,B).replace(AJ,AK)
				if K==AW:g=C.get('badge',B);P=g+Ah+C['author_name'].strip()
				else:
					if A(C[W])=='-1':P='已看完'
					elif A(C[W])==L:P='刚开始看'
					else:j=A(D.second_to_time(C[W])).strip();P='看到  '+j
					if not d in[0,1]and S:P+=' ('+A(S)+')'
				b.append({Q:N,O:f,U:D.format_img(c),X:P})
			G[H]=b;G[h]=pg;G[t]=9999;G[u]=90;G[p]=999999
		return G
	def get_fav_detail(F,pg,mlid,order):
		K='cnt_info';D={};L='https://api.bilibili.com/x/v3/fav/resource/list?media_id=%s&order=%s&pn=%s&ps=10&platform=web&type=0'%(mlid,order,pg);N=F._get_sth(L);P=N.text;G=I.loads(P)
		if G[M]==0:
			J=[];S=G[E].get('medias',[])
			for C in S:
				if C.get(r)in[2]and C.get(R)!='已失效视频':T=A(C[m]).strip();V=C[R].replace(k,B).replace(l,B).replace(AJ,AK);W=C[i].strip();Y=A(F.second_to_time(C[d])).strip()+BP+F.zh(C[K][Bx])+Ci+F.zh(C[K][Al]);J.append({Q:v+T+'_mlid'+A(mlid),O:V,U:F.format_img(W),X:Y})
			D[H]=J;D[h]=pg;D[t]=9999;D[u]=99;D[p]=999999
		return D
	get_up_info_event=j.Event();up_info={}
	def get_up_info(D,mid,**P):
		O='Official';K=mid
		if K in D.up_info:D.get_up_info_event.set()
		G=P.get(E)
		if not G:
			Q='https://api.bilibili.com/x/web-interface/card?mid={0}'.format(K);S=D._get_sth(Q);L=I.loads(S.text)
			if L[M]==0:G=L[E]
			else:D.get_up_info_event.set();return
		H=G['card'];C={};C[Aj]='未关注'
		if G[Aj]:C[Aj]='已关注'
		C[J]=H[J].replace(k,B).replace(l,B);C[A7]=H[A7];C[Ak]=D.zh(H[Ak]);C[B_]=D.zh(G[B_]);C[BS]=A(G['archive_count']).strip();C[Aa]=H[O][Aa]+Ab+H[O][R];N=divmod(F(C[BS]),D.userConfig[Y]);C[Bw]=N[0]
		if N[1]!=0:C[Bw]+=1
		D.up_info[K]=C;D.get_up_info_event.set()
	def get_vod_relation(H,id):
		if id.isdigit():F='aid='+A(id)
		elif'='in id:F=id
		else:F='bvid='+id
		J='https://api.bilibili.com/x/web-interface/archive/relation?'+F;K=H._get_sth(J);B=I.loads(K.text);C=[]
		if B[M]==0:
			B=B[E]
			if B[Cj]:C.append('已关注')
			else:C.append('未关注')
			D=[]
			if B[Ck]:D.append('⭐')
			if B[B1]:D.append('👍')
			G=B.get(C0)
			if G:D.append('💰'*G)
			if V(D)==3:C.append('👍💰⭐')
			else:C.extend(D)
			if B['dislike']:C.append('👎')
			if B['season_fav']:C.append('已订阅合集')
		return C
	def get_channel(C,pg,cid,order):
		P=order;N='uri';F={}
		if A(pg)==T:C.channel_offset=B
		if P==Cl:R='https://api.bilibili.com/x/web-interface/web/channel/featured/list?channel_id={0}&filter_type=0&offset={1}&page_size={2}'.format(cid,C.channel_offset,C.userConfig[Y])
		else:R='https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id={0}&sort_type={1}&offset={2}&page_size={3}'.format(cid,P,C.channel_offset,C.userConfig[Y])
		c=C._get_sth(R,g);L=I.loads(c.text)
		if L.get(M)==0:
			C.channel_offset=L[E].get(CY);S=[];G=L[E][H]
			if pg==T and BK in G[0]:e=G[0][BK];del G[0];G=e+G
			for D in G:
				if N in D and C1 in D[N]:V=C.find_bangumi_id(D[N])
				else:V=v+A(D[m]).strip()
				f=D[J].replace(k,B).replace(l,B).replace(AJ,AK);j=D[i].strip();K='▶'+A(D['view_count']);W=D.get(d,B)
				if W:K=A(C.second_to_time(C.str2sec(W))).strip()+'  '+K
				Z=D.get(Al,B);a=D.get('like_count',B);b=D.get('follow_count',B)
				if Z:K+=By+C.zh(Z)
				elif a:K+='  👍'+A(a)
				elif b:K+='  ❤'+A(b)
				S.append({Q:V,O:f,U:C.format_img(j),X:K})
			F[H]=S;F[h]=pg;F[t]=9999;F[u]=99;F[p]=999999
		return F
	def get_follow(G,pg,sort):
		K=pg;D=sort;L={}
		if D==BU:N='https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=10&order=desc&order_type=attention'.format(G.userid,K)
		elif D==C2:N='https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=10&order=desc&order_type='.format(G.userid,K)
		elif D==B2:N='https://api.live.bilibili.com/xlive/web-ucenter/v1/xfetter/GetWebList?page={0}&page_size=10'.format(K)
		elif D==BV:N='https://api.bilibili.com/x/v2/history?pn={0}&ps=15'.format(K)
		elif D==B3:N='https://api.bilibili.com/x/relation/tag?mid={0}&tagid=-10&pn={1}&ps=10'.format(G.userid,K)
		elif D==C3:N='https://api.bilibili.com/x/relation/whispers?pn={0}&ps=10'.format(K)
		else:N='https://api.bilibili.com/x/relation/followers?vmid={0}&pn={1}&ps=10&order=desc&order_type=attention'.format(G.userid,K)
		b=G._get_sth(N);S=I.loads(b.text)
		if S[M]!=0:return L
		if D==B3 or D==BV:T=S[E]
		elif D==B2:T=S[E]['rooms']
		else:T=S[E][H]
		if F(K)==1:G.recently_up_list=[]
		a=[]
		for C in T:
			V=B
			if D==BV:
				P=AZ+A(C[AX][W])
				if P in G.recently_up_list:continue
				G.recently_up_list.append(P);Y=A(C[AX][J]).strip();Z=A(C[AX][A7]).strip()
			elif D==B2:P=A(C[Cm]);Y=C[R].replace(k,B).replace(l,B).replace(AJ,AK);Z=C['cover_from_user'].strip();V=C[A8].strip()
			else:P=AZ+A(C[W]);Y=A(C[A8]).strip();Z=A(C[A7]).strip()
			if C4 in C and C[C4]==1:V=B3
			a.append({Q:P,O:Y,U:G.format_img(Z),X:V})
		L[H]=a;L[h]=K;L[t]=9999;L[u]=99;L[p]=999999;return L
	homeVideoContent_result={}
	def homeVideoContent(A):
		if not A.homeVideoContent_result:B=A.get_found(rid=L,tid=BW,pg=1)[H][0:F(A.userConfig[Bl])];A.homeVideoContent_result[H]=B
		return A.homeVideoContent_result
	def categoryContent(H,tid,pg,filter,extend):
		J=pg;E=tid;D=extend;H.stop_heartbeat_event.set()
		if E==AG:
			if A2 in D:E=D[A2]
			if E.isdigit():
				E=F(E)
				if E>10000:E-=10000;return H.get_timeline(tid=E,pg=J)
				R=E;E=BW;return H.get_found(tid=E,rid=R,pg=J)
			R=L;return H.get_found(tid=E,rid=R,pg=J)
		elif E==Ad:
			E=T;I=y;U='-1'
			if A2 in D:E=D[A2]
			if b in D:I=D[b]
			if C5 in D:
				if I==y:I=A1
				U=D[C5]
			return H.get_bangumi(E,J,I,U)
		elif E==AI:
			M=L;I=Ai
			if W in D:M=D[W]
			if b in D:I=D[b]
			if M==L and not H.userid or M=='登录':return H.get_Login_qrcode(J)
			return H.get_dynamic(pg=J,mid=M,order=I)
		elif E==Ae:
			I='hot';P=random.choice(H.userConfig[Aw]);P=P[C]
			if b in D:I=D[b]
			if n in D:P=D[n]
			return H.get_channel(pg=J,cid=P,order=I)
		elif E==AH:
			E=y;X=L
			if A2 in D:E=D[A2]
			if K in E:a=E.split(K);E=a[0];X=a[1]
			return H.get_live(pg=J,parent_area_id=E,area_id=X)
		elif E==A6:
			M=H.detailContent_args.get(W,B)
			if W in D:M=D[W]
			if not M or M=='登录':return H.get_Login_qrcode(J)
			c=H.config[Z].get(A6)
			if not M and c:
				for N in c:
					if N[S]==W:
						if V(N[G])>1:M=N[G][1][C]
						break
			I=Ai
			if b in D:I=D[b]
			return H.get_up_videos(mid=M,pg=J,order=I)
		elif E==BF:
			e=BU
			if C6 in D:e=D[C6]
			return H.get_follow(J,e)
		elif E==Af:
			O=A(H.userConfig[Bm])
			if Ag in D:O=D[Ag]
			f=H.config[Z].get(Af)
			if O in[T,A1]:return H.get_bangumi(tid=O,pg=J,order='追番剧',season_status=B)
			elif O==L and f:
				for N in f:
					if N[S]==Ag:
						if V(N[G])>1:O=N[G][2][C]
						break
			I='mtime'
			if b in D:I=D[b]
			return H.get_fav_detail(pg=J,mlid=O,order=I)
		elif E==BG:
			type=BW
			if r in D:type=D[r]
			if type==BM:return H.get_follow(pg=J,sort=BV)
			return H.get_history(type=type,pg=J)
		else:
			g=L
			if d in D:g=D[d]
			type=AB
			if r in D:type=D[r]
			I=Cn
			if b in D:I=D[b]
			Q=A(H.search_key);h=H.config[Z].get(BH)
			if not Q and h:
				for N in h:
					if N[S]==Ax:
						if V(N[G])>0:Q=N[G][0][C]
						break
			if Ax in D:Q=D[Ax]
			return H.get_search_content(key=Q,pg=J,duration_diff=g,order=I,type=type,ps=H.userConfig[Y])
	def get_search_content(D,key,pg,duration_diff,order,type,ps):
		K=pg;S=AU
		if not K.isdigit():S=K;K=1
		b=D.encrypt_wbi(keyword=key,page=K,duration=duration_diff,order=order,search_type=type,page_size=ps);c=f"https://api.bilibili.com/x/web-interface/wbi/search/type?{b}";e=D._get_sth(c,P);f=e.text;V=I.loads(f);F={}
		if V.get(M)==0 and AM in V[E]:
			Y=[];L=V[E].get(AM)
			if L and type==AW:L=L.get('live_room')
			if not L:return F
			for C in L:
				J=B
				if type==C7:G=AZ+A(C[W]).strip();T=C['upic'].strip();N='👥'+D.zh(C[Ak])+'  🎬'+D.zh(C[Ch]);J=C[A8]
				elif type==AW:G=A(C[Cc]).strip();T=C[i].strip();N='👁'+D.zh(C['online'])+Ah+C[A8]
				elif'media'in type:
					G=A(C[AY]).strip()
					if D.detailContent_args:
						g=D.detailContent_args.get(B4)
						if g:
							Z=[]
							for j in D.detailContent_args[B4]:Z.append(j[Q])
							if G+q in Z:continue
					G=q+G;T=C[i].strip();N=A(C[A_]).strip().replace('更新至','🆕')
				else:
					G=v+A(C[a]).strip();T=C[Ay].strip();N=A(D.second_to_time(D.str2sec(C[d]))).strip()+BP+D.zh(C[Bx])
					if S==AU:N+=By+D.zh(C[Al])
				if not J:J=C[R].replace(k,B).replace(l,B).replace(AJ,AK).replace('&amp;','&')
				if S:J=S+J
				Y.append({Q:G,O:J,U:D.format_img(T),X:N})
			F[H]=Y;F[h]=K;F[t]=9999;F[u]=99;F[p]=999999
		return F
	def cleanSpace(A,str):return str.replace('\n',B).replace('\t',B).replace('\r',B).replace(AL,B)
	def get_normal_episodes(C,episode):
		G=episode;L=H=B;M=G.get(a,B)
		if not M:M=C.detailContent_args[a]
		U=G.get(n,B);J=G.get(R,B)
		if not J:J=G.get(Bz,B)
		E=G.get(d,B)
		if not E:
			V=G.get(h,B)
			if V:E=V[d]
		D=I=W=Q=B;L=C.detailContent_args.get(B5,B)
		if L:
			L='_ss'+L;H=G.get(m,B)
			if H:H='_ep'+A(H)
			if E and A(E).endswith(C8):E=F(E/1000)
			if J.isdigit():J='第'+J+C.detailContent_args[C9]
			D=G.get('badge',B)
			if not C.session_vip.cookies and D=='会员'and C.userConfig[CT]or D=='付费'and C.userConfig[CU]:Q='_parse'
			if C.session_vip.cookies and C.userConfig[CR]:D=D.replace('会员',B)
			if C.userConfig[CQ]and D=='预告':D=D.replace('预告',B);W=1
			if D:D='【'+D+'】'
			I=G.get('long_title',B)
			if not D and I:I=AL+I
		S=J+D+I;S=S.replace(N,AC).replace(w,AD)
		if E:E='_dur'+A(E)
		O='{0}${1}_{2}{3}{4}{5}'.format(S,M,U,L,H,E);P=C.detailContent_args.get(B6,B)
		if K+A(P)==H:C.detailContent_args[B6]=O
		X=C.detailContent_args.get(Am)
		if K+A(P)==H or not P and X==AU:
			C.detailContent_args[Am]=B
			if C.userConfig[As]:C.get_vod_hot_reply_event.clear();C.pool.submit(C.get_vod_hot_reply,M)
		if L:
			if W:return O,B
			if Q:
				C.detailContent_args[An]=1
				if I:I='【解析】'+I
				J+=I;T='{0}${1}_{2}{3}{4}{5}{6}'.format(J,M,U,L,H,E,Q)
				if K+A(P)==H:C.detailContent_args[B6]+=N+T
			else:T=O
			return O,T
		else:return O
	def get_ugc_season(B,section,sections_len):
		C=section
		if sections_len>1:A=B.detailContent_args[Ao]+AL+C[R]
		else:A=B.detailContent_args[Ao]
		A=A.replace(N,AC).replace(w,AD);D=C.get(BR);E=N.join(f(B.get_normal_episodes,D));F=A,E;return F
	get_vod_hot_reply_event=j.Event()
	def get_vod_hot_reply(G,oid):
		b='member';c='http://api.bilibili.com/x/v2/reply/main?type=1&ps=30&oid='+A(oid);d=G._get_sth(c,P);L=I.loads(d.text)
		if L[M]==0:
			H=L[E].get('replies');Y=L[E].get('top_replies')
			if H and Y:H=Y+H
			if H:
				e=L[E]['upper'][W];T=[];U=[]
				for D in H:
					f=D['rpid'];J=D[b]['sex']
					if J and J=='女':J='👧'
					else:J='👦'
					V=J+D[b][A8]+'：';g=D[W]
					if g==e:V='🆙'+V
					h='👍'+G.zh(D[B1]);Z=D[BO][Co]
					if'/note-app/'in Z:continue
					F=h+AL+V+Z;F=F.replace(N,AC).replace(w,AD);F+=w+A(oid)+K+A(f)+'_notplay_reply';T.append(F);i=D[BO].get('jump_url',{})
					for(C,X)in i.items():
						if not X.get('app_url_schema')and not X.get('pc_url'):
							if C.startswith('https://www.bilibili.com/'):
								C=A(C).split('?')[0].split(AA)
								while C[-1]==B:C.pop(-1)
								C=C[-1]
							if C.startswith(Cp)or C.startswith(BX)or C.startswith(A0)or C.startswith(q):
								S=A(X[R]).replace(N,AC).replace(w,AD);a={Q:A(C),O:'评论：'+S}
								if not a in U:U.append(a)
								S='快搜：'+A(C)+AL+S;F=S+BY;T.append(F)
				G.detailContent_args[Am]=N.join(T);G.detailContent_args[Cq]=U
		G.get_vod_hot_reply_event.set()
	detailContent_args={}
	def detailContent(G,array):
		c=array;G.stop_heartbeat_event.set();L=c[0]
		if L.startswith(BZ):return G.interaction_detailContent(L)
		G.detailContent_args={}
		if L.startswith(Cp):
			try:
				A8=CM(url=L,headers=G.header,allow_redirects=False);f=A8.headers['Location'].split('?')[0].split(AA)
				while f[-1]==B:f.pop(-1)
				L=f[-1]
				if not L.startswith(BX,0,2):return{}
			except:return{}
		id=t=j=B;G.get_vod_hot_reply_event.set()
		if L.startswith(Cr):
			L=L.split(K)
			if L[1]=='tab&filter':return G.setting_tab_filter_detailContent()
			elif L[1]=='liveExtra':return G.setting_liveExtra_detailContent()
			elif L[1]=='login':A9=L[2];return G.setting_login_detailContent(A9)
		elif L.startswith(v)or L.startswith(BX):
			for T in L.split(K):
				if T.startswith(v):id=T.replace(v,B,1);j='aid='+A(id)
				elif T.startswith(BX):id=T;j='bvid='+id
				elif T.startswith(Ag):t=T.replace(Ag,B,1)
			if G.userConfig[As]:G.detailContent_args[Am]=B;G.get_vod_hot_reply_event.clear();G.pool.submit(G.get_vod_hot_reply,id)
		elif AZ in L:return G.up_detailContent(c)
		elif q in L or A0 in L:return G.ysContent(c)
		elif L.isdigit():return G.live_detailContent(c)
		AB=G.pool.submit(G.get_vod_relation,j);f='https://api.bilibili.com/x/web-interface/view/detail?'+j;AE=G._get_sth(f,P);m=I.loads(AE.text)
		if m[M]!=0:return{}
		S=m[E]['View'];z=S.get(Ba,B)
		if C1 in z:
			AF=G.find_bangumi_id(z);u=[]
			for T in c:u.append(T)
			u[0]=AF;return G.ysContent(u)
		G.detailContent_args[W]=A1=A(S[AX][W]);G.detailContent_args[a]=L=S.get(a);G.pool.submit(G.get_up_info,mid=A1,data=m[E].get('Card'));n=S.get('ugc_season')
		if n:
			G.detailContent_args[Ao]=n[R];A2=n['sections'];AG=V(A2);A3=[]
			for AH in A2:o=G.pool.submit(G.get_ugc_season,AH,AG);A3.append(o)
		A4=m[E].get('Related');A5=S['pages'];AI=S[R].replace(k,B).replace(l,B);AJ=S[Ay];AK=S[AX][J];AL=S[Aa].strip();AM=S['tname'];AP=x.strftime('%Y%m%d',x.localtime(S[Ai]));g=S[BQ];Z=[];Z.append('▶'+G.zh(g[Az]));Z.append('💬'+G.zh(g[Al]));Z.append('👍'+G.zh(g[B1]));h=S.get('honor_reply')
		if h:Z.insert(0,'🏅'+h['honor'][0][Aa])
		if not h or h and h['honor'][0][r]==4:Z.append('💰'+G.zh(g[C0]));Z.append('⭐'+G.zh(g[Ck]))
		AQ=A(S[d]).strip();An=S[d];A6=S['rights'].get('is_stein_gate',0);i={Q:v+A(L),O:AI,U:AJ,BI:AM,CA:AP,CB:Cs,X:AQ,Bb:Ab.join(Z),Ac:AL};y=[]
		if G.userid:
			AR=Ct;AS=Cu;AT='👍点赞$1_notplay_like';AU='👍🏻取消点赞$2_notplay_like';AV='👍💰投币$1_notplay_coin';AW='👍💰💰投2币$2_notplay_coin';AY='👍💰⭐三连$notplay_triple';p=[AR,AY,AT,AV,AW,AS,AU]
			if t:Ad=f"☆取消收藏${t}_del_notplay_fav";p.append(Ad)
			for s in G.userConfig.get(CW,[]):Ae=s[D].replace(N,AC).replace(w,AD);Af=s[C];s='⭐{}${}_add_notplay_fav'.format(Ae,Af);p.append(s)
			Ah=F(G.userConfig[Aq])
			if Ah>116:p.append('⚠️限高1080$116_notplay_vodTMPQn')
			y=[N.join(p)]
		Y=[];b=[]
		if A5:
			Y=['B站']
			if A6:Y=['互动视频【快搜继续】']
			b=[N.join(G.pool.map(G.get_normal_episodes,A5))]
		if y:Y.append('做点什么');b.extend(y)
		if A4:Y.append('相关推荐');b.append(N.join(G.pool.map(G.get_normal_episodes,A4)))
		if G.userConfig[As]:
			G.get_vod_hot_reply_event.wait();A7=G.detailContent_args.get(Am,B)
			if A7:Y.append('热门评论');b.extend([A7])
		if n:
			for o in Bi(A3):Y.append(o.result()[0]);b.append(o.result()[1])
		i[AN]=e.join(Y);i[AO]=e.join(b);i[CC]='🆙 '+AK+Cv+G.up_info[A1][Ak]+Ab+Ab.join(AB.result())
		if A6:G.detailContent_args['AllPt']=Y.copy();G.detailContent_args['AllPu']=b.copy();G.detailContent_args[Cw]=i.copy()
		Aj={H:[i]};return Aj
	def interaction_detailContent(C,array=B):
		F=array;F=F.split(K);V=G=0
		for D in F:
			if D.startswith(BZ):G=D.replace(BZ,B)
			elif D.startswith(n):V=D.replace(n,B)
		W=C.detailContent_args.get(a);c=C.detailContent_args.get(B7);J='https://api.bilibili.com/x/stein/edgeinfo_v2?aid={0}&graph_version={1}&edge_id={2}'.format(W,c,G);d=C._get_sth(J,P);f=I.loads(d.text);L=f.get(E);X={}
		if L:
			g=L['edges'].get('questions',[]);M=[]
			for Y in g:
				S=A(Y.get(R,B))
				if S:S+=AL
				for T in Y.get('choices',[]):h=A(T[m]);i=A(T[n]);j=A(T.get('option',B));M.append({Q:BZ+h+K+n+i,O:'互动：'+S+j})
			C.detailContent_args[CD]=M.copy()
			if G:
				Z=C.detailContent_args['AllPt'].copy()
				if not M:Z[0]='互动视频'
				b=C.detailContent_args['AllPu'].copy();k=A(L[R]).replace(N,AC).replace(w,AD);J='{0}${1}_{2}'.format(k,W,V);b[0]=J;U=C.detailContent_args[Cw].copy();U[AN]=e.join(Z);U[AO]=e.join(b);X[H]=[U]
		return X
	def up_detailContent(D,array):D.detailContent_args[W]=E=array[0].replace(AZ,B);D.get_up_info_event.clear();D.pool.submit(D.get_up_info,E);I=Cx;K='关注$1_notplay_follow';L='取消关注$2_notplay_follow';M='悄悄关注$3_notplay_follow';P='特别关注$-10_notplay_special_follow';R='取消特别关注$0_notplay_special_follow';F=[I,K,M,P,L,R];F=N.join(F);D.get_up_info_event.wait();C=D.up_info[E];G={Q:AZ+A(E),O:C[J]+Cg,U:C[A7],X:B,'vod_tags':'mv',Bb:'👥 '+C[Ak]+'\u3000🎬 '+C[BS]+'\u3000👍 '+C[B_],CC:'🆙 '+C[J]+Ab+C[Aj]+Cy+A(E),Ac:C[Aa],AN:'关注TA$$$视频投稿在动态标签——筛选——上个UP，选择后查看'};G[AO]=F;S={H:[G]};return S
	def setting_login_detailContent(E,key):
		b='检查失败';M=key;G='f';D='d';C='c';c=E.cookie_dic_tmp.get(M,B);J=B
		if not c:J=E.get_cookies(M)
		if J:J=f"【{J}】通过手机客户端扫码确认登录后点击相应按钮设置账号"
		else:J='【已扫码并确认登录】请点击相应按钮设置当前获取的账号为：'
		R={O:'登录与设置',Ac:'通过手机客户端扫码并确认登录后，点击相应按钮设置cookie，设置后不需要管嗅探结果，直接返回二维码页面刷新，查看是否显示已登录，已登录即可重新打开APP以加载全部标签'};X=['登录$$$退出登录'];P=[];d=J+BY;f='设置为主账号，动态收藏关注等内容源于此$'+A(M)+'_master_login_setting';g='设置为备用的VIP账号，仅用于播放会员番剧$'+A(M)+'_vip_login_setting';P.append(N.join([d,f,g]));h='点击相应按钮退出账号>>>$ ';i='退出主账号$master_logout_setting';j='退出备用的VIP账号$vip_logout_setting';P.append(N.join([h,i,j]));Y=[{G:'主页站点推荐栏',C:Bl,D:{AR:'3图',AV:'4图','6':'6图','8':'8图','10':'10图'}},{G:'视频画质',C:Aq,D:E.vod_qn_id},{G:'视频编码',C:Bn,D:E.vod_codec_id},{G:'音频码率',C:Ar,D:E.vod_audio_id},{G:'收藏默认显示',C:Bm,D:{L:'默认收藏夹',T:'追番',A1:'追剧'}},{G:'上传播放进度',C:BC,D:{L:'关','15':'开'}},{G:'直播筛选细化',C:Bo,D:{L:'关',T:'开'}}];S={G:'检查更新',C:CE};U=E.userConfig.get(AP,b);V=Z=0
		if U!=b:U='远端：'+A(E.userConfig[AP][CF]);Z=1;V=E.userConfig[AP].get(Bc)
		S[D]={A(Z):U}
		if V:S[D][AL]=V
		Y.insert(0,S)
		for I in Y:
			X.append(I[G])
			if I[C]==CE:Q=E.userConfig[Bk]
			else:Q=I[D][A(F(E.userConfig[I[C]]))]
			if Ar==I[C]:Q=A(Q).replace(C8,'k')
			a=['当前：'+Q+BY]
			for(id,W)in I[D].items():
				if Ar==I[C]:W=A(W).replace(C8,'k')
				a.append(W+w+A(id)+K+I[C]+'_setting')
			P.append(N.join(a))
		R[AN]=e.join(X);R[AO]=e.join(P);k={H:[R]};return k
	def setting_tab_filter_detailContent(I):
		L={O:'标签与筛选',Ac:'依次点击各标签，同一标签第一次点击为添加，第二次删除，可以返回到二维码页后重进本页查看预览，最后点击保存，未选择的将追加到末尾，如果未保存就重启app，将丢失未保存的配置'};M=[];P=[];U=[{D:At,C:'标签'},{D:BD,C:'推荐[分区]'},{D:BE,C:'推荐[排行榜]'},{D:z,C:AH}]
		for Q in U:
			E=Q[D];M.append(Q[C]);F=I.userConfig.get(A(E)+AE,[]);R=B
			if F:R='【未保存】'
			else:F=I.userConfig.get(E,[])
			if not F:F=I.defaultConfig.get(E)
			if F and type(F[0])==A3:F=s(f(lambda x:x[D],F))
			S=['当前: '+','.join(F)+BY,f"{R}点击这里保存$_{E}_save_setting",f"点击这里恢复默认并保存$_{E}_clear_setting"];J=I.defaultConfig[E].copy()
			if E==At and not A6 in J:J.append(A6)
			elif E==z:V=I.userConfig.get(A5,[]);J.extend(V.copy())
			for G in J:
				T=A(G)
				if type(G)==A3:T=G[D]+Ap+G[C].replace(K,Ap);G=G[D]
				S.append(f"{G}${T}_{E}_setting")
			P.append(N.join(S))
		L[AN]=e.join(M);L[AO]=e.join(P);W={H:[L]};return W
	def setting_liveExtra_detailContent(I):
		Q='_liveFilter_setting';F={O:CX,Ac:'点击想要添加的标签，同一标签第一次点击为添加，第二次删除，完成后在[标签与筛选]页继续操作，以添加到直播筛选分区列中'};J=['已添加'];R=I.userConfig.get(A5,[]);E=['点击相应标签(只)可以删除$ #清空$clear_liveFilter_setting']
		for B in R:S=B[C];B=B[D];E.append(B+w+'del_'+B+K+S+Q)
		E=[N.join(E)];T=I.userConfig.get(AT,{})
		for(U,W)in T.items():
			L=W[G][G]
			if V(L)==1:continue
			J.append(U);M=[]
			for P in L:B=A(P[D]).replace(K,'-').replace(N,AC).replace(w,AD);id=A(P[C]).replace(K,Ap).replace(N,AC).replace(w,AD);M.append(B+'$add_'+B+K+id+Q)
			E.append(N.join(M))
		F[AN]=e.join(J);F[AO]=e.join(E);X={H:[F]};return X
	def get_all_season(C,season):
		B=season;D=A(B[AY]);E=B[Ao]
		if D==C.detailContent_args[B5]:C.detailContent_args[B8]=E
		F=B[i];G=B[B0][A_];H={Q:D+q,O:'系列：'+E,U:C.format_img(F),X:G};return H
	def get_bangumi_section(B,section):
		A=section;C=A[R].replace(N,AC).replace(w,AD);D=A[r]
		if D in[1,2]and V(A['episode_ids'])==0:E=A[BR];F=N.join(f(lambda x:B.get_normal_episodes(x)[0],E));return C,F
	def ysContent(C,array):
		p='rating';E=array[0]
		if A0 in E:C.detailContent_args[B6]=E;E='ep_id='+E.replace(A0,B)
		elif q in E:E='season_id='+E.replace(q,B)
		t='https://api.bilibili.com/pgc/view/web/season?{0}'.format(E);u=C._get_sth(t,P);v=I.loads(u.text);D=v[AM];C.detailContent_args[B5]=A(D[AY]);w=D[R];C.detailContent_args[B8]=D[Ao];C.detailContent_args[C9]='集'
		if D[r]in[1,4]:C.detailContent_args[C9]='话'
		M=D.get(B4)
		if V(M)==1:C.detailContent_args[B8]=M[0][Ao];M=0
		else:C.detailContent_args[B4]=s(C.pool.map(C.get_all_season,M))
		f=D.get(BR);g=[]
		for J in D.get('section',[]):
			if J:b=C.pool.submit(C.get_bangumi_section,J);g.append(b)
		x=D[i];y=D['share_sub_title'];z=D['publish']['pub_time'][0:4];A1=D['evaluate'];A2=D[B0][Aa];S=D[BQ];c='▶'+C.zh(S['views'])+Ci+C.zh(S['danmakus'])+'\u3000👍'+C.zh(S['likes'])+'\u3000💰'+C.zh(S['coins'])+'\u3000❤'+C.zh(S['favorites'])
		if p in D:c=A(D[p]['score'])+'分\u3000'+c
		d={Q:q+C.detailContent_args[B5],O:w,U:x,BI:y,CA:z,CB:Cs,X:A2,Bb:c,Ac:A1};a=[];G=[]
		if C.userid:
			a=['做点什么'];G='是否追番剧$ #❤追番剧$add_notplay_zhui#💔取消追番剧$del_notplay_zhui';A3=F(C.userConfig[Aq])
			if A3>116:G+='#⚠️限高1080$116_notplay_vodTMPQn'
			G=[G]
		if M:a.append('更多系列');G.append('更多系列在快速搜索中查看$ #')
		h=[];T=[];j=[];W=[];k=[];L=[]
		if f:
			for(l,m)in C.pool.map(C.get_normal_episodes,f):
				if m:T.append(l);L.append(m)
				else:W.append(l)
			if T:h=[C.detailContent_args[B8]];T=[N.join(T)]
			if W:j=['预告'];W=[N.join(W)]
			if not C.detailContent_args.get(An):L=[]
			if L:k=[A(C.detailContent_args[B8])+'【解析】'];L=[N.join(L)]
		Y=k+h+j;Z=L+T+W
		for b in Bi(g):
			J=b.result()
			if J:Y.append(J[0]);Z.append(J[1])
		n=C.detailContent_args.get(B6,B)
		if K in n:Y=['B站']+Y;Z=[n]+Z
		if C.userConfig[As]:
			C.get_vod_hot_reply_event.wait();o=C.detailContent_args.get(Am,B)
			if o:a.append('热门评论');G.append(o)
		Y.insert(1,e.join(a));Z.insert(1,e.join(G));d[AN]=e.join(Y);d[AO]=e.join(Z);A4={H:[d]};return A4
	def get_live_api2_playurl(O,room_id):
		Q=room_id;D='qn';R=[];S=[];H='https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id={0}&no_playurl=0&mask=1&qn=0&platform=web&protocol=0,1&format=0,1,2&codec=0,1&dolby=5&panorama=1'.format(Q);Z=O._get_sth(H,P);U=I.loads(Z.text)
		if U[M]==0:
			J=U[E].get(Cz,B)
			if J:
				a=J[CG][C_];C={Bd:{'avc':L,'hevc':T},Be:{'flv':L,'ts':T,'fmp4':A1}};C[D]=A3(O.pool.map(lambda x:(x[D],x[Aa]),J[CG]['g_qn_desc']));V=[]
				for b in a:V.extend(b[Be])
				F={}
				for W in V:
					format=A(W.get('format_name'))
					for X in W[Bd]:
						Y=A(X.get('codec_name'));c=X.get('accept_qn')
						for G in c:
							H=format+K+Y+'$liveapi2_'+A(G)+K+C[Be][format]+K+C[Bd][Y]+K+A(Q)
							if not F.get(C[D][G]):F[C[D][G]]=[]
							F[C[D][G]].append(H)
				for(d,e)in F.items():R.append(d);S.append(N.join(e))
		f={'From':R,o:S};return f
	def live_detailContent(C,array):
		F=array[0];X=C.pool.submit(C.get_live_api2_playurl,F);c='https://api.live.bilibili.com/room/v1/Room/get_info?room_id='+A(F);d=C._get_sth(c,P);Y=I.loads(d.text);Z={}
		if Y.get(M)==0:
			D=Y[E];C.detailContent_args[W]=S=A(D['uid']);C.get_up_info_event.clear();C.pool.submit(C.get_up_info,S);f=D[R].replace(k,B).replace(l,B);g=D.get(Cd);h=D.get('description');i=D.get('parent_area_name')+'--'+D.get('area_name');G=D.get(CZ,B)
			if G:G='开播时间：'+D.get('live_time').replace('-','.')
			else:G='未开播'
			K={Q:F,O:f,U:g,BI:i,CA:B,CB:'bililivedanmu',Bb:'房间号：'+F+Cy+S+Ab+G,Ac:h};T=B;a=B
			if C.userid:T='关注Ta';j=Cx;m=Ct;n=Cu;p=[j,m,n];a=N.join(p)
			L=X.result().get('From',[]);V=X.result().get(o,[])
			if L:q='API_1';r='flv线路原画$platform=web&quality=4_'+F+'#flv线路高清$platform=web&quality=3_'+F+'#h5线路原画$platform=h5&quality=4_'+F+'#h5线路高清$platform=h5&quality=3_'+F;L.append(q);V.append(r)
			if T:L.insert(1,T);V.insert(1,a)
			K[AN]=e.join(L);K[AO]=e.join(V);C.get_up_info_event.wait();b=C.up_info[S];K[CC]='🆙 '+b[J]+Cv+C.zh(D.get(Cj))+Ab+b[Aj];Z[H]=[K]
		return Z
	search_key=B
	def searchContent(A,key,quick):
		F=quick
		if not A.session_fake.cookies:A.pool.submit(A.getFakeCookie,AF)
		for C in A.task_pool:C.cancel()
		A.task_pool=[];A.search_key=key;E=A.detailContent_args.get(W,B)
		if F and E:G=A.pool.submit(A.get_up_videos,E,1,Cf)
		I={AB:B,D0:'番剧: ',D1:'影视: ',C7:'用户: ',AW:'直播: '}
		for(type,J)in I.items():C=A.pool.submit(A.get_search_content,key=key,pg=J,duration_diff=0,order=B,type=type,ps=A.userConfig[Y]);A.task_pool.append(C)
		D={H:[]}
		for C in Bi(A.task_pool):K=C.result().get(H,[]);D[H].extend(K);A.task_pool.remove(C)
		if F:
			if E:D[H]=A.detailContent_args.get(CD,[])+G.result().get(H,[])+A.detailContent_args.get(Cq,[])+D[H]
			else:D[H]=A.detailContent_args.get(B4,[])+D[H]
		return D
	stop_heartbeat_event=j.Event()
	def start_heartbeat(C,aid,cid,ids):
		N=aid;L=cid;M=O=S=B
		for G in ids:
			if q in G:O=G.replace(q,B)
			elif A0 in G:S=G.replace(A0,B)
			elif CH in G:M=F(G.replace(CH,B))
		H='https://api.bilibili.com/x/player/v2?aid={0}&cid={1}'.format(N,L);Q=C._get_sth(H);X=I.loads(Q.text);D=X.get(E,{});T=D.get(CD,{})
		if T.get(B7):
			U=T.get(B7);Y=C.detailContent_args.get(B7)
			if Y!=U:C.detailContent_args[B7]=U;C.pool.submit(C.interaction_detailContent)
		R=F(C.userConfig[BC])
		if not C.userid or not R:return
		if not M:H='https://api.bilibili.com/x/web-interface/view?aid={0}&cid={1}'.format(N,L);Q=C._get_sth(H,P);Z=I.loads(Q.text);M=Z[E][d]
		J=0
		if F(D.get('last_play_cid',0))==F(L):
			V=F(D.get('last_play_time'))
			if V>0:J=F(V/1000)
		W=F((M-J)/R)+1;H='https://api.bilibili.com/x/click-interface/web/heartbeat';D={a:A(N),n:A(L),CI:A(C.csrf)}
		if O:D['sid']=A(O);D['epid']=A(S);D[r]=AV
		K=0;C.stop_heartbeat_event.clear()
		while AF:
			if K==R or C.stop_heartbeat_event.is_set():J+=K;K=0
			if not K:
				W-=1
				if not W:J=-1;C.stop_heartbeat_event.set()
				D['played_time']=A(J);C.pool.submit(C._post_sth,url=H,data=D)
				if C.stop_heartbeat_event.is_set():break
			x.sleep(1);K+=1
	wbi_key={}
	def get_wbiKey(A,wts):D='wbi_img';C=A.fetch(CV,headers=A.header);F=C.json()[E][D]['img_url'];G=C.json()[E][D]['sub_url'];H=[46,47,18,2,53,8,23,32,15,50,10,31,58,3,45,35,27,43,5,49,33,9,42,19,29,28,14,39,12,38,41,13,37,48,7,16,24,55,40,61,26,17,0,1,60,51,30,4,22,25,54,21,56,59,6,63,57,62,11,36,20,34,44,52];I=F.split(AA)[-1].split('.')[0]+G.split(AA)[-1].split('.')[0];J=reduce(lambda s,i:s+I[i],H,B);A.wbi_key={S:J[:32],CJ:wts}
	def encrypt_wbi(D,**C):
		E=Bj(x.time())
		if not D.wbi_key or abs(D.wbi_key[CJ])<30:D.get_wbiKey(E)
		C[CJ]=E;C=A3(sorted(C.items()));C={C:B.join(filter(lambda chr:chr not in"!'()*",A(D)))for(C,D)in C.items()};F=CN(C);return F+'&w_rid='+hashlib.md5((F+D.wbi_key[S]).encode(encoding=Au)).hexdigest()
	def _get_sth(A,url,_type=g):
		D=_type;B=url
		if D==AS and A.session_vip.cookies:C=A.session_vip.get(B,headers=A.header)
		elif D==P:
			if not A.session_fake.cookies:A.getFakeCookie_event.wait()
			C=A.session_fake.get(B,headers=A.header)
		else:C=A.session_master.get(B,headers=A.header)
		return C
	def _post_sth(A,url,data):return A.session_master.post(url,headers=A.header,data=data)
	def post_live_history(B,room_id):C={Cm:A(room_id),'platform':'pc',CI:A(B.csrf)};D='https://api.live.bilibili.com/xlive/web-room/v1/index/roomEntryAction';B._post_sth(url=D,data=C)
	def do_notplay(F,ids):
		C=ids;G=F.detailContent_args.get(a);H=F.detailContent_args.get(W);I=F.detailContent_args.get(B5);D={CI:A(F.csrf)};E=B
		if CK in C:F.detailContent_args[CK]=A(C[0]);return
		elif'follow'in C:
			if C4 in C:D.update({'fids':A(H),'tagids':A(C[0])});E='https://api.bilibili.com/x/relation/tags/addUsers'
			else:D.update({'fid':A(H),'act':A(C[0])});E='https://api.bilibili.com/x/relation/modify'
		elif'zhui'in C:D.update({AY:A(I)});E='https://api.bilibili.com/pgc/web/follow/'+A(C[0])
		elif B1 in C:D.update({a:A(G),B1:A(C[0])});E='https://api.bilibili.com/x/web-interface/archive/like'
		elif C0 in C:D.update({a:A(G),'multiply':A(C[0]),'select_like':T});E='https://api.bilibili.com/x/web-interface/coin/add'
		elif'fav'in C:D.update({'rid':A(G),r:A1});D[C[1]+'_media_ids']=A(C[0]);E='https://api.bilibili.com/x/v3/fav/resource/deal'
		elif'triple'in C:D.update({a:A(G)});E='https://api.bilibili.com/x/web-interface/archive/like/triple'
		elif'reply'in C:D.update({'oid':A(C[0]),'rpid':A(C[1]),r:T,'action':T});E='http://api.bilibili.com/x/v2/reply/action'
		F._post_sth(url=E,data=D)
	def get_cid(D,video):
		C=video;F='https://api.bilibili.com/x/web-interface/view?aid=%s'%A(C[a]);G=D._get_sth(F);H=I.loads(G.text);B=H[E];C[n]=B[n];C[d]=B[d]
		if Ba in B and C1 in B[Ba]:C[A0]=D.find_bangumi_id(B[Ba])
	cookie_dic_tmp={}
	def get_cookies(A,key):
		D='https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key='+key;F=A._get_sth(D,P);B=I.loads(F.text)
		if B[M]==0:
			C=B[E][Co]
			if not C:A.cookie_dic_tmp[key]=A3(A.session_fake.cookies);A.pool.submit(A.getFakeCookie)
			return C
		return'网络错误'
	def set_cookie(A,key,_type):
		D=_type;C=key;F=A.cookie_dic_tmp.get(C,B)
		if not F:
			G=A.get_cookies(C)
			if G:return
		E=A.userConfig.get(c,{});E[D]={A4:A.cookie_dic_tmp.get(C,{})};A.userConfig.update({c:E});A.getCookie(D);A.dump_config()
	def unset_cookie(A,_type):
		C=_type
		if C==AS:A.session_vip.cookies.clear()
		else:A.session_master.cookies=A.session_fake.cookies;A.userid=A.csrf=B
		if C in A.userConfig.get(c,{}):A.userConfig[c].pop(C);A.dump_config()
	def set_normal_default(B,id,type):B.userConfig[type]=A(id);B.dump_config()
	def set_normal_cateManual(B,name,_List,action):
		H=action;F=name;E=_List;G=B.userConfig.get(A(E)+AE)
		if not G:G=B.userConfig[A(E)+AE]=[]
		if H=='save':
			for I in B.defaultConfig[E]:
				if not I in G.copy():B.userConfig[A(E)+AE].append(I)
			B.userConfig[E]=B.userConfig[A(E)+AE].copy();B.userConfig.pop(E+AE);B.dump_config()
		elif H=='clear':B.userConfig[E]=B.defaultConfig[E].copy();B.userConfig.pop(A(E)+AE);B.dump_config()
		else:
			if E==z:
				F=F.split(Ap)
				if V(F)==3:F[1]+=K+A(F[2])
				F={D:F[0],C:A(F[1])}
			if F in G:B.userConfig[A(E)+AE].remove(F)
			else:B.userConfig[A(E)+AE].append(F)
	def add_cateManualLiveExtra(A,action,name,id):
		F='cateManualLive_tmp';G=A.userConfig.get(A5,[])
		if not G:G=A.userConfig[A5]=[]
		if action=='clear':
			for E in G:
				E[C]=E[C].replace(Ap,K)
				if E in A.userConfig.get(z,[]):A.userConfig[z].remove(E)
				if E in A.userConfig.get(F,[]):A.userConfig[F].remove(E)
			A.userConfig.pop(A5)
		elif id in s(f(lambda x:x[C],A.userConfig.get(A5,[]))):
			B={D:name,C:id};A.userConfig[A5].remove(B);B[C]=id.replace(Ap,K)
			if B in A.userConfig.get(z,[]):A.userConfig[z].remove(B)
			if B in A.userConfig.get(F,[]):A.userConfig[F].remove(B)
		else:B={D:name,C:id};A.userConfig[A5].append(B)
		A.dump_config()
	def _checkUpdate(A,action):
		E={A9:A.header[A9]}
		if F(action):
			D=A.userConfig.get(AP)
			if D and D[CF]!=A.userConfig[Bk]:
				A.userConfig[AP][Bc]='正在更新';B=D[o];C=CM(url=B,headers=E,timeout=(3,5))
				if C.status_code==200:
					H=B.split(AA)
					with BA(f"{AQ}/{H[-1]}",'w',encoding=Au)as J:J.write(C.text)
					A.userConfig[AP][Bc]='更新完成'
				else:A.userConfig[AP][Bc]='更新失败'
		else:
			B='http://jm92swf.s1002.xrea.com/index.php/update.json';C=A.fetch(B,headers=E);G=I.loads(C.text);K=G.get(CF)
			if K:A.userConfig[AP]=G
	vod_qn_id={'127':'8K','126':'杜比视界','125':'HDR','120':'4K','116':'1080P60帧','112':'1080P+','80':'1080P','64':'720P'};vod_codec_id={'7':'avc','12':'hevc','13':'av1'};vod_audio_id={'30280':D2,'30232':'132000','30216':'64000'}
	def get_dash_media(I,video):
		H='SegmentBase';B=video;C=A(B.get(m));D=B.get(D3);J=B.get('codecs');L=B.get('bandwidth');M=B.get('startWithSap');E=B.get(D4);N=B.get('baseUrl').replace('&','&amp;');O=B[H].get('indexRange');P=B[H].get('Initialization');F=E.split(AA)[0]
		if F==AB:Q=B.get('frameRate');R=B.get('sar');S=B.get('width');T=B.get('height');G=f"height='{T}' width='{S}' frameRate='{Q}' sar='{R}'"
		elif F==Bf:U=I.vod_audio_id.get(C,D2);G=f"numChannels='2' sampleRate='{U}'"
		if D:C+=K+A(D)
		V=f'''
      <Representation id="{C}" bandwidth="{L}" codecs="{J}" mimeType="{E}" {G} startWithSAP="{M}">
        <BaseURL>{N}</BaseURL>
        <SegmentBase indexRange="{O}">
          <Initialization range="{P}"/>
        </SegmentBase>
      </Representation>''';return V
	def get_dash_media_list(I,media_lis):
		D=media_lis
		if not D:return B
		E=D[0][D4].split(AA)[0];C=N=B
		if E==AB:
			C=J=I.detailContent_args.get(CK,B)
			if J:J=F(J)
			else:C=A(I.userConfig[Aq]);J=120
			N=A(I.userConfig[Bn])
		elif E==Bf:C=A(I.userConfig[Ar]);J=F(C);N=L
		G=s(f(lambda x:A(x[m])+K+A(x[D3]),D));H=[]
		if C+K+N in G:H.append(D[G.index(C+K+N)])
		if not H and E==AB:
			for Q in I.vod_codec_id.keys():
				if C+K+A(Q)in G:H.append(D[G.index(C+K+A(Q))])
		if not H:
			M=B
			for P in G:
				O=P.split(K)
				if M and F(M)>F(O[0]):break
				elif E==AB and F(O[0])<=J and not M or E==Bf and not M or F(O[0])==M:
					M=F(O[0])
					if E==AB and A(O[1])==N:H=[D[G.index(A(P))]];break
					H.append(D[G.index(A(P))])
		R=f'\n    <AdaptationSet>\n      <ContentComponent contentType="{E}"/>{B.join(f(I.get_dash_media,H))}\n    </AdaptationSet>';return R
	get_dash_event=j.Event()
	def get_dash(A,ja):
		B=ja.get(d);C=ja.get('minBufferTime');D=A.pool.submit(A.get_dash_media_list,ja.get(AB));E=A.pool.submit(A.get_dash_media_list,ja.get(Bf));F=f'<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:dash:schema:mpd:2011" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd" type="static" mediaPresentationDuration="PT{B}S" minBufferTime="PT{C}S" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011">\n  <Period duration="PT{B}S" start="PT0S">{D.result()}{E.result()}\n  </Period>\n</MPD>'
		with BA(f"{AQ}/playurl.mpd",'w',encoding=Au)as G:G.write(F)
		A.get_dash_event.set();x.sleep(3);os.remove(f"{AQ}/playurl.mpd")
	def get_durl(I,ja):
		H='size';C=-1;A=-1
		for D in range(V(ja)):
			E=ja[D]
			if C<F(E[H]):C=F(E[H]);A=D
		G=B
		if V(ja)>0:
			if A==-1:A=0
			G=ja[A][o]
		return G
	def playerContent(C,flag,id,vipFlags):
		S='https://api.bilibili.com/x/v1/dm/list.so?oid=';C.stop_heartbeat_event.set();D={D5:B,o:B};F=id.split(K)
		if'web'in id or D6==F[0]:return C.live_playerContent(flag,id,vipFlags)
		if V(F)<2:return D
		H=F[0];G=F[1]
		if Cr in F:
			if'liveFilter'in id:id=F[2];C.add_cateManualLiveExtra(H,G,id)
			elif G==CE:C._checkUpdate(H)
			elif G in[At,z,BD,BE]:U=F[2];C.set_normal_cateManual(H,G,U)
			elif'login'in id:C.set_cookie(H,G)
			elif'logout'in id:C.unset_cookie(H)
			else:C.set_normal_default(H,G)
			return D
		elif'notplay'in F:C.pool.submit(C.do_notplay,F);return D
		elif G==n:
			N={a:A(H)};C.get_cid(N);G=N[n];F.append(CH+A(N[d]));P=N.get(A0)
			if P:id+=K+P;F.append(P)
		W=C.encrypt_wbi(avid=H,cid=G,fnval=4048,fnver=0,fourk=1)
		O=f"https://api.bilibili.com/x/player/wbi/playurl?{W}"
		dan = f'https://api.bilibili.com/x/v1/dm/list.so?oid={G}'
		if A0 in id:
			if An in id:X=s(A for A in f(lambda x:x if A0 in x else AU,F)if A is not AU);O='https://www.bilibili.com/bangumi/play/'+X[0];D[o]=O;D['flag']='bilibili';D[An]=T;D['jx']=T;D[CL]=A({A9:C.header[A9]});D[Al]=S+A(G)
			D['danmaku'] = dan
			return D
			O='https://api.bilibili.com/pgc/player/web/playurl?aid={}&cid={}&fnval=4048&fnver=0&fourk=1'.format(H,G)
		Y=C._get_sth(O,AS);J=I.loads(Y.text)
		if J[M]==0:
			if E in J:Q=J[E]
			elif AM in J:Q=J[AM]
			else:
				D['danmaku'] = dan
				return D
		else:
			D['danmaku'] = dan
			return D
		R=Q.get('dash')
		if R:C.get_dash_event.clear();Z=C.pool.submit(C.get_dash,R);C.get_dash_event.wait();D[o]=f"{AQ}/playurl.mpd"
		else:D[o]=C.get_durl(Q.get('durl',{}))
		D[An]=L;D[B9]=B;D[CL]=C.header;D[Al]=S+A(G);C.pool.submit(C.start_heartbeat,H,G,F)
		D['danmaku'] = dan
		return D
	def live_playerContent(G,flag,id,vipFlags):
		U='video/x-flv';T='url_info';C={D5:B,o:B};D=id.split(K)
		dan = f'https://api.bilibili.com/x/v1/dm/list.so?oid={D[1]}'
		if V(D)<2:
			C['danmaku'] = dan
			return C
		if G.userid and F(G.userConfig[BC])>0:G.pool.submit(G.post_live_history,D[-1])
		if D[0]==D6:
			W=F(D[1]);format=F(D[2]);H=F(D[3]);X=F(D[-1]);O='https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id={0}&protocol=0,1&format={1}&codec={2}&qn={3}&ptype=8&platform=web&dolby=5&panorama=1&no_playurl=0&mask=1'.format(X,format,H,W);Q=G._get_sth(O,P);J=I.loads(Q.text)
			if J[M]==0:
				try:N=J[E][Cz].get(CG);H=N[C_][0][Be][0][Bd][0]
				except:
					C['danmaku'] = dan
					return C
				Y=A(H['base_url']);Z=A(H[T][0]['host']);a=A(H[T][0]['extra']);N=Z+Y+a;C[o]=N
				if'.flv'in N:C[B9]=U
				else:C[B9]=B
			else:
				C['danmaku'] = dan
				return C
		else:
			O='https://api.live.bilibili.com/room/v1/Room/playUrl?cid=%s&%s'%(D[1],D[0])
			try:Q=G._get_sth(O)
			except:
				C['danmaku'] = dan
				return C
			R=I.loads(Q.text)
			if R[M]==0:
				J=R[E];S=J['durl']
				if V(S)>0:C[o]=S[0][o]
				if'h5'in D[0]:C[B9]=B
				else:C[B9]=U
			else:
				C['danmaku'] = dan
				return C
		C[An]=L;C[CL]={D7:'https://live.bilibili.com',A9:G.header[A9]}
		C['danmaku'] = dan
		return C
	config={'player':{},Z:{BF:[{S:C6,J:'分类',G:[{D:B2,C:B2},{D:BU,C:BU},{D:C2,C:C2},{D:B3,C:B3},{D:C3,C:C3},{D:'我的粉丝',C:'我的粉丝'}]}],AI:[{S:b,J:'别人投稿排序',G:[{D:'最新发布',C:Ai},{D:'最多播放',C:'click'},{D:'最多收藏',C:'stow'},{D:'最早发布',C:Ce}]}],Ad:[{S:A2,J:'分类',G:[{D:'番剧',C:T},{D:'国创',C:AV},{D:'电影',C:A1},{D:'电视剧',C:'5'},{D:'纪录片',C:AR},{D:'综艺',C:'7'}]},{S:b,J:'排序',G:[{D:y,C:y},{D:'播放数量',C:A1},{D:'更新时间',C:L},{D:'最高评分',C:AV},{D:'弹幕数量',C:T},{D:'追看人数',C:AR},{D:'开播时间',C:'5'},{D:'上映时间',C:'6'}]},{S:C5,J:'付费',G:[{D:'全部',C:'-1'},{D:'免费',C:T},{D:'付费',C:'2%2C6'},{D:'大会员',C:'4%2C6'}]}],Ae:[{S:b,J:'排序',G:[{D:'近期热门',C:'hot'},{D:'月播放量',C:Az},{D:'最新投稿',C:'new'},{D:'频道精选',C:Cl}]}],Af:[{S:b,J:'排序',G:[{D:'收藏时间',C:'mtime'},{D:'播放量',C:Az},{D:'投稿时间',C:'pubtime'}]}],BG:[{S:r,J:'分类',G:[{D:'全部',C:BW},{D:'视频',C:BN},{D:AH,C:AW},{D:BM,C:BM},{D:BT,C:BT}]}],BH:[{S:r,J:'类型',G:[{D:'视频',C:AB},{D:'番剧',C:D0},{D:Ad,C:D1},{D:AH,C:AW},{D:'用户',C:C7}]},{S:b,J:'视频排序',G:[{D:'综合排序',C:Cn},{D:'最多点击',C:'click'},{D:'最新发布',C:Ai},{D:'最多收藏',C:'stow'},{D:'最多弹幕',C:'dm'}]},{S:d,J:'视频时长',G:[{D:'全部',C:L},{D:'60分钟以上',C:AV},{D:'30~60分钟',C:AR},{D:'5~30分钟',C:A1},{D:'5分钟以下',C:T}]}]}};header={'Origin':Bu,D7:Bu,A9:'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
	def localProxy(A,param):return[200,'video/MP2T',action,B]