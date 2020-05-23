document.addEventListener("DOMContentLoaded", function() {
  let btn=document.querySelector('#burger');
  let sb = document.querySelector('.overlay_sidebar');  

  btn.onclick = function toggle() {
    sb.classList.toggle('closed');
  }          
});