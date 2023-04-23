import requests
import ujson
import time
import re
import execjs
from urllib.parse import quote

class tencent:
    def __init__(self, url, timeout=None,cookie=''):
        self.url = url
        self.timeout = timeout or 2
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬",
            "cookie":cookie,
        }
        self.int_time = int(time.time())
        self.cookie = cookie
        self.cookie_dict = {}
        self.parse_cookie()

    def parse_cookie(self):
        if self.cookie:
            for i in self.cookie.rstrip(';').split(";"):
                kv = i.split("=")
                print(kv)
                self.cookie_dict[kv[0].strip()] = kv[1]
        print(self.cookie_dict)

    def get_vid(self):
        vipUrl = self.url
        vid = None
        if vipUrl.find('v.qq.com/x/cover/') > -1:
            _type = vipUrl.split("v.qq.com/x/cover/")[1].split(".html")[0]
            if _type.find('/') > -1:
                vid = _type.split("/")[1]
            else:
                r = requests.get(vipUrl, headers=self.headers)
                html = r.text
                vid = html.split('<link rel="canonical" href="https://v.qq.com/x/cover/')[1].split('/')[1].split('.')[0]
        else:
            if re.search('/page/.*\.html',vipUrl):
                vid = vipUrl.split("/page/")[1].split(".html")[0]
            else:
                if vipUrl.find('&vid=') > -1:
                    vid = vipUrl.split("&vid=")[1].split("&")[0]

        print(f'vid:{vid}')
        return vid

    def get_adparams(self):
        pf = "in"
        ad_type = quote("LD|KB|PVL")
        pf_ex = "pc"
        url = quote(self.url)
        refer = quote("https://v.qq.com/")
        ty = "web"
        plugin = "1.0.0"
        v = "3.5.57"
        coverid = re.search("cover/(.*?).html", self.url).group(1)
        coverid = coverid.split('/')[0]
        # print(f'coverid:{coverid}')
        vid = self.get_vid()
        pt = ""
        flowid = "f48222928272c7950a794ffbea32022c_10901"
        vptag = quote("vptag=www_baidu_com|channel")
        pu = "1"
        chid = "0"
        adaptor = "2"
        dtype = "1"
        live = "0"
        resp_type = "json"
        guid = "2634e72faf052aa51f98971b2a68718c"
        req_type = 1
        # from = "0"
        appversion = "1.0.157"
        uid = self.cookie_dict['vqq_vuserid']
        tkn = self.cookie_dict['vqq_vusession']
        lt = "qq"
        platform = "10901"
        opid = self.cookie_dict['vqq_openid']
        atkn = self.cookie_dict['vqq_access_token']
        appid = self.cookie_dict['vqq_appid']
        tpid = "1"
        result = f"pf={pf}&ad_type={ad_type}&pf_ex={pf_ex}&url={url}&refer={refer}&ty={ty}&plugin={plugin}&v={v}&coverid={coverid}&vid={vid}&pt={pt}&flowid={flowid}&vptag={vptag}&pu={pu}&chid={chid}&adaptor={adaptor}&dtype={dtype}&live={live}&resp_type={resp_type}&guid={guid}&req_type={req_type}&from=0&appversion={appversion}&" \
                 f"uid={uid}&tkn={tkn}&lt={lt}&platform={platform}&opid={opid}&atkn={atkn}&appid={appid}&tpid={tpid}"
        return result

    def get_vinfoparams(self):
        spsrt = "1"
        charge = "1"
        defaultfmt = "auto"
        otype = "ojson"
        guid = "2634e72faf052aa51f98971b2a68718c"
        # 随机数 + platform
        flowid = "f48222928272c7950a794ffbea32022c_10901"
        platform = "10901"
        sdtfrom = "v1010"
        defnpayver = "1"
        appVer = "3.5.57"
        host = "v.qq.com"
        ehost = quote(self.url)
        refer = "v.qq.com"
        sphttps = "1"
        tm = self.int_time
        spwm = "4"
        logintoken = quote(str({"main_login": self.cookie_dict['main_login'], "openid": self.cookie_dict['vqq_openid'],
                                "appid": self.cookie_dict['vqq_appid'],
                                "access_token": self.cookie_dict['vqq_access_token'],
                                "vuserid": self.cookie_dict['vqq_vuserid'],
                                "vusession": self.cookie_dict['vqq_vusession']}))
        # print(f'logintoken:{logintoken}')
        vid = self.get_vid()
        defn = "fhd"
        fhdswitch = "0"
        show1080p = "1"
        isHLS = "1"
        dtype = "3"
        sphls = "2"
        spgzip = "1"
        dlver = "2"
        drm = "32"
        hdcp = "1"
        spau = "1"
        spaudio = "15"
        defsrc = "1"
        encryptVer = "9.1"
        cKey = self.get_cKey(platform, appVer, vid, guid, tm)
        fp2p = "1"
        spadseg = "3"
        result = f"spsrt={spsrt}&charge={charge}&defaultfmt={defaultfmt}&otype={otype}&guid={guid}&flowid={flowid}&platform={platform}&sdtfrom={sdtfrom}&defnpayver={defnpayver}&appVer={appVer}&host={host}&ehost={ehost}&refer={refer}&sphttps={sphttps}&tm={tm}&spwm={spwm}&logintoken={logintoken}&vid={vid}&defn={defn}&fhdswitch={fhdswitch}&show1080p={show1080p}&isHLS={isHLS}&dtype={dtype}&sphls={sphls}&spgzip={spgzip}&dlver={dlver}&drm={drm}&hdcp={hdcp}&spau={spau}&spaudio={spaudio}&defsrc={defsrc}&encryptVer={encryptVer}&cKey={cKey}&fp2p={fp2p}&spadseg={spadseg}"
        return result

    def get_cKey(self, platform, version, vid, guid, tm):
        file = './js/getck.js'
        ctx = execjs.compile(open(file).read())
        params = ctx.call("getckey", platform, version, vid, '', guid,
                          tm)
        return params

    def get_buid(self):
        return "vinfoad"

    def deal_data(self,data):
        # print(data)
        vinfo = ujson.loads(data['vinfo'])
        vl = vinfo['vl']
        urls = vl['vi'][0]['ul']['ui']
        # print(urls)
        try:
            pt = urls[-1]['hls']['pt']
        except:
            pt = ''
        url = urls[-1]['url']
        realUrl = url + pt
        print(realUrl)
        return realUrl

    def start(self):
        ad_params = self.get_adparams()
        vinfoparams = self.get_vinfoparams()
        buid = self.get_buid()
        params = {"buid": buid,
                  "adparam": ad_params,
                  "vinfoparam": vinfoparams}
        # print(params)
        res = requests.post("https://vd.l.qq.com/proxyhttp", headers=self.headers, json=params)
        data = res.json()
        return self.deal_data(data)


if __name__ == '__main__':
    # 控制台执行 document.cookie 获取
    cookie = """
    pgv_pvid=5805499462; iip=0; RK=yQaYRyNLbG; ptcz=2a0d041daba2e1e3872184cd999e01bf90678c0e492c5900527c802251d224ad; tvfe_boss_uuid=53b5e88a3ebeba2c; ts_uid=8123938908; tvfe_search_uid=225c6955-d257-4d4a-97d0-cc327ffea211; txv_boss_uuid=95755769-e482-3a22-3e9f-6f8d842da1a7; pgv_pvi=1381712896; logTrackKey=613d40c3fea04aafb45fc9642dd67b99; video_platform=2; main_login=qq; vqq_vuserid=1260982452; vqq_openid=406CA2296D6A3B970597D6CF1605B6B7; vqq_appid=101483052; qq_nick=feng; pgv_info=ssid=s1368217315; pac_uid=1_434857005; vversion_name=8.2.95; video_guid=3419ca23530808d22bb278e881e46647; video_omgid=3419ca23530808d22bb278e881e46647; _qpsvr_localtk=0.710205836458567; compared_guid=bc772040638cf0da; vqq_access_token=88AEE1A8BC32318537BC7D81586E44A4; o_cookie=434857005; qv_als=vzJJwNyUEiCeDF1UA11662524934RoBNzA==; video_bucketid=4; fqm_pvqid=0a2a19f9-b09d-48d2-835a-cee916bdb63f; fqm_sessionid=a2c625f7-98e9-4d69-adb4-ad82846832bc; uin=o0434857005; skey=@rZMv3mYSR; tab_experiment_str=8752038#9047927#8752037#9040406#9099387; bucket_id=9231009; last_refresh_time=1666604352564; last_refresh_vuserid=1260982452; ts_refer=m.v.qq.com/; qq_head=http://thirdqq.qlogo.cn/g?b=sdk&k=llMfAicCbslpBk4funDukzg&s=100&t=318; vqq_vusession=sj85gfjn1ZL5jGI_RW5lLA.N; ptag=m_v_qq_com|channel; tab_experiment_data=exp_id=9099387&status=1; ts_last=v.qq.com/x/cover/m441e3rjq9kwpsc.html
    """.strip()
    login_token = """
    vqq_appid=101483052; vqq_openid=406CA2296D6A3B970597D6CF1605B6B7; vqq_vuserid=1260982452;vqq_vusession=Xd5bba2m9ByWls30Vi2FSQ.N; vqq_refresh_token=2D85975A29FB056EB6F9A338CB8F1EF5;vqq_next_refresh_time=6530;vqq_access_token=88AEE1A8BC32318537BC7D81586E44A4;main_login=qq;
    """.strip()
    auth_token = """
    vqq_appid=101483052; vqq_openid=406CA2296D6A3B970597D6CF1605B6B7; vqq_vuserid=1260982452;vqq_vusession=
    """.strip()
    cookie = login_token
    print(cookie)

    # refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=1698594290&g_vstk=270754686&g_actk=2412125&callback=jQuery191028559957521840595_1666665357793&_=1666665357794'
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    #     "Referer":"https://v.qq.com/",
    #     # "cookie":cookie,
    #     "cookie":auth_token,
    # }
    # r = requests.get(refresh_url,headers=headers)
    # print(r.text)
    # 斗罗大陆
    url = 'https://v.qq.com/x/cover/m441e3rjq9kwpsc/c00442r6ry6.html'
    # 复仇者联盟
    # url = 'https://v.qq.com/x/cover/v2098lbuihuqs11/m00314jtw6k.html'
    vqq = tencent(url=url,cookie=cookie)
    vqq.start()