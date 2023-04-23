var global_grey = {
  '-webkit-filter':'grayscale(1)',
  '-moz-filter':'grayscale(1)',
  '-ms-filter':'grayscale(1)',
  '-o-filter':'grayscale(1)',
  'filter':'grayscale(1)',
};

function autoGreyByTime(){
  let now = new Date();
  let now_hours = now.getHours();
  // console.log(now_hours,typeof now_hours);
  if(now_hours >= 23 || now_hours < 8){
      $('html').css(global_grey);
  }
}
autoGreyByTime();

function darkModeHandler() {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    if (mediaQuery.matches) {
        let color = '#1b1b1b';
        $('body').css({"background": color });
    }
}
darkModeHandler();