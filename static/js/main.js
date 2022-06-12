const doc = document;
const menuOpen = doc.querySelector('.menu');
const menuClose = doc.querySelector('.close');
const overlay = doc.querySelector('.overlay');
const allStars = document.querySelectorAll('.star');
const starCount = document.querySelector('.star-count');
const newsDes = document.querySelectorAll('.pro-des');
const rating = document.querySelector('#rate');

menuOpen.addEventListener('click', () => {
  overlay.classList.add('overlay--active');
});

menuClose.addEventListener('click', () => {
  overlay.classList.remove('overlay--active');
});

console.log(allStars);

allStars.forEach((star, i) => {
  star.onclick = function () {
    let current_star_level = i + 1;
    starCount.textContent = `${current_star_level} of 5`;
    rating.setAttribute('value', current_star_level);
    console.log(`value is ${rating.value}`);
    console.log(current_star_level);
    allStars.forEach((star, j) => {
      if (current_star_level >= j + 1) {
        star.innerHTML = '&#9733';
      } else {
        star.innerHTML = '&#9734';
      }
    });
  };
});

for (nt of newsDes) {
  DesContent = nt.textContent;
  console.log(DesContent);
  len = DesContent.length;
  console.log(len);
  if (len > 120) {
    content_dis = DesContent.slice(0, 110);
    nt.innerText = `${content_dis}...`;
    console.log(DesContent);
  }
  console.log(DesContent);
}
