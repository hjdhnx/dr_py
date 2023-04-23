js:
let purl = input.split('|')[0];
let referer = input.split('|')[1];
let zm = input.split('|')[2];
print('purl:'+purl);
print('referer:'+referer);
print('zm:'+zm);
let myua = 'okhttp/3.15';
if(/ddrkey/.test(purl)){
   let ret=request(purl,{
        Referer: referer,
        withHeaders:true,
       'User-Agent':myua
   });
   log(ret);
   input = purl;
}else {
    let html = request(purl, {
        headers: {
            Referer: referer,
            'User-Agent':myua
        }
    });
    print(html);
    try {
        input = JSON.parse(html).url||{};
    }catch (e) {
        input = purl
    }
}