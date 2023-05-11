window.xcsoft = window.xcsoft || {};
xcsoft.tipsCss = {
	height: "40px",
	fontSize: "14px",
	top:"82%"
};
xcsoft.tipsHide = xcsoft.tipsShow = "fast";
xcsoft.dom;
xcsoft.timeout;
xcsoft.loading = function(b) {
	xcsoft.init(b, 0, "loading", !0)
};
xcsoft.info = function(b, c) {
	xcsoft.init(b, c || 2500, "info")
};
xcsoft.error = function(b, c) {
	xcsoft.init(b, c || 2E3, "error")
};
xcsoft.success = function(b, c) {
	xcsoft.init(b, c || 1500, "success")
};
xcsoft.init = function(b, c, a, d) {
	this.tipsHtml(b, a);
	$(this.dom).animate({
		left: 0,
		top:"82%"
	}, this.tipsHide);
	clearTimeout(this.timeout);
	this.timeout = !d && setTimeout(function() {
		xcsoft._hide()
	}, c)
};
xcsoft._hide = function() {
	this.dom.stop().animate({
		left: "-" + xcsoft.tipsCss.height
	}, this.tipsHide, "", function() {
		$(this).remove()
	})
};
xcsoft.tipsHtml = function(b, c) {
	var a = $(".xctips");
	c = c || "info";
	0 == a.length ? (a = document.createElement("div"), a.className = "xctips " + c, this.dom = $(a), this.dom.css(this.tipsCss), a.style.left = "-" + this.tipsCss.height, a.style.height = this.tipsCss.height, a.style.lineHeight = this.tipsCss.height, a.innerHTML = b, $("body").append(this.dom)) : (a.html(b), a.attr("class", "xctips " + c), this.dom = a)
};