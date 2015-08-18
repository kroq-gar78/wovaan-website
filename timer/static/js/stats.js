var timesData, chart;
$(document).ready(function(){
  $.ajax({
    type: "POST",
    url: "/timer/getjsontimesdata/",
    contentType: "application/json",
    success: function(result)
    {
      timesData = result;
      $.each(timesData, function(i, item){
        timesData[i].duration = parseFloat(item.duration);
        timesData[i].date = new Date(item.date);
      })
      console.log(JSON.stringify(timesData));
      chart = AmCharts.makeChart("chartdiv", {
          "type": "serial",
          "theme": "dark",
          "valueAxes": [{
              "id": "v1",
              "axisAlpha": 0,
              "position": "left"
          }],
          "dataDateFormat" : "YYYY-MM-DD HH:MM:SS.QQQ",
          "balloon": {
              "borderThickness": 1,
              "shadowAlpha": 0
          },
          "graphs": [{
              "id": "g1",
              "bullet": "round",
              "bulletBorderAlpha": 1,
              "bulletColor": "#FFFFFF",
              "bulletSize": 5,
              "hideBulletsCount": 50,
              "lineThickness": 2,
              "title": "red line",
              "useLineColorForBulletBorder": true,
              "valueField": "duration",
              "balloonText": "<div style='margin:5px; font-size:19px;'>[[value]]</div>"
          }],
          "chartScrollbar": {
              "graph": "g1",
              "oppositeAxis":false,
              "offset":30,
              "scrollbarHeight": 80,
              "backgroundAlpha": 0,
              "selectedBackgroundAlpha": 0.1,
              "selectedBackgroundColor": "#888888",
              "graphFillAlpha": 0,
              "graphLineAlpha": 0.5,
              "selectedGraphFillAlpha": 0,
              "selectedGraphLineAlpha": 1,
              "autoGridCount":true,
              "color":"#AAAAAA"
          },
          "chartCursor": {
              "pan": true,
              "valueLineEnabled": true,
              "valueLineBalloonEnabled": true,
              "cursorAlpha":0,
              "valueLineAlpha":0.2
          },
          "categoryField": "date",
          "categoryAxis": {
              "parseDates": true,
              "dashLength": 1,
              "minorGridEnabled": true,
              "minPeriod": "mm"
          },
          "export": {
              "enabled": true
          },
          "dataProvider" : timesData
      });
      chart.addListener("dataUpdated", zoomChart);
    }
  });
});

// this method is called when chart is first inited as we listen for "dataUpdated" event
function zoomChart() {
    // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
    chart.zoomToIndexes(chartData.length - 250, chartData.length - 100);
}
