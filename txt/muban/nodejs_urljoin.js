const url = require('url');
let a = url.resolve('http://example.com/one', '/two');
let b = url.resolve('http://example.com/one', 'http://www.baidu.com');
console.log(a);
console.log(b);