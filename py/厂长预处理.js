rule_fetch_params.headers.Cookie = '68148872828e9f4d64e7a296f6c6b6d7=5429da9a54375db451f7f9e4f16ce0ea';
let new_host = 'https://czspp.com';
let new_html = request(new_host);
if(/正在进行人机识别/.test(new_html)){
let new_src = pd(new_html,'script&&src',new_host);
log(new_src);
let hhtml = request(new_src,{withHeaders:true});
let json = JSON.parse(hhtml);
let html = json.body;
let key = html.match(new RegExp('var key=\"(.*?)\"'))[1];
let avalue = html.match(new RegExp('value=\"(.*?)\"'))[1];
// log(html.indexOf('var key='));
// log(key);
// log(avalue);
let c = ''
for(let i=0;i<avalue.length;i++){
    let a = avalue[i];
    let b = a.charCodeAt();
    c += b;
}
let value = md5(c);
log(value);
let yz_url = 'https://czspp.com/a20be899_96a6_40b2_88ba_32f1f75f1552_yanzheng_ip.php?type=96c4e20a0e951f471d32dae103e83881&key='+key+'&value='+value;
log(yz_url);
hhtml = request(yz_url,{withHeaders:true});
json = JSON.parse(hhtml);
let setCk = Object.keys(json).find(it=>it.toLowerCase()==='set-cookie');
let cookie = setCk?json[setCk].split(';')[0]:'';
// let cookie = setCk?json[setCk]:'';
log('cookie:'+cookie);
rule_fetch_params.headers.Cookie = cookie;
setItem(RULE_CK,cookie);
}