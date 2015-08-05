var timeStart,
    timeCurrent,
    start = "off",
    timeInterval,
    nextScramble;

// from: https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

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
    url: "/timer/updatescramble/",
    datatype: "html",
    data: "",
    success: function(result)
    {
      nextScramble = result;
    }
  });
}

$(document).ready(
function () {
    $(document).bind('keydown', function (e) {
      if(e.keyCode == 32){
          if(start == "started"){
            clearInterval(timeInterval);
            $("#scramble").text(nextScramble);
            fetchScramble();
            start = "show-time";
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

    fetchScramble(); // keep one scramble cached
});