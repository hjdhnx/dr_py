// npm install urijs
var URI = require('urijs');
var uri = new URI("/relative/path");


// let c = URI.resolve('http://example.com/one', '/two');
// let d = URI.resolve('http://example.com/one', 'http://www.baidu.com');
// console.log(c);
// console.log(d);
var uri2 = URI("../foobar.html", "http://example.org/hello/world.html");
console.log(uri2.toString())
uri2 = URI('http://www.baidu.com', 'http://example.com/one');
console.log(uri2.toString())

uri2 = URI('', 'http://example.com/one');
console.log(uri2.toString())

function urljoin(fromPath, nowPath) {
    let new_uri = URI(nowPath, fromPath);
    new_uri = new_uri.toString();
    // console.log(new_uri);
    // return fromPath + nowPath
    return new_uri
}
console.log(urljoin('http://example.com/one','/detail/1.html'));
console.log(urljoin('http://example.com/one/path/','detail/1.html'));
console.log(urljoin('http://example.com/one','http://www.baidu.com'));
console.log(urljoin('https://example.com/one','//path/1.png'));


// make path relative
var relUri = uri.relativeTo("/relative/sub/foo/sub/file"); // returns a new URI instance
// relUri == "../../../path"

// absolute URLs are passed through unchanged
let a = URI("http://example.org/world.html").relativeTo("http://google.com/baz");
console.log(a.toString())
// -> "http://example.org/world.html"

// absolute URLs relative to absolute URLs
// may resolve the protocol
URI("http://example.org/world.html")
    .clone()
    .authority("")
    .relativeTo("http://google.com/baz");
// -> "//google.com/world.html"

// equal URLs are relative by empty string
URI("http://www.example.com:8080/dir/file")
    .relativeTo('http://www.example.com:8080/dir/file');
// -> ""

// relative on fragment and query string as well
URI("http://www.example.com:8080/dir/file?foo=bar#abcd")
    .relativeTo('http://www.example.com:8080/dir/file');