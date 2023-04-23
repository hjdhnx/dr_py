js:
let d = [];
MY_FL.type = MY_CATE;
let fl = stringify(MY_FL);
fl = encodeUrl(fl);
input = input.split('{')[0]+fl;
if(MY_PAGE>1){
    let old_session = getItem('yk_session_'+MY_CATE,'{}');
    // print('本地访问session:'+old_session);
    if(MY_PAGE===2){
        input = input.replace('optionRefresh=1','session='+encodeUrl(old_session));
    }else{
        // input = input.replace(/session=.*?&/,'session='+encodeUrl(old_session)+'&');
        input = input.replace('optionRefresh=1','session='+encodeUrl(old_session));
    }
}
let html = fetch(input,fetch_params);
// print(html);
try {
    html = JSON.parse(html);
    let lists = html.data.filterData.listData;
    let session = html.data.filterData.session;
    session = stringify(session);
    // print(session);
    if(session!==getItem('yk_session_'+MY_CATE,'{}')){
         setItem('yk_session_'+MY_CATE,session);
    }
    lists.forEach(function (it){
         let vid;
        if (it.videoLink.includes('id_')) {
            vid = it.videoLink.split("id_")[1].split('.html')[0];
            // vid = it.videoLink.split("id_")[1].replace('.html','');
        } else {
            vid = 'msearch:'
        }

        d.push({
            title:it.title,
            img:it.img,
            desc:it.summary,
            url:'https://search.youku.com/api/search?appScene=show_episode&showIds='+vid,
            content:it.subTitle
        });
    });
}catch (e) {
    log('一级列表解析发生错误:'+e.message);
}
// print(d);
setResult(d)