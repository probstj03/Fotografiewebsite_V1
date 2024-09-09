window.onscroll = function () { scrollFunctionNavbar() };

document.addEventListener("DOMContentLoaded", function () {
  setFavicon();
});

var darkmode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

function setFavicon() {
  if (darkmode) {
    document.querySelector('link[rel="shortcut icon"]').href = "img/favicon_dark.png";
  } else {
    document.querySelector('link[rel="shortcut icon"]').href = "img/favicon_light.png";
  }
}

function scrollFunctionNavbar() {
  const navanchors = Array.from(
    document.getElementsByClassName("navanchor")
  );
  if (darkmode) {
    const navanchors = Array.from(
      document.getElementsByClassName("navanchor")
    );

    if ((document.body.scrollTop > screen.height / 4) * 3 || (document.documentElement.scrollTop > screen.height / 4) * 3) {
      document.getElementById("navbar").style.boxShadow = "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)";
      document.getElementById("navbar").style.backgroundColor = "#151515";
    } else {
      document.getElementById("navbar").style.boxShadow = "0 0 #00000000";
      document.getElementById("navbar").style.backgroundColor = "#00000000";
    }
  } else {
    if ((document.body.scrollTop > screen.height / 4) * 3 || (document.documentElement.scrollTop > screen.height / 4) * 3) {
      document.getElementById("navbar").style.backgroundColor = "white";
      document.getElementById("navbar").style.boxShadow = "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)";
      document.getElementById("headergrafik").style.filter = "invert(0%)";
      navanchors.forEach(navanchor => { navanchor.style.color = 'black'; });
    } else {
      document.getElementById("navbar").style.boxShadow = "0 0 #00000000";
      document.getElementById("navbar").style.backgroundColor = "#ffffff00";
      document.getElementById("headergrafik").style.filter = "invert(100%)";
      navanchors.forEach(navanchor => { navanchor.style.color = 'white'; });
    }
  }
}

function openNav() {
  document.getElementById("navlinks").style.width = "100%";
}

function closeNav() {
  document.getElementById("navlinks").style.width = "0%";
}

function mouseOverBurger() {
  const burgerLines = Array.from(
    document.getElementsByClassName("line")
  );
  burgerLines.forEach(burgerLines => { burgerLines.style.filter = "invert(50%)"; });
}

function mouseOutBurger() {
  const burgerLines = Array.from(
    document.getElementsByClassName("line")
  );
  burgerLines.forEach(burgerLines => { burgerLines.style.filter = "invert(0%)"; });
}

function moveGalery(name){
  galery = document.getElementById(name);

  if (galery.classList.contains("opened")) {
    galery.style.height = "100px";
    document.getElementById(name+"_arrow").style.rotate = "45deg";
    galery.classList.toggle("opened")
  } else {
    galery.style.height = "100%";
    document.getElementById(name+"_arrow").style.rotate = "225deg";
    galery.classList.toggle("opened")
  }
}

function calculateAge(birthDate) {
  const today = new Date();
  const birth = new Date(birthDate);
  
  let age = today.getFullYear() - birth.getFullYear();
  const monthDifference = today.getMonth() - birth.getMonth();
  
  if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birth.getDate())) {
      age--;
  }
  
  return age;
}

document.addEventListener('DOMContentLoaded', function() {
  const birthDate = '2000-10-03';  
  const age = calculateAge(birthDate);
  document.getElementById('age').textContent = age;
});