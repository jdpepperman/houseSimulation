$(document).ready(function () {
    $.ajax({
        url: "output.txt",
        async: false,
        success: function(data) {
            //alert(data)
            drawMap(JSON.parse(data))
        }
    });
});

function drawMap(houseData) {
    alert("Inside function.");

    //Get the dimensions of the house and create an outer div.
    var dimensions = getDimensions(houseData);
    alert(dimensions);
    $("#outer-div").width(200*dimensions[0]).height(200*dimensions[1]).css("border", "solid");

    // var $div = $("<div>", {id: "foo", class: "a"});
    // $div.click(function(){ /* ... */ });
    // $("#box").append($div);
}

function getDimensions(houseData){
    var visitedRooms = [];

    var maxX = 0;
    var minX = 0;
    var maxY = 0;
    var minY = 0;
    var startRoom = Object.keys(houseData)[0];

    function exploreRoom(currentRoom, curX, curY){
        // Updates the maximum and minimum values for x and y.
        if(curX > maxX) maxX = curX;
        if(curX < minX) minX = curX;
        if(curY > maxY) maxY = curY;
        if(curY < minY) minY = curY;

        // Adds location data to the room for later use.
        houseData[currentRoom].locX = curX;
        houseData[currentRoom].locY = curY;
        //TODO use locX and locY to build a map of the rooms.

        // Checks if currentRoom has any connections. Will only be false if the house has only one room.
        if(houseData[currentRoom].hasOwnProperty("Connections")){
            var connections = houseData[currentRoom]["Connections"];

            // Checks if connectionNorth exists
            if(connections.hasOwnProperty("connectionNorth")){
                // Checks if connectionNorth has been visited
                if(visitedRooms.indexOf(connections["connectionNorth"]) == -1){
                    // Explores connectionNorth
                    visitedRooms.push(connections["connectionNorth"]);
                    exploreRoom(connections["connectionNorth"], curX, curY+1);
                }
            }

            // Checks if connectionSouth exists
            if(connections.hasOwnProperty("connectionSouth")){
                // Checks if connectionSouth has been visited
                if(visitedRooms.indexOf(connections["connectionSouth"]) == -1){
                    // Explores connectionSouth
                    visitedRooms.push(connections["connectionSouth"]);
                    exploreRoom(connections["connectionSouth"], curX, curY-1);
                }
            }

            // Checks if connectionEast exists
            if(connections.hasOwnProperty("connectionEast")){
                // Checks if connectionEast has been visited
                if(visitedRooms.indexOf(connections["connectionEast"]) == -1){
                    // Explores connectionEast
                    visitedRooms.push(connections["connectionEast"]);
                    exploreRoom(connections["connectionEast"], curX+1, curY);
                }
            }

            // Checks if connectionWest exists
            if(connections.hasOwnProperty("connectionWest")){
                // Checks if connectionWest has been visited
                if(visitedRooms.indexOf(connections["connectionWest"]) == -1){
                    // Explores connectionWest
                    visitedRooms.push(connections["connectionWest"]);
                    exploreRoom(connections["connectionWest"], curX-1, curY);
                }
            }
        }
    }

    // Begin exploring with startRoom at location (0,0)
    visitedRooms.push(startRoom);
    exploreRoom(startRoom, 0, 0);

    return [(maxX-minX)+1, (maxY-minY)+1];
}