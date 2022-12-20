var rolLength = 10;
var setNum;
var hiddenInput = document.createElement("input");
hiddenInput.className = "hidden-input";

const rRotate = () => {
  var panel = document.querySelector(".rouletter-wacu");
  var btn = document.querySelector(".rouletter-btn");
  var deg = []; // 인덱스는 0 ~ rolLength-1 반시계 방향으로 이동한다는 것 체크
  for (var i = 1, len = rolLength; i <= len; i++) {
    deg.push((360 / len) * i);
  }

  var num = 0;
  document.body.append(hiddenInput);
  setNum = hiddenInput.value = 2; // 무조건 랜덤상품 나오게 설정

  var ani = setInterval(() => {
    num++;
    panel.style.transform = "rotate(" + 360 * num + "deg)";
    btn.disabled = true; //button,input
    btn.style.pointerEvents = "none"; //a 태그

    if (num === 30) {
      clearInterval(ani);
      panel.style.transform = "rotate(" + deg[setNum] + "deg)";
    }
  }, 50);
};

const rReset = (ele) => {
  setTimeout(() => {
    ele.style.pointerEvents = "auto";
    hiddenInput.remove();
  }, 5500);
};

document.addEventListener("click", function (e) {
  var target = e.target;
  var ele = document.getElementById('ticket');
  var pop = document.getElementById('popup-bg');
  if (target.tagName === "BUTTON") {
    ele.innerText="0"; 
    rRotate();
    rReset(target);
    setTimeout(() => {
        pop.style.display = "block";
    }, 4500);
  }
});

document.getElementById("app").innerHTML = `
<div class="rouletter">
    <div class="rouletter-bg">
        <div class="rouletter-wacu"></div>
    </div>
    <div class="rouletter-arrow"></div>
    <button class="rouletter-btn">start</button>
</div>
`;
