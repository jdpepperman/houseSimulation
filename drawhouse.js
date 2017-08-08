$(document).ready(function () {
    $.ajax({
        url: "output.txt",
        async: false,
        success: function(data) {
            alert(data)
            //drawMap(JSON.parse(data))
        }
    });
});

// function drawMap(houseData) {
//     alert("Inside function.");
//
//     //Get the dimensions of the house.
//     var dimensions = getDimensions(houseData);
//
//     $("#outer-div").attr({ "width" : 100*dimensions[0], "height" : 100*dimensions[1] });
//
//     var $div = $("<div>", {id: "foo", class: "a"});
//     $div.click(function(){ /* ... */ });
//     $("#box").append($div);
// }
//
// function getDimensions(houseData){
//     // var visitedRooms = [];
//     //
//     // var curX, maxX, minX, curY, maxY, minY = 0;
//     // for(var key in houseData) {
//     //     if(key in visitedRooms) continue;
//     //
//     //
//     // }
//
//     return [1,1];
// }