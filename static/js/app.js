const eliminar = document.querySelector('.js-eliminar');
eliminar.addEventListener('click', ()=>{
  var confirma = confirm("¿Estas Seguro de Eliminar?");
  if (confirma){
    e.click();
  }
  if (!confirma){
    e.preventDefault
  } // true if OK is pressed
})