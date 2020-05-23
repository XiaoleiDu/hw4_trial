/*"use strict"



var username = document.getElementsByName('email')[0].value;
var userpassword = document.getElementsByName('password')[0].value;
alert(username);
alert(userpassword);*/




//<![CDATA[
function getNameFile(){
 var fileName="names.txt", xmlHttp=new XMLHttpRequest();
 xmlHttp.onreadystatechange=function(){
  var tmpDoc, re=/^(.+)$/gm, arr=[], oP;
  if(xmlHttp.readyState===4){
   if(xmlHttp.status===200){
    tmpDoc=xmlHttp.responseText;
    arr=re.exec(tmpDoc);
    while(arr!==null){
     oP=document.createElement("P");
     document.getElementById("namesFromFile").appendChild(oP).appendChild(document.createTextNode(arr[1]));
     document.getElementById("namesFromFile").appendChild(document.createTextNode("\r\n"));
     //insert tests -> for style/format
     if(arr[1].substr(0,4)==="John"){
      oP.style.color="#f00";
     }
     if(arr[1].split(" ")[0]==="Sue"){
      oP.style.color="#0c0";
      oP.style.fontWeight="bold";
     }
     alert(arr[1].split(" ")[0]);
     arr=re.exec(tmpDoc);
    }
    xmlHttp=null;
   }
  }
 };
 xmlHttp.open("POST", fileName, true); //Use POST to prevent use of cached file
 xmlHttp.send();
}
function refreshNamesFromFile(){
 var namesNode=document.getElementById("namesFromFile");
 while(namesNode.firstChild){
  namesNode.removeChild(namesNode.firstChild);
 }
 getNameFile();
}
function sortByName(e){
 var i=0, el, sortEl=[], namesNode=document.getElementById("namesFromFile"), sortMethod, evt, evtSrc, oP;
 evt=e||event;
 evtSrc=evt.target||evt.srcElement;
 sortMethod=(evtSrc.id==="firstSort")?"first":"last";
 while(el=namesNode.getElementsByTagName("P").item(i++)){
  sortEl[i-1]=[el.innerHTML.split(" ")[0],el.innerHTML.split(" ")[1]];
 }
 sortEl.sort(function(a,b){
  var x=a[0].toLowerCase(), y=b[0].toLowerCase(), s=a[1].toLowerCase(), t=b[1].toLowerCase();
  if(sortMethod==="first"){
   return x<y?-1:x>y?1:s<t?-1:s>t?1:0;
  }
  else{
   return s<t?-1:s>t?1:x<y?-1:x>y?1:0;
  }
 });
 while(namesNode.firstChild){
  namesNode.removeChild(namesNode.firstChild);
 }
 for(i=0;i<sortEl.length;i++){
  oP=document.createElement("P");
  namesNode.appendChild(oP).appendChild(document.createTextNode(sortEl[i][0]+" "+sortEl[i][1]));
  namesNode.appendChild(document.createTextNode("\r\n"));
  //insert tests ->  for style/format
  if(sortEl[i][0]==="John"){
   oP.style.color="#f00";
  }
  if(sortEl[i][0]==="Sue"){
   oP.style.color="#0c0";
   oP.style.fontWeight="bold";
  }
 }
}
document.onreadystatechange=function(){
 if(document.readyState==="complete"){
  getNameFile();
  document.getElementById("refreshNames").onclick=refreshNamesFromFile;
  document.getElementById("firstSort").onclick=document.getElementById("lastSort").onclick=sortByName;
 }
};
//]]>