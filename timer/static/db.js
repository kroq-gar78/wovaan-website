var currentTimes;
function load_from_db(){
  $.ajax({
    type: "POST",
    url: "/timer/gettimes/",
    datatype: "html",
    data: {"puzzle": puzzle},
    success: function(result)
    {
      $('.times-list').html(result);
      //console.log(result);
    }
  });
}

load_from_db();
