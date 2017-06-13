/**
 * Created by Myway on 2017/6/8.
 */
// 检查Cookies
/*function getCookie(cname) {
    if(document.cookie.length > 0) {
        cstart = document.cookie.indexOf(cname + '=');
        if(cstart !== -1) {
            cstart = cstart + cname.length + 1;
            cend = document.cookie.indexOf(';', cstart);
            if(cend === -1) cend = document.cookie.length;
            return unescape(document.cookie.substring(cstart, cend))
        }
    }
    return ''
}
function setCookie(cname, value, expiresday) {
    var esdate = new Date();
    esdate.setDate(esdate.getDate() + expiresday);
    document.cookie = cname + '=' +escape(value) + ((expiredays===null) ? "" : "; expires="+exdate.toGMTString());
}
function checkCookie() {
    var username = getCookie('username');
    if (username!==null && username!=="")
        {alert('Welcome again '+username+'!')}
    else {
        username=prompt('Please enter your name:',"");
    if (username!=null && username!="") {
        setCookie('username',username,365)
    }
  }
}*/
/*var c = 0;
var t;
function set() {
    document.getElementById('txt').value = c;
    c += 1;
    setTimeout('set()', 1000);
}

function time() {
    var day = new Date();
    var h = day.getHours();
    var m = day.getMinutes();
    var s = day.getSeconds();
    m = checktime(m);
    s = checktime(s);
    document.getElementById('text').innerHTML = h + ':' + m +':' + s;
    t = setTimeout('time()', 1000);
}
function checktime(i) {
    if(i < 10 ) {
        i = '0' + i}
    return i
}
function stoptime() {
    document.getElementById('text').innerHTML = '';
    clearTimeout(t)
}*/


