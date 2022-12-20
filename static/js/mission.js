// 업로드 버튼을 제출 버튼으로 바꿈
function toggle() {
  var element1=document.getElementById('fileimg');
  var element2=document.getElementById('returnimg');
  var element3=document.getElementsByClassName('buttonload');
    
  if ( element1.style.display!='none' ) {
    element1.disabled = true;
    element1.style.display='none';
    element2.style.display="block";
  } else {
    element1.style.display='block';
    element1.disabled = false;
    element2.style.display="none";
  }
}

// 제출 버튼 누르면 popup 창 뜸
// 이미지 확인 느낌을 주기 위해 로딩 아이콘이 보이면서 3초 정도 딜레이
function popup() {
    var element=document.getElementById('popup-bg');
    var loading=document.getElementById('buttonload');
    loading.style.display = "block";
    setTimeout(() => {
        element.style.display = "block";
    }, 3000);
}
