function pageY(elem) {
    return elem.offsetParent ? (elem.offsetTop + pageY(elem.offsetParent)) : elem.offsetTop;
}

function pageX(elem) {
    return elem.offsetParent ? (elem.offsetLeft + pageX(elem.offsetParent)) : elem.offsetLeft;
}

function iframeSize(){
  let width = document.documentElement.clientWidth;
  let height = document.documentElement.clientHeight;
  if (width >= 768)
  {
    width -= pageX(document.getElementById('ifm'))+ buffer ;
    width = (width < 0) ? 0 : width;
    height -= pageY(document.getElementById('ifm'))+ buffer ;
    height = (height < 0) ? 0 : height;
  }
  else
  {
    height -= pageY(document.getElementById('ifm'))+ buffer ;
    height = (height < 0) ? 0 : height;
  }
  let size = (width > height) ? height : width;
  return size;
}

function updateIframe(link){
  let size = iframeSize();
  document.getElementById('ifm_container').innerHTML ='';
  let tempifm = document.createElement('iframe');
  tempifm.style = "border:none";
  tempifm.style.height = size + 'px';
  tempifm.style.width = size + 'px';
  tempifm.id = 'ifm';
  tempifm.src = link;
  document.getElementById('ifm_container').appendChild(tempifm);
  document.getElementById('currentLink').href = link;
}

function resizeIframe(){
  let iframe = document.getElementById('ifm');
  if (document.getElementById('faceBtn').style.display != 'none'){
    let link = iframe.src;
    updateIframe(link); // Only run if a character has been selected
  }
  else {  // If no character has been selected
    let size = iframeSize();
    iframe.style.height = size + 'px';
    iframe.style.width = size + 'px';
  }
}
