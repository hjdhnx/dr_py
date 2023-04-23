js:
// cacheUrl = d.getParse(input);
cacheUrl = getParse(input);
// print(cacheUrl);
if(cacheUrl){
    input=cacheUrl;
}else{
    try {
        // let html = fetch([input, {headers:d.headers,timeout:d.timeout,encoding:d.encoding}]);
        // let html = fetch(input, {headers:d.headers,timeout:d.timeout,encoding:d.encoding});
        let html = fetch(input, fetch_params);
        // js = pdfh(html,'.stui-player__video script:eq(0)&&Html');
        // print(js);
        let ret = html.match(/var player_(.*?)=(.*?)</)[2];
        let url = JSON.parse(ret).url;
        if(url.length > 10){
            real_url = 'https://player.buyaotou.xyz/?url='+url;
            // log('免嗅地址:'+real_url);
            // d.saveParse(input,real_url);
            saveParse(input,real_url);
            input =  real_url;
        }
    }catch (e) {
        print('网络请求发生错误:'+e.message);
    }
}