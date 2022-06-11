const doc = document;
const menuOpen = doc.querySelector('.menu');
const menuClose = doc.querySelector('.close');
const overlay = doc.querySelector('.overlay');
const allStars = document.querySelectorAll('.star');
const starCount = document.querySelector('.star-count');
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
