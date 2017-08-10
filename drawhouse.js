$(document).ready(function () {
    $.ajax({
        url: "output.txt",
        async: false,
        success: function(data) {
            //alert(data)
            drawMap(JSON.parse(data));
        }
    });

    window.setInterval("updateActors()", 1000);
});

function drawMap(houseData) {
    //Get the dimensions of the house and create an outer div.
    createMap(houseData);


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
            if(connections.hasOwnProperty("connection_north")){
                // Checks if connectionNorth has been visited
                if(visitedRooms.indexOf(connections["connection_north"]) == -1){
                    // Explores connectionNorth
                    visitedRooms.push(connections["connection_north"]);
                    exploreRoom(connections["connection_north"], curX, curY-1);
                }
            }

            // Checks if connectionSouth exists
            if(connections.hasOwnProperty("connection_south")){
                // Checks if connectionSouth has been visited
                if(visitedRooms.indexOf(connections["connection_south"]) == -1){
                    // Explores connectionSouth
                    visitedRooms.push(connections["connection_south"]);
                    exploreRoom(connections["connection_south"], curX, curY+1);
                }
            }

            // Checks if connectionEast exists
            if(connections.hasOwnProperty("connection_east")){
                // Checks if connectionEast has been visited
                if(visitedRooms.indexOf(connections["connection_east"]) == -1){
                    // Explores connectionEast
                    visitedRooms.push(connections["connection_east"]);
                    exploreRoom(connections["connection_east"], curX+1, curY);
                }
            }

            // Checks if connectionWest exists
            if(connections.hasOwnProperty("connection_west")){
                // Checks if connectionWest has been visited
                if(visitedRooms.indexOf(connections["connection_west"]) == -1){
                    // Explores connectionWest
                    visitedRooms.push(connections["connection_west"]);
                    exploreRoom(connections["connection_west"], curX-1, curY);
                }
            }
        }
    }

    // Begin exploring with startRoom at location (0,0)
    visitedRooms.push(startRoom);
    exploreRoom(startRoom, 0, 0);

    return [(maxX-minX)+1, (maxY-minY)+1];
}

function createMap(houseData){
    function getRoom(x, y){
        var keys = Object.keys(houseData);
        for(var i = 0; i < keys.length; i++){
            if(houseData[keys[i]].locX == x && houseData[keys[i]].locY == y) return keys[i];
        }

        return null;
    }

    var dimensions = getDimensions(houseData);

    // Keeps the page from shrinking and collapsing the rows.
    $(document.body).css({minWidth : 150*dimensions[0]});

    var $row;
    var $div;
    var $actor;
    for(var y = 0; y < dimensions[1]; y++){
        // Create a row for the grid
        $row = $("<div>", {class: "row"});
        for(var x = 0; x < dimensions[0]; x++){
            // Add space for a room to the row
            $div = $("<div>", {class: "col"});
            $div.attr({x_loc:x, y_loc:y});
            // Checks to see if the grid space is a valid room.
            var roomName = getRoom(x, y);
            if(roomName != null){
                $div.text(roomName);
                $div.addClass("room");
                $div.attr({"id": roomName});
                // Adds an actor to the room if applicable
                if(houseData[roomName].hasOwnProperty("Actors")){
                    $actor = $("<div>", {class: "actor"});
                    $div.append($actor);
                }
            }
            $row.append($div);
        }
        // Add the row to the body of the page.
        $(document.body).append($row);
    }
}

function updateActors(){
    var houseData = null;
    $.ajax({
        url: "output.txt",
        async: false,
        success: function(data) {
            houseData = JSON.parse(data);
        }
    });

    if(houseData == null) return;

    $(".actor").remove();

    var keys = Object.keys(houseData);
    var $room;
    var $actor;
    for(var i = 0; i < keys.length; i++){
        if(houseData[keys[i]].hasOwnProperty("Actors")){
            $room = $("#" + keys[i]);
            $actor = $("<div>", {class: "actor"});
            $room.append($actor);
        }
    }
}