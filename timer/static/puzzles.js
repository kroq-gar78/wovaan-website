$(document).ready(
function () {
  $('.type').click(animateOut);
  $('.types').click(function(){animateIn($(this).text())});
});

function animateOut(){
  if($('.type').css('opacity')!='0'){
    $('.type').animate({top:'175px',opacity:'0'},{queue:false});
    $('.types').animate({opacity:'1',height:'toggle'},{queue:false});
  }
}

function animateIn(text){
  if($('.type').css('opacity')!='1'){
    puzzle=text.replace("[","").replace("]","");
    $('.type').text(text.replace("[","(").replace("]",")"));
    $('.type').animate({opacity:'1'},{queue:false});
    $('.types').animate({top:'175px',opacity:'0',height:'toggle'},{queue:false});
  }
}
