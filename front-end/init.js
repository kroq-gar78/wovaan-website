var milliseconds = 0,
    seconds = 0,
    minutes = 0,
    start = "off",
    timeInterval;


function toMMSSMMMM(milli, sec, min){
  if(sec<10) {sec = "0"+sec;}
  if(min<10) {min = "0"+min;}
  if(milli<10) {milli = "00"+milli;}
  else if (milli<100) {milli = "0"+milli;}

  return min+":"+sec+":"+milli;
}

function timer(){
  milliseconds++;
  if(milliseconds>=1000){
    milliseconds=0;
    seconds++;
    if(seconds>=60){
      seconds=0;
      minutes++;
    }
  }

  $('#timer').text(toMMSSMMMM(milliseconds, seconds, minutes));
  setTimer();
}

function setTimer(){
  timeInterval = setTimeout(timer, 1);
}

$(document).ready(
function () {
    $(document).bind('keydown', 'space', function () {
        if(start == "started"){
          clearTimeout(timeInterval);
          start = "off";
          return;
        }
        if(start == "off"){
          start = "held";
          return;
        }
    });
    $(document).bind('keyup', 'space', function(){
      if(start == "held"){
        minutes = 0;
        seconds = 0;
        milliseconds = 0;
        $('#timer').text(toMMSSMMMM(milliseconds, seconds, minutes));
        start = "started";
        setTimer();
        return;
      }
    });
});
