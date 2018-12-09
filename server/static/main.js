"use strict"

//originally i wanted to do everything with HTML/CSS only so the website works without javascript for compatiblity and performance reasons, but since i need to somehow showcase my skills, here are some unnecessary javascript shenanigans

let profileOnClick = function(){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', "https://ipinfo.io/json", true);
    xhr.onloadend = function(){ 
        let obj = JSON.parse(xhr.responseText)
        let msg = `Profiles aren't implemented yet, so instead here is everything I know about you:\n\nYour ip address is ${obj.ip} allocated by ${obj.org} at ${obj.loc} in ${obj.postal} ${obj.city}, ${obj.region} ${obj.country}.\n\nYour useragent is ${window.navigator.userAgent}`
        alert(msg)
    }
    xhr.send()
}
let wikiOnClick = function(){
    window.location.href="https://github.com/mskeegan01/GreenCampus/blob/master/README.md"
}

let initEvents = function(){
    document.getElementById("button_profile").addEventListener('click', profileOnClick)
    document.getElementById("button_wiki").addEventListener('click', wikiOnClick)
}

window.onload = initEvents