/**
 * 扩展es6函数 fromEntries
 * @param iterable
 * @returns {*}
 */
Object.fromEntries = function fromEntries (iterable) {
  return [...iterable].reduce((obj, [key, val]) => {
    obj[key] = val;
    return obj;
  }, {});
};

/**
 *
 * @param url 原始接口链接,支持带参数
 * @param params_str 拼接搜索字符串 如 ?a=1&b=2
 * @returns {string} 返回拼接后的完整链接,支持带上原始接口链接的hash
 */
const buildUrl = function (url,params_str){
  const u = new URL(url);
  const p = new URLSearchParams(params_str);
  const api = u.origin + u.pathname;
  let params = Object.fromEntries(u.searchParams.entries());
  let params_obj = Object.fromEntries(p.entries());
  Object.assign(params,params_obj);
  let plist = [];
  for(let key in params){
    plist.push(key+'='+params[key]);
  }
  return api + '?' + plist.join('&') + u.hash
};