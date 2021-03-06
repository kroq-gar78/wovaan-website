var timeStart,
    timeElapsed,
    timer_status = "initial",
    space_released = true,
    timeInterval,
    nextScramble;

function toMMSSMMMM(milli, sec, min){
  if(sec<10) {sec = "0"+sec;}
  if(min<10) {min = "0"+min;}
  if(milli<10) {milli = "00"+milli;}
  else if(milli<100) {milli = "0"+milli;}

  return (min+":"+sec+"."+milli).split('').join(' ');
}

function timer(){
  timeElapsed = new Date(new Date() - timeStart)
    , minutes = timeElapsed.getUTCMinutes()
    , seconds = timeElapsed.getUTCSeconds()
    , milliseconds = timeElapsed.getUTCMilliseconds();

  $('#timer').text(toMMSSMMMM(milliseconds, seconds, minutes));
}

function setTimer(){
  timeInterval = setInterval(timer, 1);
}

function fetchScramble()
{
  $.ajax({
    type: "POST",
    url: "/timer/updatescramble/",
    datatype: "html",
    data: {"puzzle": puzzle},
    success: function(result)
    {
      nextScramble = result;
    }
  });
}

function postSolve()
{
  var duration = timeElapsed.getUTCMilliseconds()/1000;
  duration += timeElapsed.getUTCSeconds();
  duration += timeElapsed.getUTCMinutes()*60;
  duration = +duration.toFixed(3); // JS hack to fix floating point precision nonsense

  $.ajax({
    type: "POST",
    url: "/timer/addsolve/",
    datatype: "html",
    data: {"puzzle": puzzle,
           "scramble": $("#scramble").text(),
           "duration": duration},
    success: function(result)
    {
      console.log("Sent solve");
    }
  });
  load_from_db();
}

$(document).ready(
function () {
    $(document).bind('keydown', function (e) {
      if(e.keyCode == 32){
          if(timer_status == "started"){
            clearInterval(timeInterval);
            $("#scramble").text(nextScramble);
            fetchScramble();
            postSolve();
            timer_status = "show-time";
            space_released = false; // prevent repeated keydown events
          }
          else if((timer_status == "initial" || timer_status == "show-time") && space_released == true){
            timer_status = "ready";
            $('#timer').css("color", "#00C853");
          }
        }
    });
    $(document).bind('keyup', function(e){
      if(e.keyCode == 32){
        if(timer_status == "ready"){
          timeStart = new Date();
          $('#timer').text(toMMSSMMMM(0, 0, 0));
          timer_status = "started";
          setTimer();
        }
        space_released = true;
        $('#timer').css('color','inherit');
      }
    });

    fetchScramble(); // keep one scramble cached
});
