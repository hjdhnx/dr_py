js:
log(input);
let d = [];
// log(MY_FL);
// log(MY_PAGE);
let body = {
  "mform": MY_CATE,
  "mcountry": MY_FL.mcountry||'all',
  "tag_arr%5B%5D": MY_FL.mtag||'all',
  // "tag_arr[]": MY_FL.mtag||'all',
  "page": MY_PAGE,
  "sort": MY_FL.sort||'updatetime',
  "album": MY_FL.album||'all',
  "title": '',
};
// let forms=[];
// Object.keys(body).forEach(function (it){
//   forms.push(it+'='+body[it]);
// });
// let form = forms.join('&');
// log(body);
// log(form);
// fetch_params.body = form;

fetch_params.body = body;
fetch_params.headers['x-requested-with'] = 'XMLHttpRequest';
// fetch_params.headers['cookie'] = 'PHPSESSID=e7ht5hvema4sg0o8l1o5k0bqt1; Hm_lvt_eebb854b7348edadfb6b433786f5d059=1666239708; Hm_lpvt_eebb854b7348edadfb6b433786f5d059=1666244071';
let url = input.split('?')[0];
let html = post(url,fetch_params);
print(html);
let data = JSON.parse(html);
data.mlist.forEach(function (it){
  d.push({
    title: it.title,
    desc: it.definition+' '+it.grade,
    url:it.id,
    img:it.cover_img,
  });
});
setResult(d);