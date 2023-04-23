js:
// fetch_params.withHeaders = 1;
// let data=fetch(input,fetch_params);
// let html = data.body;
print(input);
fetch_params.headers['User-Agent'] = MOBILE_UA;
print(fetch_params);
let html=request(input);
// let rurl = html.match(/window\.open\('(.*?)',/)[1].split('?')[0];
let rurl = html.match(/window\.open\('(.*?)',/)[1];
// print(rurl);
rurl = urlDeal(rurl);
// print(rurl);
// input = rurl;
input = {parse:1,jx:1,url:rurl};
// print(html);
