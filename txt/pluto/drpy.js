import ch from './cheerio.min.js';
// import 'http://192.168.10.99:5705/txt/pluto/drT.js';
// import 'http://192.168.3.239:5705/txt/pluto/drT.js';
import 'http://gitcode.net/qq_32394351/dr_py/-/raw/master/txt/pluto/drT.js';
// import 模板 from 'https://ghproxy.net/https://raw.githubusercontent.com/hjdhnx/dr_py/main/js/模板.js'
// var rule = Object.assign(模板.首图2,{
// host: 'https://www.zbkk.net',
// });

const key = 'drpy_zbk';

function init_test(){
    console.log("init_test_start");
    // clearItem(RULE_CK);
    console.log(JSON.stringify(rule));
    // console.log(request('https://www.baidu.com',{withHeaders:true}));
    // console.log(request('https://www.baidu.com/favicon.ico',{toBase64:true}));
    // require('http://192.168.10.99:5705/txt/pluto/drT.js');
    // console.log(typeof(drT));
    // console.log(drT.renderText('{{fl.cate}},hi, {{fl}}哈哈.{{fl}}',{sort: 1,cate:'movie'},'fl'));
    console.log("init_test_end");
}

let rule = {
    title: '真不卡',
    host: 'https://www.zbkk.net',
    // url: '/vodshow/fyclass--------fypage---.html',
    url:'/vodshow/fyclass-fyfilter',
    filter_url:'{{fl.地区}}-{{fl.排序}}-{{fl.剧情}}-{{fl.语言}}-{{fl.字母}}---fypage---{{fl.年份}}.html',
    searchUrl:'/vodsearch/**----------fypage---.html',
    filter:{'1': [{'key': '剧情', 'name': '按剧情', 'value': [{'n': '全部', 'v': ''}, {'n': '喜剧', 'v': '%E5%96%9C%E5%89%A7'}, {'n': '爱情', 'v': '%E7%88%B1%E6%83%85'}, {'n': '恐怖', 'v': '%E6%81%90%E6%80%96'}, {'n': '动作', 'v': '%E5%8A%A8%E4%BD%9C'}, {'n': '科幻', 'v': '%E7%A7%91%E5%B9%BB'}, {'n': '剧情', 'v': '%E5%89%A7%E6%83%85'}, {'n': '战争', 'v': '%E6%88%98%E4%BA%89'}, {'n': '警匪', 'v': '%E8%AD%A6%E5%8C%AA'}, {'n': '犯罪', 'v': '%E7%8A%AF%E7%BD%AA'}, {'n': '动画', 'v': '%E5%8A%A8%E7%94%BB'}, {'n': '奇幻', 'v': '%E5%A5%87%E5%B9%BB'}, {'n': '武侠', 'v': '%E6%AD%A6%E4%BE%A0'}, {'n': '冒险', 'v': '%E5%86%92%E9%99%A9'}, {'n': '枪战', 'v': '%E6%9E%AA%E6%88%98'}, {'n': '恐怖', 'v': '%E6%81%90%E6%80%96'}, {'n': '悬疑', 'v': '%E6%82%AC%E7%96%91'}, {'n': '惊悚', 'v': '%E6%83%8A%E6%82%9A'}, {'n': '经典', 'v': '%E7%BB%8F%E5%85%B8'}, {'n': '青春', 'v': '%E9%9D%92%E6%98%A5'}, {'n': '文艺', 'v': '%E6%96%87%E8%89%BA'}, {'n': '微电影', 'v': '%E5%BE%AE%E7%94%B5%E5%BD%B1'}, {'n': '古装', 'v': '%E5%8F%A4%E8%A3%85'}, {'n': '历史', 'v': '%E5%8E%86%E5%8F%B2'}, {'n': '运动', 'v': '%E8%BF%90%E5%8A%A8'}, {'n': '农村', 'v': '%E5%86%9C%E6%9D%91'}, {'n': '儿童', 'v': '%E5%84%BF%E7%AB%A5'}, {'n': '网络电影', 'v': '%E7%BD%91%E7%BB%9C%E7%94%B5%E5%BD%B1'}]}, {'key': '地区', 'name': '按地区', 'value': [{'n': '全部', 'v': ''}, {'n': '大陆', 'v': '%E5%A4%A7%E9%99%86'}, {'n': '香港', 'v': '%E9%A6%99%E6%B8%AF'}, {'n': '台湾', 'v': '%E5%8F%B0%E6%B9%BE'}, {'n': '美国', 'v': '%E7%BE%8E%E5%9B%BD'}, {'n': '法国', 'v': '%E6%B3%95%E5%9B%BD'}, {'n': '英国', 'v': '%E8%8B%B1%E5%9B%BD'}, {'n': '日本', 'v': '%E6%97%A5%E6%9C%AC'}, {'n': '韩国', 'v': '%E9%9F%A9%E5%9B%BD'}, {'n': '德国', 'v': '%E5%BE%B7%E5%9B%BD'}, {'n': '泰国', 'v': '%E6%B3%B0%E5%9B%BD'}, {'n': '印度', 'v': '%E5%8D%B0%E5%BA%A6'}, {'n': '意大利', 'v': '%E6%84%8F%E5%A4%A7%E5%88%A9'}, {'n': '西班牙', 'v': '%E8%A5%BF%E7%8F%AD%E7%89%99'}, {'n': '加拿大', 'v': '%E5%8A%A0%E6%8B%BF%E5%A4%A7'}, {'n': '其他', 'v': '%E5%85%B6%E4%BB%96'}]}, {'key': '年份', 'name': '按年份', 'value': [{'n': '全部', 'v': ''}, {'n': '2022', 'v': '2022'}, {'n': '2021', 'v': '2021'}, {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'}, {'n': '2018', 'v': '2018'}, {'n': '2017', 'v': '2017'}, {'n': '2016', 'v': '2016'}, {'n': '2015', 'v': '2015'}, {'n': '2014', 'v': '2014'}, {'n': '2013', 'v': '2013'}, {'n': '2012', 'v': '2012'}, {'n': '2011', 'v': '2011'}, {'n': '2010', 'v': '2010'}]}, {'key': '语言', 'name': '按语言', 'value': [{'n': '全部', 'v': ''}, {'n': '国语', 'v': '%E5%9B%BD%E8%AF%AD'}, {'n': '英语', 'v': '%E8%8B%B1%E8%AF%AD'}, {'n': '粤语', 'v': '%E7%B2%A4%E8%AF%AD'}, {'n': '闽南语', 'v': '%E9%97%BD%E5%8D%97%E8%AF%AD'}, {'n': '韩语', 'v': '%E9%9F%A9%E8%AF%AD'}, {'n': '日语', 'v': '%E6%97%A5%E8%AF%AD'}, {'n': '法语', 'v': '%E6%B3%95%E8%AF%AD'}, {'n': '德语', 'v': '%E5%BE%B7%E8%AF%AD'}, {'n': '其它', 'v': '%E5%85%B6%E5%AE%83'}]}, {'key': '字母', 'name': '按字母', 'value': [{'n': '全部', 'v': ''}, {'n': 'A', 'v': 'A'}, {'n': 'B', 'v': 'B'}, {'n': 'C', 'v': 'C'}, {'n': 'D', 'v': 'D'}, {'n': 'E', 'v': 'E'}, {'n': 'F', 'v': 'F'}, {'n': 'G', 'v': 'G'}, {'n': 'H', 'v': 'H'}, {'n': 'I', 'v': 'I'}, {'n': 'J', 'v': 'J'}, {'n': 'K', 'v': 'K'}, {'n': 'L', 'v': 'L'}, {'n': 'M', 'v': 'M'}, {'n': 'N', 'v': 'N'}, {'n': 'O', 'v': 'O'}, {'n': 'P', 'v': 'P'}, {'n': 'Q', 'v': 'Q'}, {'n': 'R', 'v': 'R'}, {'n': 'S', 'v': 'S'}, {'n': 'T', 'v': 'T'}, {'n': 'U', 'v': 'U'}, {'n': 'V', 'v': 'V'}, {'n': 'W', 'v': 'W'}, {'n': 'X', 'v': 'X'}, {'n': 'Y', 'v': 'Y'}, {'n': 'Z', 'v': 'Z'}, {'n': '0-9', 'v': '09'}]}], '2': [{'key': '剧情', 'name': '按剧情', 'value': [{'n': '全部', 'v': ''}, {'n': '古装', 'v': '%E5%8F%A4%E8%A3%85'}, {'n': '战争', 'v': '%E6%88%98%E4%BA%89'}, {'n': '青春偶像', 'v': '%E9%9D%92%E6%98%A5%E5%81%B6%E5%83%8F'}, {'n': '喜剧', 'v': '%E5%96%9C%E5%89%A7'}, {'n': '家庭', 'v': '%E5%AE%B6%E5%BA%AD'}, {'n': '犯罪', 'v': '%E7%8A%AF%E7%BD%AA'}, {'n': '动作', 'v': '%E5%8A%A8%E4%BD%9C'}, {'n': '奇幻', 'v': '%E5%A5%87%E5%B9%BB'}, {'n': '剧情', 'v': '%E5%89%A7%E6%83%85'}, {'n': '历史', 'v': '%E5%8E%86%E5%8F%B2'}, {'n': '经典', 'v': '%E7%BB%8F%E5%85%B8'}, {'n': '乡村', 'v': '%E4%B9%A1%E6%9D%91'}, {'n': '情景', 'v': '%E6%83%85%E6%99%AF'}, {'n': '商战', 'v': '%E5%95%86%E6%88%98'}, {'n': '网剧', 'v': '%E7%BD%91%E5%89%A7'}, {'n': '其他', 'v': '%E5%85%B6%E4%BB%96'}]}, {'key': '地区', 'name': '按地区', 'value': [{'n': '全部', 'v': ''}, {'n': '内地', 'v': '%E5%86%85%E5%9C%B0'}, {'n': '韩国', 'v': '%E9%9F%A9%E5%9B%BD'}, {'n': '香港', 'v': '%E9%A6%99%E6%B8%AF'}, {'n': '台湾', 'v': '%E5%8F%B0%E6%B9%BE'}, {'n': '日本', 'v': '%E6%97%A5%E6%9C%AC'}, {'n': '美国', 'v': '%E7%BE%8E%E5%9B%BD'}, {'n': '泰国', 'v': '%E6%B3%B0%E5%9B%BD'}, {'n': '英国', 'v': '%E8%8B%B1%E5%9B%BD'}, {'n': '新加坡', 'v': '%E6%96%B0%E5%8A%A0%E5%9D%A1'}, {'n': '其他', 'v': '%E5%85%B6%E4%BB%96'}]}, {'key': '年份', 'name': '按年份', 'value': [{'n': '全部', 'v': ''}, {'n': '2022', 'v': '2022'}, {'n': '2021', 'v': '2021'}, {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'}, {'n': '2018', 'v': '2018'}, {'n': '2017', 'v': '2017'}, {'n': '2016', 'v': '2016'}, {'n': '2015', 'v': '2015'}, {'n': '2014', 'v': '2014'}, {'n': '2013', 'v': '2013'}, {'n': '2012', 'v': '2012'}, {'n': '2011', 'v': '2011'}, {'n': '2010', 'v': '2010'}]}, {'key': '语言', 'name': '按语言', 'value': [{'n': '全部', 'v': ''}, {'n': '国语', 'v': '%E5%9B%BD%E8%AF%AD'}, {'n': '英语', 'v': '%E8%8B%B1%E8%AF%AD'}, {'n': '粤语', 'v': '%E7%B2%A4%E8%AF%AD'}, {'n': '闽南语', 'v': '%E9%97%BD%E5%8D%97%E8%AF%AD'}, {'n': '韩语', 'v': '%E9%9F%A9%E8%AF%AD'}, {'n': '日语', 'v': '%E6%97%A5%E8%AF%AD'}, {'n': '其它', 'v': '%E5%85%B6%E5%AE%83'}]}, {'key': '字母', 'name': '按字母', 'value': [{'n': '全部', 'v': ''}, {'n': 'A', 'v': 'A'}, {'n': 'B', 'v': 'B'}, {'n': 'C', 'v': 'C'}, {'n': 'D', 'v': 'D'}, {'n': 'E', 'v': 'E'}, {'n': 'F', 'v': 'F'}, {'n': 'G', 'v': 'G'}, {'n': 'H', 'v': 'H'}, {'n': 'I', 'v': 'I'}, {'n': 'J', 'v': 'J'}, {'n': 'K', 'v': 'K'}, {'n': 'L', 'v': 'L'}, {'n': 'M', 'v': 'M'}, {'n': 'N', 'v': 'N'}, {'n': 'O', 'v': 'O'}, {'n': 'P', 'v': 'P'}, {'n': 'Q', 'v': 'Q'}, {'n': 'R', 'v': 'R'}, {'n': 'S', 'v': 'S'}, {'n': 'T', 'v': 'T'}, {'n': 'U', 'v': 'U'}, {'n': 'V', 'v': 'V'}, {'n': 'W', 'v': 'W'}, {'n': 'X', 'v': 'X'}, {'n': 'Y', 'v': 'Y'}, {'n': 'Z', 'v': 'Z'}, {'n': '0-9', 'v': '09'}]}], '3': [{'key': '剧情', 'name': '按剧情', 'value': [{'n': '全部', 'v': ''}, {'n': '选秀', 'v': '%E9%80%89%E7%A7%80'}, {'n': '情感', 'v': '%E6%83%85%E6%84%9F'}, {'n': '访谈', 'v': '%E8%AE%BF%E8%B0%88'}, {'n': '播报', 'v': '%E6%92%AD%E6%8A%A5'}, {'n': '旅游', 'v': '%E6%97%85%E6%B8%B8'}, {'n': '音乐', 'v': '%E9%9F%B3%E4%B9%90'}, {'n': '美食', 'v': '%E7%BE%8E%E9%A3%9F'}, {'n': '纪实', 'v': '%E7%BA%AA%E5%AE%9E'}, {'n': '曲艺', 'v': '%E6%9B%B2%E8%89%BA'}, {'n': '生活', 'v': '%E7%94%9F%E6%B4%BB'}, {'n': '游戏互动', 'v': '%E6%B8%B8%E6%88%8F%E4%BA%92%E5%8A%A8'}, {'n': '财经', 'v': '%E8%B4%A2%E7%BB%8F'}, {'n': '求职', 'v': '%E6%B1%82%E8%81%8C'}]}, {'key': '地区', 'name': '按地区', 'value': [{'n': '全部', 'v': ''}, {'n': '内地', 'v': '%E5%86%85%E5%9C%B0'}, {'n': '港台', 'v': '%E6%B8%AF%E5%8F%B0'}, {'n': '日韩', 'v': '%E6%97%A5%E9%9F%A9'}, {'n': '欧美', 'v': '%E6%AC%A7%E7%BE%8E'}]}, {'key': '年份', 'name': '按年份', 'value': [{'n': '全部', 'v': ''}, {'n': '2022', 'v': '2022'}, {'n': '2021', 'v': '2021'}, {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'}, {'n': '2018', 'v': '2018'}, {'n': '2017', 'v': '2017'}, {'n': '2016', 'v': '2016'}, {'n': '2015', 'v': '2015'}, {'n': '2014', 'v': '2014'}, {'n': '2013', 'v': '2013'}, {'n': '2012', 'v': '2012'}, {'n': '2011', 'v': '2011'}, {'n': '2010', 'v': '2010'}]}, {'key': '语言', 'name': '按语言', 'value': [{'n': '全部', 'v': ''}, {'n': '国语', 'v': '%E5%9B%BD%E8%AF%AD'}, {'n': '英语', 'v': '%E8%8B%B1%E8%AF%AD'}, {'n': '粤语', 'v': '%E7%B2%A4%E8%AF%AD'}, {'n': '闽南语', 'v': '%E9%97%BD%E5%8D%97%E8%AF%AD'}, {'n': '韩语', 'v': '%E9%9F%A9%E8%AF%AD'}, {'n': '日语', 'v': '%E6%97%A5%E8%AF%AD'}, {'n': '其它', 'v': '%E5%85%B6%E5%AE%83'}]}, {'key': '字母', 'name': '按字母', 'value': [{'n': '全部', 'v': ''}, {'n': 'A', 'v': 'A'}, {'n': 'B', 'v': 'B'}, {'n': 'C', 'v': 'C'}, {'n': 'D', 'v': 'D'}, {'n': 'E', 'v': 'E'}, {'n': 'F', 'v': 'F'}, {'n': 'G', 'v': 'G'}, {'n': 'H', 'v': 'H'}, {'n': 'I', 'v': 'I'}, {'n': 'J', 'v': 'J'}, {'n': 'K', 'v': 'K'}, {'n': 'L', 'v': 'L'}, {'n': 'M', 'v': 'M'}, {'n': 'N', 'v': 'N'}, {'n': 'O', 'v': 'O'}, {'n': 'P', 'v': 'P'}, {'n': 'Q', 'v': 'Q'}, {'n': 'R', 'v': 'R'}, {'n': 'S', 'v': 'S'}, {'n': 'T', 'v': 'T'}, {'n': 'U', 'v': 'U'}, {'n': 'V', 'v': 'V'}, {'n': 'W', 'v': 'W'}, {'n': 'X', 'v': 'X'}, {'n': 'Y', 'v': 'Y'}, {'n': 'Z', 'v': 'Z'}, {'n': '0-9', 'v': '09'}]}], '4': [{'key': '剧情', 'name': '按剧情', 'value': [{'n': '全部', 'v': ''}, {'n': '情感', 'v': '%E6%83%85%E6%84%9F'}, {'n': '科幻', 'v': '%E7%A7%91%E5%B9%BB'}, {'n': '热血', 'v': '%E7%83%AD%E8%A1%80'}, {'n': '推理', 'v': '%E6%8E%A8%E7%90%86'}, {'n': '搞笑', 'v': '%E6%90%9E%E7%AC%91'}, {'n': '冒险', 'v': '%E5%86%92%E9%99%A9'}, {'n': '萝莉', 'v': '%E8%90%9D%E8%8E%89'}, {'n': '校园', 'v': '%E6%A0%A1%E5%9B%AD'}, {'n': '动作', 'v': '%E5%8A%A8%E4%BD%9C'}, {'n': '机战', 'v': '%E6%9C%BA%E6%88%98'}, {'n': '运动', 'v': '%E8%BF%90%E5%8A%A8'}, {'n': '战争', 'v': '%E6%88%98%E4%BA%89'}, {'n': '少年', 'v': '%E5%B0%91%E5%B9%B4'}, {'n': '少女', 'v': '%E5%B0%91%E5%A5%B3'}, {'n': '社会', 'v': '%E7%A4%BE%E4%BC%9A'}, {'n': '原创', 'v': '%E5%8E%9F%E5%88%9B'}, {'n': '亲子', 'v': '%E4%BA%B2%E5%AD%90'}, {'n': '益智', 'v': '%E7%9B%8A%E6%99%BA'}, {'n': '励志', 'v': '%E5%8A%B1%E5%BF%97'}, {'n': '其他', 'v': '%E5%85%B6%E4%BB%96'}]}, {'key': '地区', 'name': '按地区', 'value': [{'n': '全部', 'v': ''}, {'n': '国产', 'v': '%E5%9B%BD%E4%BA%A7'}, {'n': '日本', 'v': '%E6%97%A5%E6%9C%AC'}, {'n': '欧美', 'v': '%E6%AC%A7%E7%BE%8E'}, {'n': '其他', 'v': '%E5%85%B6%E4%BB%96'}]}, {'key': '年份', 'name': '按年份', 'value': [{'n': '全部', 'v': ''}, {'n': '2022', 'v': '2022'}, {'n': '2021', 'v': '2021'}, {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'}, {'n': '2018', 'v': '2018'}, {'n': '2017', 'v': '2017'}, {'n': '2016', 'v': '2016'}, {'n': '2015', 'v': '2015'}, {'n': '2014', 'v': '2014'}, {'n': '2013', 'v': '2013'}, {'n': '2012', 'v': '2012'}, {'n': '2011', 'v': '2011'}, {'n': '2010', 'v': '2010'}]}, {'key': '语言', 'name': '按语言', 'value': [{'n': '全部', 'v': ''}, {'n': '国语', 'v': '%E5%9B%BD%E8%AF%AD'}, {'n': '英语', 'v': '%E8%8B%B1%E8%AF%AD'}, {'n': '粤语', 'v': '%E7%B2%A4%E8%AF%AD'}, {'n': '闽南语', 'v': '%E9%97%BD%E5%8D%97%E8%AF%AD'}, {'n': '韩语', 'v': '%E9%9F%A9%E8%AF%AD'}, {'n': '日语', 'v': '%E6%97%A5%E8%AF%AD'}, {'n': '其它', 'v': '%E5%85%B6%E5%AE%83'}]}, {'key': '字母', 'name': '按字母', 'value': [{'n': '全部', 'v': ''}, {'n': 'A', 'v': 'A'}, {'n': 'B', 'v': 'B'}, {'n': 'C', 'v': 'C'}, {'n': 'D', 'v': 'D'}, {'n': 'E', 'v': 'E'}, {'n': 'F', 'v': 'F'}, {'n': 'G', 'v': 'G'}, {'n': 'H', 'v': 'H'}, {'n': 'I', 'v': 'I'}, {'n': 'J', 'v': 'J'}, {'n': 'K', 'v': 'K'}, {'n': 'L', 'v': 'L'}, {'n': 'M', 'v': 'M'}, {'n': 'N', 'v': 'N'}, {'n': 'O', 'v': 'O'}, {'n': 'P', 'v': 'P'}, {'n': 'Q', 'v': 'Q'}, {'n': 'R', 'v': 'R'}, {'n': 'S', 'v': 'S'}, {'n': 'T', 'v': 'T'}, {'n': 'U', 'v': 'U'}, {'n': 'V', 'v': 'V'}, {'n': 'W', 'v': 'W'}, {'n': 'X', 'v': 'X'}, {'n': 'Y', 'v': 'Y'}, {'n': 'Z', 'v': 'Z'}, {'n': '0-9', 'v': '09'}]}]},
    // headers: {
    //     'User-Agent': MOBILE_UA
    // },
    // play_parse:true,
    // lazy:'',
    class_parse: 'body&&.stui-header__menu .dropdown li:gt(0):lt(5);a&&Text;a&&href;.*/(.*?).html',
    一级: '.stui-vodlist li;a&&title;a&&data-original;.pic-text&&Text;a&&href',
    推荐:'ul.stui-vodlist.clearfix;body&&li;a&&title;.lazyload&&data-original;.pic-text&&Text;a&&href',
    二级:{"title":".stui-content__detail .title&&Text;.stui-content__detail p:eq(-2)&&Text","img":".stui-content__thumb .lazyload&&data-original","desc":".stui-content__detail p:eq(0)&&Text;.stui-content__detail p:eq(1)&&Text;.stui-content__detail p:eq(2)&&Text","content":".detail&&Text","tabs":"body&&h3.title","lists":".stui-content__playlist,#id&&li"},
    double:true, // 推荐内容是否双层定位
    //搜索:'ul.stui-vodlist__media:eq(0) li,ul.stui-vodlist:eq(0) li,#searchList li;a&&title;.lazyload&&data-original;.text-muted&&Text;a&&href;.text-muted:eq(-1)&&Text',
    搜索:'body&&ul.stui-vodlist__media&&li;a&&title;.lazyload&&data-original;.text-muted&&Text;a&&href;.text-muted:eq(-1)&&Text',
    // cate_exclude: '首页|留言|APP|下载|资讯|新闻|动态',
    // tab_exclude: '猜你|喜欢|APP|下载|剧情',
}


/****上面才是pluto的drpy源,支持import外部模板来继承修改
 *  已知问题记录:
 *  自动补body逻辑可能有Bug，二级选集列表现在不正常了会报错
 *  1.pdfa没法正确获取非body开头的直接定位列表,比如 推荐 body&&ul.stui-vodlist.clearfix 和 ul.stui-vodlist.clearfix 获取出来的列表不一样,建议自动补body(已解决)
 * 2. pd函数有问题,没法正确的urljoin来源链接,比如分类页获取到数据href为/zbkdetail/63174.html应该自动与rule.url拼接后才返回给二级完整链接 (已解决)
 * .stui-pannel_hd h3 这个pdfa都没法识别?
 * pdf 系列不支持eq定位?
 * 解析播放问题,parse返回的1怎么下面不出解析选项 ?? 不过可以通免
 * urljoin问题,求求了这个函数很重要,还要pd函数内部需要自动urljoin (已解决)
 * 请求重复问题,调试日志一个console总是打印两次？？(待解决)
 * 筛选功能暂未实现,搜索验证码暂未实现
 * quickjs发生一次崩溃后除非重启软件,否则该源后续操作点击二级都没有数据
 * setItem系列存在问题,用的公用变量实现没法持久化,需要一个数据库存储持久化,下次进来也能获取储存的cookie
 * 电脑看日志调试
 adb tcpip 5555
 adb connect 192.168.10.192
 adb devices -l
 adb logcat -c
 adb logcat | grep -i QuickJS
 * ***/


/*** 以下是内置变量和解析方法 **/
const MOBILE_UA = 'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36';
const PC_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36';
const UA = 'Mozilla/5.0';
const UC_UA = 'Mozilla/5.0 (Linux; U; Android 9; zh-CN; MI 9 Build/PKQ1.181121.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.5.5.1035 Mobile Safari/537.36';
const IOS_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1';
const RULE_CK = 'cookie'; // 源cookie的key值
const KEY = typeof(key)!=='undefined'&&key?key:'drpy_'+rule.title; // 源的唯一标识
const CATE_EXCLUDE = '首页|留言|APP|下载|资讯|新闻|动态';
const TAB_EXCLUDE = '猜你|喜欢|APP|下载|剧情|热播';
const OCR_RETRY = 3;//ocr验证重试次数
// const OCR_API = 'http://dm.mudery.com:10000';//ocr在线识别接口
const OCR_API = 'http://192.168.3.239:5705/parse/ocr';//ocr在线识别接口
var MY_URL; // 全局注入变量,pd函数需要
var VODS = [];// 一级或者搜索需要的数据列表
var vod = {};//二级用单个影片详情

/** 处理一下 rule规则关键字段没传递的情况 **/
let rule_cate_excludes = (rule.cate_exclude||'').split('|').filter(it=>it.trim());
let rule_tab_excludes = (rule.tab_exclude||'').split('|').filter(it=>it.trim());
rule_cate_excludes = rule_cate_excludes.concat(CATE_EXCLUDE.split('|').filter(it=>it.trim()));
rule_tab_excludes = rule_tab_excludes.concat(TAB_EXCLUDE.split('|').filter(it=>it.trim()));

rule.cate_exclude = rule_cate_excludes.join('\n');
rule.tab_exclude = rule_tab_excludes.join('\n');
rule.host = rule.host||'';
rule.url = rule.url||'';
rule.homeUrl = rule.homeUrl||'';
rule.searchUrl = rule.searchUrl||'';

/*** 后台需要实现的java方法并注入到js中 ***/

/**
 * 读取本地文件->应用程序目录
 * @param filePath
 * @returns {string}
 */
function readFile(filePath){
    filePath = filePath||'./uri.min.js';
    var fd = os.open(filePath);
    var buffer = new ArrayBuffer(1024);
    var len = os.read(fd, buffer, 0, 1024);
    console.log(len);
    let text = String.fromCharCode.apply(null, new Uint8Array(buffer));
    console.log(text);
    return text
}

/**
 * 验证码识别逻辑,需要java实现(js没有bytes类型,无法调用后端的传递图片二进制获取验证码文本的接口)
 * @type {{api: string, classification: (function(*=): string)}}
 */
var OcrApi={
    api:OCR_API,
    classification:function (img){ // img是byte类型,这里不方便搞啊
        let code = '';
        try {
            let html = request(this.api,{data:{img:img},headers:{'User-Agent':PC_UA},'method':'POST'});
            html = JSON.parse(html);
            code = html.url||'';
        }catch (e) {}
        return code
    }
};
/**
 * 验证码识别,暂未实现
 * @param url 验证码图片链接
 * @returns {string} 验证成功后的cookie
 */
function verifyCode(url){
    let cnt = 0;
    let host = getHome(url);
    let cookie = '';
    while (cnt < OCR_RETRY){
        try{
            // let obj = {headers:headers,timeout:timeout};
            let yzm_url = `${host}/index.php/verify/index.html`;
            console.log(`验证码链接:${yzm_url}`);
            let hhtml = request(yzm_url,{withHeaders:true,toBase64:true});
            let json = JSON.parse(hhtml);
            if(!cookie){
                cookie = json['set-cookie']?json['set-cookie'].split(';')[0]:'';
            }
            // console.log(hhtml);
            console.log('cookie:'+cookie);
            let img = json.body;
            // console.log(img);
            let code = OcrApi.classification(img);
            console.log(`第${cnt+1}次验证码识别结果:${code}`);
            let submit_url = `${host}/index.php/ajax/verify_check?type=search&verify=${code}`;
            console.log(submit_url);
            let html = request(submit_url,{headers:{Cookie:cookie,'User-Agent':MOBILE_UA},'method':'POST'});
            // console.log(html);
            html = JSON.parse(html);
            if(html.msg === 'ok'){
                console.log(`第${cnt+1}次验证码提交成功`);
                return cookie // 需要返回cookie
            }else if(html.msg!=='ok'&&cnt+1>=OCR_RETRY){
                cookie = ''; // 需要清空返回cookie
            }
        }catch (e) {
            console.log(`第${cnt+1}次验证码提交失败:${e.message}`);
            if(cnt+1>=OCR_RETRY){
                cookie = '';
            }
        }
        cnt+=1
    }
    return cookie
}

/**
 * 存在数据库配置表里, key字段对应值value,没有就新增,有就更新,调用此方法会清除key对应的内存缓存
 * @param k 键
 * @param v 值
 */
function setItem(k,v){
    local.set(KEY,k,v);
    console.log(`规则${KEY}设置${k} => ${v}`)
}

/**
 *  获取数据库配置表对应的key字段的value，没有这个key就返回value默认传参.需要有缓存,第一次获取后会存在内存里
 * @param k 键
 * @param v 值
 * @returns {*}
 */
function getItem(k,v){
    return local.get(KEY,k) || v;
}

/**
 *  删除数据库key对应的一条数据,并清除此key对应的内存缓存
 * @param k
 */
function clearItem(k){
    local.delete(KEY,k);
}

/**
 *  url拼接(暂未实现)
 * @param fromPath 初始当前页面url
 * @param nowPath 相对当前页面url
 * @returns {*}
 */
function urljoin(fromPath, nowPath) {
    fromPath = fromPath||'';
    nowPath = nowPath||'';
    return joinUrl(fromPath, nowPath);
    // try {
    //     // import Uri from './uri.min.js';
    //     // var Uri = require('./uri.min.js');
    //     // eval(request('https://cdn.bootcdn.net/ajax/libs/URI.js/1.19.11/URI.min.js'));
    //     // let new_uri = URI(nowPath, fromPath);

    //     let new_uri = Uri(nowPath, fromPath);
    //     new_uri = new_uri.toString();
    //     // console.log(new_uri);
    //     // return fromPath + nowPath
    //     return new_uri
    // }
    // catch (e) {
    //     console.log('urljoin发生错误:'+e.message);
    //     if(nowPath.startsWith('http')){
    //         return nowPath
    //     }if(nowPath.startsWith('/')){
    //         return getHome(fromPath)+nowPath
    //     }
    //     return fromPath+nowPath
    // }
}

/**
 * 重写pd方法-增加自动urljoin(没法重写,改个名继续骗)
 * @param html
 * @param parse
 * @param uri
 * @returns {*}
 */
function pD(html,parse,uri){
    let ret = pdfh(html,parse);
    if(typeof(uri)==='undefined'||!uri){
        uri = '';
    }
    // MY_URL = getItem('MY_URL',MY_URL);
    // console.log(`规则${KEY}打印MY_URL:${MY_URL},uri:${uri}`);
    return urljoin(MY_URL,ret)
}

/*** js自封装的方法 ***/

/**
 * 获取链接的host(带http协议的完整链接)
 * @param url 任意一个正常完整的Url,自动提取根
 * @returns {string}
 */
function getHome(url){
    if(!url){
        return ''
    }
    let tmp = url.split('//');
    url = tmp[0] + '//' + tmp[1].split('/')[0];
    return url
}

/**
 * get参数编译链接,类似python params字典自动拼接
 * @param url 访问链接
 * @param obj 参数字典
 * @returns {*}
 */
function buildUrl(url,obj){
    obj = obj||{};
    if(url.indexOf('?')<0){
        url += '?'
    }
    let param_list = [];
    let keys = Object.keys(obj);
    keys.forEach(it=>{
        param_list.push(it+'='+obj[it])
    });
    let prs = param_list.join('&');
    if(keys.length > 0 && !url.endsWith('?')){
        url += '&'
    }
    url+=prs;
    return url
}

/**
 * 远程依赖执行函数
 * @param url 远程js地址
 */
function require(url){
    eval(request(url));
}

/**
 * 海阔网页请求函数完整封装
 * @param url 请求链接
 * @param obj 请求对象 {headers:{},method:'',timeout:5000,body:'',withHeaders:false}
 * @returns {string|string|DocumentFragment|*}
 */
function request(url,obj){
    if(typeof(obj)==='undefined'||!obj||obj==={}){
        obj = {
            headers:{
                'User-Agent':MOBILE_UA,
                'Referer':getHome(url),
            }
        }
    }else{
        let headers = obj.headers||{};
        let keys = Object.keys(headers).map(it=>it.toLowerCase());
        if(!keys.includes('user-agent')){
            headers['User-Agent'] = MOBILE_UA;
        }if(!keys.includes('referer')){
            headers['Referer'] = getHome(url);
        }
        obj.headers = headers;
    }
    console.log(JSON.stringify(obj.headers));
    if(typeof(obj.headers.body)!='undefined'&&obj.headers.body&&typeof (obj.headers.body)==='string'){
        let data = {};
        obj.headers.body.split('&').forEach(it=>{
            data[it.split('=')[0]] = it.split('=')[1]
        });
        obj.data = data;
        delete obj.headers.body
    }
    if(!url){
        return obj.withHeaders?'{}':''
    }
    if(obj.toBase64){ // 返回base64,用于请求图片
        obj.buffer = 2;
        delete obj.toBase64
    }
    let res = req(url, obj);
    let html = res.content||'';
    if(obj.withHeaders){
        let htmlWithHeaders = res.headers;
        htmlWithHeaders.body = html;
        return JSON.stringify(htmlWithHeaders);
    }else{
        return html
    }
}

/**
 * 检查宝塔验证并自动跳过获取正确源码
 * @param html 之前获取的html
 * @param url 之前的来源url
 * @param obj 来源obj
 * @returns {string|DocumentFragment|*}
 */
function checkHtml(html,url,obj){
    if(/\?btwaf=/.test(html)){
        let btwaf = html.match(/btwaf(.*?)"/)[1];
        url = url.split('#')[0]+'?btwaf'+btwaf;
        html = request(url,obj);
    }
    return html
}

/**
 *  带一次宝塔验证的源码获取
 * @param url 请求链接
 * @param obj 请求参数
 * @returns {string|DocumentFragment}
 */
function getCode(url,obj){
    let html = request(url,obj);
    html = checkHtml(html,url,obj);
    return html
}

/**
 * 源rule专用的请求方法,自动注入cookie
 * @param url 请求链接
 * @returns {string|DocumentFragment}
 */
function getHtml(url){
    let obj = {};
    if(rule.headers){
        obj.headers = rule.headers;
    }
    let cookie = getItem(RULE_CK,'');
    if(cookie){
        if(obj.headers && ! Object.keys(obj.headers).map(it=>it.toLowerCase()).includes('cookie')){
            obj.headers['Cookie'] = cookie;
        }else if(!obj.headers){
            obj.headers = {Cookie:cookie};
        }
    }
    let html = getCode(url,obj);
    return html
}

/**
 * 首页分类解析，筛选暂未实现
 * @param homeObj 首页传参对象
 * @returns {string}
 */
function homeParse(homeObj) {
    let classes = [];
    if (homeObj.class_name && homeObj.class_url) {
        let names = homeObj.class_name.split('&');
        let urls = homeObj.class_url.split('&');
        let cnt = Math.min(names.length, urls.length);
        for (let i = 0; i < cnt; i++) {
            classes.push({
                'type_id': urls[i],
                'type_name': names[i]
            });
        }
    }

    if (homeObj.class_parse) {
        let p = homeObj.class_parse.split(';');
        if (p.length >= 4) {
            try {
                let html = getHtml(homeObj.MY_URL);
                if (html) {
                    let list = pdfa(html, p[0]);
                    if (list && list.length > 0) {
                        list.forEach(it => {
                            try {
                                let name = pdfh(it, p[1]);
                                if (homeObj.cate_exclude && (new RegExp(homeObj.cate_exclude).test(name))) {
                                    return;
                                }
                                let url = pdfh(it, p[2]);
                                if (p[3]) {
                                    let exp = new RegExp(p[3]);
                                    url = url.match(exp)[1];
                                }

                                classes.push({
                                    'type_id': url,
                                    'type_name': name
                                });
                            } catch (e) {
                                console.log(e.message);
                            }
                        });
                    }
                }
            } catch (e) {
                console.log(e.message);
            }

        }
    }
    let resp = {
        'class': classes
    };
    if(homeObj.filter){
        resp.filters = homeObj.filter;
    }
    console.log(JSON.stringify(resp));
    return JSON.stringify(resp);

}

/**
 *  首页推荐列表解析
 * @param homeVodObj
 * @returns {string}
 */
function homeVodParse(homeVodObj){
    let d = [];
    MY_URL = homeVodObj.homeUrl;
    // setItem('MY_URL',MY_URL);
    console.log(MY_URL);
    let p = homeVodObj.推荐;
    if(!p){
        return '{}'
    }
    if(typeof(p)==='string'&&p.trim().startsWith('js:')){
        const TYPE = 'home';
        var input = MY_URL;
        const HOST = rule.host;
        eval(p.trim().replace('js:',''));
        d = VODS;
    }else {
        p = p.split(';');
        if (!homeVodObj.double && p.length < 5) {
            return '{}'
        } else if (homeVodObj.double && p.length < 6) {
            return '{}'
        }
        let html = getHtml(MY_URL);
        try {
            console.log('double:' + homeVodObj.double);
            if (homeVodObj.double) {
                p[0] = p[0].trim().startsWith('json:') ? p[0].replace('json:', '') : p[0];
                // console.log(p[0]);
                let items = pdfa(html, p[0]);
                // console.log(items.length);
                for (let item of items) {
                    // console.log(p[1]);
                    let items2 = pdfa(item, p[1]);
                    // console.log(items2.length);
                    for (let item2 of items2) {
                        try {
                            let title = pdfh(item2, p[2]);
                            let img = '';
                            try {
                                img = pD(item2, p[3])
                            } catch (e) {
                            }
                            let desc = pdfh(item2, p[4]);
                            let links = [];
                            for (let p5 of p[5].split('+')) {
                                let link = !homeVodObj.detailUrl ? pD(item2, p5, MY_URL) : pdfh(item2, p5);
                                links.push(link);
                            }
                            let vod = {
                                vod_name: title,
                                vod_pic: img,
                                vod_remarks: desc,
                                vod_id: links.join('$')
                            };
                            d.push(vod);
                        } catch (e) {

                        }

                    }


                }


            } else {
                p[0] = p[0].trim().startsWith('json:') ? p[0].replace('json:', '') : p[0];
                let items = pdfa(html, p[0]);
                for (let item of items) {
                    try {
                        let title = pdfh(item, p[1]);
                        let img = '';
                        try {
                            img = pD(item, p[2], MY_URL);
                        } catch (e) {

                        }
                        let desc = pdfh(item, p[3]);
                        let links = [];
                        for (let p5 of p[4].split('+')) {
                            let link = !homeVodObj.detailUrl ? pD(item, p5, MY_URL) : pdfh(item, p5);
                            links.push(link);
                        }
                        let vod = {
                            vod_name: title,
                            vod_pic: img,
                            vod_remarks: desc,
                            vod_id: links.join('$')
                        };
                        d.push(vod);

                    } catch (e) {

                    }

                }

            }

        } catch (e) {

        }
    }
    // console.log(JSON.stringify(d));
    return JSON.stringify({
        list:d
    })
}

/**
 * 一级分类页数据解析
 * @param cateObj
 * @returns {string}
 */
function categoryParse(cateObj) {
    let p = cateObj.一级;
    let d = [];
    // let url = cateObj.url.replaceAll('fyclass', cateObj.tid).replaceAll('fypage', cateObj.pg);
    let url = cateObj.url.replaceAll('fyclass', cateObj.tid);
    if(rule.filter_url){
        if(!/fyfilter/.test(url)){
            if(!url.endsWith('&')&&!rule.filter_url.startsWith('&')){
                url+='&'
            }
            url+=rule.filter_url;
        }else{
            url = url.replace('fyfilter', rule.filter_url);
        }
        // console.log('filter:'+cateObj.filter);
        let fl = cateObj.filter?cateObj.extend:{};
        url = drT.renderText(url,fl);
    }
    if(/fypage/.test(url)){
        if(url.includes('(')&&url.includes(')')){
            let url_rep = url.match(/.*?\((.*)\)/)[1];
            let cnt_page = url_rep.replaceAll('fypage', cateObj.pg);
            eval(`let cnt_pg=${cnt_page}`);
            url = url.replaceAll(url_rep,cnt_pg).replaceAll('(','').replaceAll(')','');
        }else{
            url = url.replaceAll('fypage',cateObj.pg);
        }
    }
    if(cateObj.pg === 1 && url.includes('[')&&url.includes(']')){
        url = url.split('[')[1].split(']')[0];
    }
    MY_URL = url;
    // setItem('MY_URL',MY_URL);
    console.log(MY_URL);

    if(typeof(p)==='string'&&p.trim().startsWith('js:')){
        const MY_CATE = cateObj.tid;
        const MY_FL = cateObj.extend;
        const TYPE = 'cate';
        var input = MY_URL;
        const MY_PAGE = cateObj.pg;
        eval(p.trim().replace('js:',''));
        d = VODS;
    }else {
        p = p.split(';');
        if (p.length < 5) {
            return '{}'
        }
        try {
            let html = getHtml(MY_URL);
            if (html) {
                let list = pdfa(html, p[0]);
                list.forEach(it => {
                    d.push({
                        'vod_id': pD(it, p[4],MY_URL),
                        'vod_name': pdfh(it, p[1]),
                        'vod_pic': pD(it, p[2],MY_URL),
                        'vod_remarks': pdfh(it, p[3]),
                    });
                });
            }
        } catch (e) {
            console.log(e.message);
        }
    }

    return d.length<1?'{}':JSON.stringify({
        'page': parseInt(cateObj.pg),
        'pagecount': 999,
        'limit': 20,
        'total': 999,
        'list': d,
    });
}

/**
 * 搜索列表数据解析
 * @param searchObj
 * @returns {string}
 */
function searchParse(searchObj) {
    let d = [];
    if(!searchObj.searchUrl){
        return '{}'
    }
    let p = searchObj.搜索==='*'&&rule.一级 ? rule.一级 : searchObj.搜索;
    let url = searchObj.searchUrl.replaceAll('**', searchObj.wd).replaceAll('fypage', searchObj.pg);
    MY_URL = url;
    console.log(MY_URL);
    // setItem('MY_URL',MY_URL);
    if(typeof(p)==='string'&&p.trim().startsWith('js:')){
        const TYPE = 'search';
        const MY_PAGE = searchObj.pg;
        const KEY = searchObj.wd;
        var input = MY_URL;
        var detailUrl = rule.detailUrl||'';
        eval(p.trim().replace('js:',''));
        d = VODS;
    }else{
        p = p.split(';');
        if (p.length < 5) {
            return '{}'
        }
        try {
            let html = getHtml(MY_URL);
            if (html) {
                if(/系统安全验证|输入验证码/.test(html)){
                    let cookie = verifyCode(MY_URL);
                    if(cookie){
                        console.log(`本次成功过验证,cookie:${cookie}`);
                        setItem(RULE_CK,cookie);
                    }else{
                        console.log(`本次自动过搜索验证失败,cookie:${cookie}`);
                    }
                    // obj.headers['Cookie'] = cookie;
                    html = getHtml(MY_URL);
                }
                if(!html.includes(searchObj.wd)){
                    console.log('搜索结果源码未包含关键字,疑似搜索失败,正为您打印结果源码');
                    console.log(html);
                }
                let list = pdfa(html, p[0]);
                list.forEach(it => {
                    let ob = {
                        'vod_id': pD(it, p[4],MY_URL),
                        'vod_name': pdfh(it, p[1]),
                        'vod_pic': pD(it, p[2],MY_URL),
                        'vod_remarks': pdfh(it, p[3]),
                    };
                    if (p.length > 5 && p[5]) {
                        ob.vod_content = pdfh(it, p[5]);
                    }
                    d.push(ob);
                });

            }
        } catch (e) {
            return '{}'
        }
        return JSON.stringify({
            'page': parseInt(searchObj.pg),
            'pagecount': 10,
            'limit': 20,
            'total': 100,
            'list': d,
        });
    }
}

/**
 * 二级详情页数据解析
 * @param detailObj
 * @returns {string}
 */
function detailParse(detailObj){
    let vod = {
        vod_id: "id",
        vod_name: "片名",
        vod_pic: "",
        type_name: "剧情",
        vod_year: "年份",
        vod_area: "地区",
        vod_remarks: "更新信息",
        vod_actor: "主演",
        vod_director: "导演",
        vod_content: "简介"
    };
    let p = detailObj.二级;
    let url = detailObj.url;
    let detailUrl = detailObj.detailUrl;
    let fyclass = detailObj.fyclass;
    let tab_exclude = detailObj.tab_exclude;
    let html = detailObj.html||'';
    MY_URL = url;
    console.log(MY_URL);
    // setItem('MY_URL',MY_URL);
    if(p==='*'){
        vod.vod_play_from = '道长在线';
        vod.vod_remarks = detailUrl;
        vod.vod_actor = '没有二级,只有一级链接直接嗅探播放';
        vod.vod_content = MY_URL;
        vod.vod_play_url = '嗅探播放$' + MY_URL;
    }else if(typeof(p)==='string'&&p.trim().startsWith('js:')){
        const TYPE = 'detail';
        var input = MY_URL;
        eval(p.trim().replace('js:',''));
    }else if(p&&typeof(p)==='object'){
        if(!html){
            html = getHtml(MY_URL);
        }
        if(p.title){
            let p1 = p.title.split(';');
            vod.vod_name = pdfh(html, p1[0]).replaceAll('\n', ' ').trim();
            let type_name = p1.length > 1 ? pdfh(html, p1[1]).replaceAll('\n', ' ').trim():'';
            vod.type_name = type_name||vod.type_name;
        }
        if(p.desc){
            try{
                let p1 = p.desc.split(';');
                vod.vod_remarks =  pdfh(html, p1[0]).replaceAll('\n', ' ').trim();
                vod.vod_year = p1.length > 1 ? pdfh(html, p1[1]).replaceAll('\n', ' ').trim():'';
                vod.vod_area = p1.length > 2 ? pdfh(html, p1[2]).replaceAll('\n', ' ').trim():'';
                vod.vod_actor = p1.length > 3 ? pdfh(html, p1[3]).replaceAll('\n', ' ').trim():'';
                vod.vod_director = p1.length > 4 ? pdfh(html, p1[4]).replaceAll('\n', ' ').trim():'';
            }
            catch (e) {

            }
        }
        if(p.content){
            try{
                let p1 = p.content.split(';');
                vod.vod_content =  pdfh(html, p1[0]).replaceAll('\n', ' ').trim();
            }
            catch (e) {}
        }
        if(p.img){
            try{
                let p1 = p.img.split(';');
                vod.vod_pic =  pD(html, p1[0],MY_URL);
            }
            catch (e) {}
        }

        let vod_play_from = '$$$';
        let playFrom = [];
        if(p.重定向&&p.重定向.startsWith('js:')){
            html = eval(p.重定向.replace('js:',''));
        }
        
// console.log(2);
        if(p.tabs){
            let p_tab = p.tabs.split(';')[0];
            console.log(p_tab);
            let vHeader = pdfa(html, p_tab);

            console.log(vHeader.length);
            for(let v of vHeader){
                let v_title = pdfh(v,'body&&Text');
                console.log(v_title);
                if(tab_exclude&& (new RegExp(tab_exclude)).test(v_title)){
                    continue;
                }
                playFrom.push(v_title);
            }
            console.log(JSON.stringify(playFrom));
        }else{
            playFrom = ['道长在线']
        }
        vod.vod_play_from = playFrom.join(vod_play_from);

// console.log(3);
        let vod_play_url = '$$$';
        let vod_tab_list = [];
        if(p.lists){
            for(let i=0;i<playFrom.length;i++){
                let tab_name = playFrom[i];
                let tab_ext =  p.tabs.split(';').length > 1 ? p.tabs.split(';')[1] : '';
                let p1 = p.lists.replaceAll('#idv', tab_name).replaceAll('#id', i);
                tab_ext = tab_ext.replaceAll('#idv', tab_name).replaceAll('#id', i);
                console.log(p1);
                // console.log(html);
                let vodList = [];
                try {
                    vodList =  pdfa(html, p1);
                    console.log('len(vodList):'+vodList.length);
                }catch (e) {
                    // console.log(e.message);
                }
                let new_vod_list = [];
                let tabName = tab_ext?pdfh(html, tab_ext):tab_name;
                console.log(tabName);
                vodList.forEach(it=>{
                    new_vod_list.push(pdfh(it,'body&&Text')+'$'+pD(it,'a&&href',MY_URL));
                });
                let vlist = new_vod_list.join('#');
                vod_tab_list.push(vlist);
            }
        }
        vod.vod_play_url = vod_tab_list.join(vod_play_url);
    }
// console.log(JSON.stringify(vod));
    return JSON.stringify({
        list: [vod]
    })
}

/**
 * 选集播放点击事件解析
 * @param playObj
 * @returns {string}
 */
function playParse(playObj){
    MY_URL = playObj.url;
    var input = MY_URL;
    let common_play = {
        parse:1,
        url:MY_URL
    };
    let lazy_play;
    if(!rule.play_parse||!rule.lazy){
        lazy_play =  common_play;
    }else if(rule.play_parse&&rule.lazy&&typeof(rule.lazy)==='string'){
        try {
            eval(rule.lazy.replace('js:').trim());
            lazy_play = typeof(input) === 'object'?input:{
                parse:1,
                jx:1,
                url:input
            };
        }catch (e) {
            lazy_play =  common_play;
        }
    }else{
        lazy_play =  common_play;
    }
    console.log(JSON.stringify(lazy_play));
    return JSON.stringify(lazy_play);
}

/**
 * js源预处理特定返回对象中的函数
 * @param ext
 */
function init(ext) {
    console.log("init");
    try {
        init_test();
    }catch (e) {
        console.log('init_test发生错误:'+e.message);
    }
}

/**
 * js源获取首页分类和筛选特定返回对象中的函数
 * @param filter 筛选条件字典对象
 * @returns {string}
 */
function home(filter) {
    console.log("home");
    let homeObj = {
        filter:rule.filter||false,
        MY_URL: rule.host,
        class_name: rule.class_name || '',
        class_url: rule.class_url || '',
        class_parse: rule.class_parse || '',
        cate_exclude: rule.cate_exclude,
    };
    return homeParse(homeObj);
}

/**
 * js源获取首页推荐数据列表特定返回对象中的函数
 * @param params
 * @returns {string}
 */
function homeVod(params) {
    let homeUrl = rule.host&&rule.homeUrl?urljoin(rule.host,rule.homeUrl):(rule.homeUrl||rule.host);
    let detailUrl = rule.host&&rule.detailUrl?urljoin(rule.host,rule.detailUrl):rule.detailUrl;
    let homeVodObj = {
        推荐:rule.推荐,
        double:rule.double,
        homeUrl:homeUrl,
        detailUrl:detailUrl
    };
    return homeVodParse(homeVodObj)
    // return "{}";
}

/**
 * js源获取分类页一级数据列表特定返回对象中的函数
 * @param tid 分类id
 * @param pg 页数
 * @param filter 当前选中的筛选条件
 * @param extend 扩展
 * @returns {string}
 */
function category(tid, pg, filter, extend) {
    let cateObj = {
        url: urljoin(rule.host, rule.url),
        一级: rule.一级,
        tid: tid,
        pg: parseInt(pg),
        filter: filter,
        extend: extend
    };
    // console.log(JSON.stringify(extend));
    return categoryParse(cateObj)
}

/**
 * js源获取二级详情页数据特定返回对象中的函数
 * @param vod_url 一级列表中的vod_id或者是带分类的自拼接 vod_id 如 fyclass$vod_id
 * @returns {string}
 */
function detail(vod_url) {
    let fyclass = '';
    if(vod_url.indexOf('$')>-1){
        let tmp = vod_url.split('$');
        fyclass = tmp[0];
        vod_url = tmp[1];
    }
    let detailUrl = vod_url;
    let url;
    rule.homeUrl = urljoin(rule.host,rule.homeUrl);
    rule.detailUrl = urljoin(rule.host,rule.detailUrl);
    if(!detailUrl.startsWith('http')&&!detailUrl.includes('/')){
        url = rule.detailUrl.replaceAll('fyid', detailUrl).replaceAll('fyclass',fyclass);
    }else if(detailUrl.includes('/')){
        url = urljoin(rule.homeUrl,detailUrl);
    }else{
        url = detailUrl
    }
    let detailObj = {
        url:url,
        二级:rule.二级,
        detailUrl:detailUrl,
        fyclass:fyclass,
        tab_exclude:rule.tab_exclude,
    }
    return detailParse(detailObj)
}

/**
 * js源选集按钮播放点击事件特定返回对象中的函数
 * @param flag 线路名
 * @param id 播放按钮的链接
 * @param flags 全局配置的flags是否需要解析的标识列表
 * @returns {string}
 */
function play(flag, id, flags) {
    let playObj = {
        url:id,
        flag:flag,
        flags:flags
    }
    return playParse(playObj);
}

/**
 * js源搜索返回的数据列表特定返回对象中的函数
 * @param wd 搜索关键字
 * @param quick 是否来自快速搜索
 * @returns {string}
 */
function search(wd, quick) {
    let searchObj = {
        searchUrl: urljoin(rule.host, rule.searchUrl),
        搜索: rule.搜索,
        wd: wd,
        //pg: pg,
        pg: 1,
        quick: quick,
    };
    // console.log(JSON.stringify(searchObj));
    return searchParse(searchObj)
}

function DRPY(){//导出函数
    return {
        init: init,
        home: home,
        homeVod: homeVod,
        category: category,
        detail: detail,
        play: play,
        search: search,
    }
}

// 导出函数对象
export default {
    init: init,
    home: home,
    homeVod: homeVod,
    category: category,
    detail: detail,
    play: play,
    search: search,
    DRPY:DRPY
}