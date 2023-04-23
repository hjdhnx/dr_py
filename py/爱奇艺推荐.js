js:
let d =[];
// print(input);
// print(HOST);
fetch_params.headers['user-agent'] = PC_UA;
// print(fetch_params);
pdfh = jsp.pdfh;
pdfa = jsp.pdfa;
pd = jsp.pd;
let html = fetch(HOST,fetch_params);
let lists = pdfa(html,'.qy-mod-li');
// print(lists.length);
lists.forEach(function (it){
    try {
        let title = pdfh(it,'p.sub&&title');
    let desc = pdfh(it,'.qy-mod-label&&Text');
    let pic_url = pd(it,'img&&src');
    d.push({
        title:title,
        desc:desc,
        img:pic_url,
    });
    }catch(e){
        // print(e.message);
    }

});
// print(d);
res = setResult(d);
// print(res);