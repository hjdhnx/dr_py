var rule = {
    title: "88看球",
    // host:'http://www.88kanqiu.cc',
    host: "http://www.88kanqiu.live",
    url: "/match/fyclass/live",
    searchUrl: "",
    searchable: 0,
    quickSearch: 0,
    class_parse: ".nav-pills li;a&&Text;a&&href;/match/(\\d+)/live",
    headers: {
        "User-Agent": "PC_UA",
    },
    timeout: 5000,
    play_parse: true,
    lazy: "",
    limit: 6,
    double: false,
    推荐: "*",
    一级: ".list-group .group-game-item;.d-none&&Text;img&&src;.btn&&Text;a&&href",
    二级: {
        title: ".game-info-container&&Text;.customer-navbar-nav li&&Text",
        img: "img&&src",
        desc: ";;;div.team-name:eq(0)&&Text;div.team-name:eq(1)&&Text",
        content: "div.game-time&&Text",
        tabs: "js:TABS=['道长在线']",
        lists: `js:
            LISTS=[];
            let html = request(input);
            let pdata = jsp.pdfh(html, "#t&&value");
            pdata = pdata.substring(6, pdata.length);
            pdata = pdata.substring(0, (pdata.length) - 2)
            pdata = base64Decode(pdata);
            let jo = JSON.parse(pdata).links;
            let d = jo.map(function(it){
                return it.name + '$' + urlencode(it.url)
            });
            LISTS.push(d)
        `,
    },
    搜索: "",
};