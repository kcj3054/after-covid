function initMap() {
    $.ajax({
        type: "get",
        url: "/get_venues",
        data: {},
        success: function (response) {
            let location = response['pac_input']
            for (let i =0; i <location.length; i++){
                let lat = location[i]['latitude']
                let lon = location[i]['longitude']

                shawMap(lat, lon);
                $("#container").show();
            }
        }
    })
}
function shawMap(lat, lon) {
    const pyrmont = {lat: +lat, lng: +lon};
    const map = new google.maps.Map(document.getElementById("map"), {
        center: pyrmont,
        zoom: 17,
        mapId: "8d193001f940fde3",
    });

    // Create the places service.
    const service = new google.maps.places.PlacesService(map);
    let getNextPage;
    const moreButton = document.getElementById("more");

    moreButton.onclick = function () {
        moreButton.disabled = true;
        if (getNextPage) {
            getNextPage();
        }
    };

    // Perform a nearby search.
    $('#places').empty()
    service.nearbySearch(
        {location: pyrmont, radius: 500, type: "store"},
        (results, status, pagination) => {
            if (status !== "OK" || !results) return;

            addPlaces(results, map);
            moreButton.disabled = !pagination || !pagination.hasNextPage;
            if (pagination && pagination.hasNextPage) {
                getNextPage = () => {
                    // Note: nextPage will call the same handler function as the initial call
                    pagination.nextPage();
                };
            }
        }
    );
}

function addPlaces(places, map) {
    const infowindow = new google.maps.InfoWindow();
    const placesList = document.getElementById("places");
    for (const place of places) {
        if (place.geometry && place.geometry.location) {
            const image = {
                url: place.icon,
                size: new google.maps.Size(71, 71),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(25, 25),
            };

            const marker = new google.maps.Marker({
                map,
                icon: image,
                title: place.name,
                position: place.geometry.location,
            });

            google.maps.event.addListener(marker, "click", () => {
                const content = document.createElement("div");
                const nameElement = document.createElement("h2");

                nameElement.textContent = place.name;
                content.appendChild(nameElement);

                const placeIdElement = document.createElement("a");

                placeIdElement.textContent = "구글맵스에서 보기"
                content.appendChild(placeIdElement);

                const link = document.createTextNode("");

                placeIdElement.appendChild(link);

                placeIdElement.title = "This is Link";
                placeIdElement.href = "http://www.google.com/maps/place/?q=place_id:" + place.place_id;
                placeIdElement.id = "placeId"

                content.appendChild(placeIdElement);

                const placeAddressElement = document.createElement("p");

                placeAddressElement.textContent = place.formatted_address;
                content.appendChild(placeAddressElement);
                infowindow.setContent(content);
                infowindow.open(map, marker);

                const bookmarkElement = document.createElement("button");

                bookmarkElement.textContent = "Bookmark";
                content.appendChild(bookmarkElement);

                const text = document.createTextNode("");

                bookmarkElement.appendChild(text);

                bookmarkElement.id = "Bookmark"

                function save_venues() {

                    let url = placeIdElement.href

                    $.ajax({
                        type: "POST",
                        url: "/save_venues",
                        data: {url_give: url},
                        success: function (response) {
                            // 성공하면
                            return response
                            console.log(response["msg"])
                            alert(response["msg"]);
                        }
                    })

                }

                bookmarkElement.onclick = save_venues()

            });



            const li = document.createElement("li");

            li.textContent = place.name;
            placesList.appendChild(li);
            li.addEventListener("click", () => {
                map.setCenter(place.geometry.location);
            });
        }
    }
}

function sign_out() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!')
    window.location.href = "/login"
}
