ymaps.ready(init);

var myMap;

function init () {
    $('#tabs').tabs();
    myMap = new ymaps.Map('tab-2', {
        center: [55.76, 37.64], // Москва
        zoom: 10
    });

    $('#tabs').bind('tabsshow', function (event, ui) {
        myMap.container.fitToViewport();
    });
}
