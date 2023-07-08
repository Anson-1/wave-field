// // This example uses a GroundOverlay to place an image on the map
// // showing an antique map of Newark, NJ.
// let historicalOverlay;

// function changeIMG(locateIDX, directionIDX, currentIDX){

//   if(locateIDX == 1){         //  Clear Water Bay
//     var lat_centre = 22.283547; var lng_centre = 114.302780;
//   }else if(locateIDX == 2){   //  Hang Zhou
//     var lat_centre = 29.450138; var lng_centre = 121.987014;
//   }else{                      //  Tai Tam Bay
//     var lat_centre = 22.207199; var lng_centre = 114.228361;
//   }

//   const map = new google.maps.Map(document.getElementById("map"), {
//     zoom: 13,
//     center: { lat: lat_centre, lng: lng_centre },
//     mapTypeId: 'terrain' 
//     });
//     //google.maps.MapTypeId.SATELLITE
//   const imageBounds = {
//     north: 22.25653245833641,
//     south: 22.15312409020326,
//     east: 114.3019137061097, 
//     west: 114.1616601056619,
//   };
  
//   const imageURL_list = [
//     "https://drive.google.com/uc?id=1ryaJevutoGVMik5-cbpHCVoues-dHrzV", // Northerly
//     "https://drive.google.com/uc?id=1HxrCQuPtJaPz9pJThXloDMRA8kslK-Jh", // Northeasterly
//     "https://drive.google.com/uc?id=1J_JqnAmR-Sn2svcavoZoHHpNIhFIKr68", // Easterly
//     "https://drive.google.com/uc?id=1FO9XowoHtaytyqNkdkHom0PuXQ_oAKpY", // Southeasterly
//     "https://drive.google.com/uc?id=186yj8Jxw7tZ6iKPgc08TOv7WzmtVuLx4", // Southerly
//     "https://drive.google.com/uc?id=1q_Fld39WJmjN7DA5zPjiVHGq7fADvY0A", // Southwesterly
//     "https://drive.google.com/uc?id=1prqFBr21c-8eY7MKCYMn2_M9LzrN1KVn", // Westerly
//     "https://drive.google.com/uc?id=17qJgQ6uS5D0rjYUXWw2hayQVwBLEn4oJ", // Northwesterly
//     ]
  
//   const imageURL = imageURL_list[directionIDX]; //currentIDX];
  
//   const groundOverlay = new google.maps.GroundOverlay(imageURL, imageBounds);
//   groundOverlay.setOpacity(0.8); // Set opacity to 50%
//   groundOverlay.setMap(map);

//   //alert(lat_centre + lng_centre );
  
// }

// function initMap(locateIDX) {
 
//   if(locateIDX == 1){         //  Clear Water Bay
//     var lat_centre = 22.283547; var lng_centre = 114.302780;
//   }else if(locateIDX == 2){   //  Hang Zhou
//     var lat_centre = 29.450138; var lng_centre = 121.987014;
//   }else{                      //  Tai Tam Bay
//     var lat_centre = 22.207199; var lng_centre = 114.228361;
//   }

//   const map = new google.maps.Map(document.getElementById("map"), {
//     zoom: 13,
//     center: { lat: lat_centre, lng: lng_centre },
//     mapTypeId: 'terrain' //google.maps.MapTypeId.SATELLITE
//     });
  
//   const CFDBounds = [
//     { lat: 22.24802886612813, lng: 114.2828492026208 },
//     { lat: 22.24802886612813, lng: 114.1921983455725 },
//     { lat: 22.17907932940151, lng: 114.1921983455725 },
//     { lat: 22.17907932940151, lng: 114.2828492026208 },
//     { lat: 22.24802886612813, lng: 114.2828492026208 },
//   ];
//   const CFDPath = new google.maps.Polyline({
//     path: CFDBounds,
//     geodesic: true,
//     strokeColor: "#FF0000",
//     strokeOpacity: 1.0,
//     strokeWeight: 2,
//   });

//   CFDPath.setMap(map);

// }

// window.initMap = initMap;


// This example requires the Visualization library. Include the libraries=visualization
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">
let map, heatmap;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: { lat: 22.283547, lng: 114.302780 },
    mapTypeId: "satellite",
  });
  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map,
  });
  const lineSymbol = {
    path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
  };
  // Create the polyline and add the symbol via the 'icons' property.
  const line = new google.maps.Polyline({
    path: [
      { lat: 22.28347, lng: 114.302389 },
      { lat: 22.28338, lng: 114.303230 },
    ],
    icons: [
      {
        icon: lineSymbol,
        offset: "100%",
      },
    ],
    map: map,
  });
  document
    .getElementById("toggle-heatmap")
    .addEventListener("click", toggleHeatmap);
  document
    .getElementById("change-gradient")
    .addEventListener("click", changeGradient);
  document
    .getElementById("change-opacity")
    .addEventListener("click", changeOpacity);
  document
    .getElementById("change-radius")
    .addEventListener("click", changeRadius);
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  const gradient = [
    "rgba(0, 255, 255, 0)",
    "rgba(0, 255, 255, 1)",
    "rgba(0, 191, 255, 1)",
    "rgba(0, 127, 255, 1)",
    "rgba(0, 63, 255, 1)",
    "rgba(0, 0, 255, 1)",
    "rgba(0, 0, 223, 1)",
    "rgba(0, 0, 191, 1)",
    "rgba(0, 0, 159, 1)",
    "rgba(0, 0, 127, 1)",
    "rgba(63, 0, 91, 1)",
    "rgba(127, 0, 63, 1)",
    "rgba(191, 0, 31, 1)",
    "rgba(255, 0, 0, 1)",
  ];

  heatmap.set("gradient", heatmap.get("gradient") ? null : gradient);
}

function changeRadius() {
  heatmap.set("radius", heatmap.get("radius") ? null : 20);
}

function changeOpacity() {
  heatmap.set("opacity", heatmap.get("opacity") ? null : 0.2);
}

// Heatmap data: 500 Points
function getPoints() {
  return [
    new google.maps.LatLng(22.1778, 114.19),
    new google.maps.LatLng(22.283433, 114.302620),
    new google.maps.LatLng(22.283343, 114.302521),
    new google.maps.LatLng(22.283234, 114.302412),
    new google.maps.LatLng(22.283134, 114.302341),
    new google.maps.LatLng(22.283012, 114.302214),
  ];
}

window.initMap = initMap;