from rest_framework.decorators import api_view
from django.http import HttpResponse, FileResponse
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


@api_view(['POST'])
def export(request):
    data_json = request.data
    print(data_json)

    data = ET.Element('release')
    ET.SubElement(data, 'aggregatorName').text = str(data_json['aggregatorName'])
    ET.SubElement(data, 'labelName').text = str(data_json['labelName'])
    ET.SubElement(data, 'UPC_EAN').text = str(data_json['UPC_EAN'])
    ET.SubElement(data, 'catalogNumber').text = str(data_json['catalogNumber'])
    ET.SubElement(data, 'coverArtFilename').text = str(data_json['coverArtFilename'])
    ET.SubElement(data, 'releaseTitle').text = str(data_json['releaseTitle'])
    ET.SubElement(data, 'releaseSalesType').text = str(data_json['releaseSalesType'])

    tracks = ET.SubElement(data, 'tracks')
    for i in range(len(data_json['tracks'])):
        track = ET.SubElement(tracks, 'track')
        ET.SubElement(track, 'albumOnly').text = str(data_json['tracks'][i]['albumOnly'])
        ET.SubElement(track, 'trackNumber').text = str(data_json['tracks'][i]['trackNumber'])
        ET.SubElement(track, 'trackPublisher').text = str(data_json['tracks'][i]['trackPublisher'])
        ET.SubElement(track, 'trackTitle').text = str(data_json['tracks'][i]['trackTitle'])
        ET.SubElement(track, 'trackMixVersion').text = str(data_json['tracks'][i]['trackMixVersion'])
        ET.SubElement(track, 'originalReleaseDate').text = str(data_json['tracks'][i]['originalReleaseDate'])
        exc = ET.SubElement(track, 'beatportExclusive')
        ET.SubElement(exc, 'exclusivePeriod').text = str(data_json['tracks'][i]['exclusivePeriod'])
        artist = ET.SubElement(track, 'trackArtists')
        for a in range(len(data_json['tracks'][i]['trackArtists'])):
            ET.SubElement(artist, 'artistName').text = str(data_json['tracks'][i]['trackArtists'][a]['artistName'])
        remixers = ET.SubElement(track, 'trackRemixers')
        for r in range(len(data_json['tracks'][i]['trackRemixers'])):
            ET.SubElement(remixers, 'remixerName').text = str(data_json['tracks'][i]['trackRemixers'][r]['remixerName'])
        audio = ET.SubElement(track, 'trackAudioFile')
        ET.SubElement(audio, 'audioFilename').text = str(data_json['tracks'][i]['audioFilename'])
        country = ET.SubElement(track, 'countriesAvailable')
        ET.SubElement(country, 'country').text = str(data_json['tracks'][i]['country'])
        ET.SubElement(track, 'trackGenre').text = str(data_json['tracks'][i]['trackGenre'])
        ET.SubElement(track, 'trackCopyright').text = str(data_json['tracks'][i]['trackCopyright'])
        songwriters = ET.SubElement(track, 'songwriters')
        for s in range(len(data_json['tracks'][i]['songwriters'])):
            songwriter = ET.SubElement(songwriters, 'songwriter')
            ET.SubElement(songwriter, 'name').text = str(data_json['tracks'][i]['songwriters'][s]['name'])
            ET.SubElement(songwriter, 'type').text = str(data_json['tracks'][i]['songwriters'][s]['type'])

    with open("GFG.xml", "wb") as f:
        pretty_xml = minidom.parseString(ET.tostring(data))
        f.write(pretty_xml.toprettyxml(encoding='utf-8'))

    return FileResponse(open('GFG.xml', 'rb'))
