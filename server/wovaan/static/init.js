var timeStart,
    timeCurrent,
    start = "off",
    timeInterval;


function toMMSSMMMM(milli, sec, min){
  if(sec<10) {sec = "0"+sec;}
  if(min<10) {min = "0"+min;}
  if(milli<10) {milli = "00"+milli;}
  else if(milli<100) {milli = "0"+milli;}

  return (min+":"+sec+"."+milli).split('').join(' ');
}

function timer(){
  var timeElapsed = new Date(new Date() - timeStart)
    , minutes = timeElapsed.getUTCMinutes()
    , seconds = timeElapsed.getUTCSeconds()
    , milliseconds = timeElapsed.getUTCMilliseconds()

  $('#timer').text(toMMSSMMMM(milliseconds, seconds, minutes));
}

function setTimer(){
  timeInterval = setInterval(timer, 1);
}

function fetchScramble()
{
  $.ajax({
    type: "POST",
    url: "/updatescramble/",
    datatype: "html",
    data: "",
    success: function(result)
    {
      $("#scramble").html(result);
    }
  });
}

$(document).ready(
function () {
    $(document).bind('keydown', function (e) {
      if(e.keyCode == 32){
          if(start == "started"){
            clearInterval(timeInterval);
            start = "show-time";
            fetchScramble();
            return;
          }
          if(start == "off"){
            start = "held";
            $('#timer').text("Let go to begin");
            return;
          }
          if(start == "show-time"){
            $('#timer').text("Hold Space");
            start = "off";
            return;
          }
        }
    });
    $(document).bind('keyup', function(e){
      if(e.keyCode == 32){
        if(start == "held"){
          timeStart = new Date();
          $('#timer').text(toMMSSMMMM(0, 0, 0));
          start = "started";
          setTimer();
          return;
        }
      }
    });
});
