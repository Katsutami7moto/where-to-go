from django.shortcuts import render
from places.models import Place

moscow_legends = Place.objects.get(place_id='moscow_legends')
roofs24 = Place.objects.get(place_id='roofs24')

places = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [moscow_legends.longitude,
                                moscow_legends.latitude]
            },
            "properties": {
                "title": moscow_legends.title,
                "place_id": moscow_legends.place_id,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [roofs24.longitude,
                                roofs24.latitude]
            },
            "properties": {
                "title": roofs24.title,
                "place_id": roofs24.place_id,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
            }
        }
    ]
}


def start(request):
    return render(request, 'start.html', {'places_geojson': places})
