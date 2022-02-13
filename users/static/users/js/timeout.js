
// Dom ile yakaladık set timre out fonkunu kullandık 5 sn sonra message yok olsun die
let element = document.querySelector('.alert');

setTimeout(function () {
  element.style.display = 'none';
}, 5000);
