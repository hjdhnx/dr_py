js:
let d = [];
// let douban_api_host = 'https://frodo.douban.com/api/v2';
let douban_api_host = 'http://api.douban.com/api/v2';
let miniapp_apikey = '0ac44ae016490db2204ce0a042db2916';
// let miniapp_apikey = '054022eaeae0b00e0fc068c0c0a2102a';
const count = 30;

function miniapp_request(path, query){
    try {
        let url = douban_api_host + path;
        query.apikey = miniapp_apikey;
        fetch_params.headers = oheaders;
        url = buildUrl(url,query);
        let html = fetch(url,fetch_params);
        return JSON.parse(html);
    }
    catch(e){
    print('发生了错误:'+e.message);
    return {}
    }
}

function subject_real_time_hotest(){
    try{
        let res = miniapp_request("/subject_collection/subject_real_time_hotest/items", {});
        let lists = [];
        let arr = res.subject_collection_items||[];
        arr.forEach(function (item){
            if(item.type==='movie'||item.type==='tv'){
                let rating = item.rating?item.rating.value:"暂无评分";
                let honnor = (item.honor_infos||[]).map(function (it){return it.title}).join('|');
                lists.append({
                    "vod_id": "msearch:"+TYPE,
                    // "vod_id": TYPE+"$1",
                    "vod_name": item.title||"",
                    "vod_pic": item.pic.normal,
                    "vod_remarks": rating + " " + honnor
                })
            }
        });
        return lists
    }catch (e) {
        print('发生了错误:'+e.message);
        return []
    }
}
VODS = subject_real_time_hotest();
print(VODS);