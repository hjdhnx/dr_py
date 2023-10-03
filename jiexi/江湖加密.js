var flag = [];
function lazy() {
    let PWD = 'drpy';
// log(params);
    if (!params.passwd) {
        realUrl = input
    } else if (params.passwd !== PWD) {
        realUrl = toast(input + ' 解析失败。解析密码错误');
    } else {
        realUrl = 重定向('http://211.99.99.236:4567/jhjson/ceshi.php?url=' + input)
    }
    return realUrl
}