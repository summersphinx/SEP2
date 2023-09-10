import os
import spotipy
from rich import print
import imageio.v3 as iio
from PIL import Image


class NoURI(Exception):
    pass
    # print("[bold red] Did not recieve any URI or URL!!![/bold red]")

class ToPNG:

    def __init__(self, sp, uri = None, url = None, image_size = None, name = None, path=None):
        """

        :param sp: The Spotipy Object. Needed to get the playlist image.
        :type sp: <spotipy.client.Spotipy object>
        :param uri: The URI of the playlist. If a list is given, it will recursivly go throught the list.
        :type uri: str | list | None
        :param url: The URL of the playlist. If URI is given, the URI will be used.
        :type url: str | list | None
        :param image_size: Resizes the image to the given int.
        :type image_size: int | None
        :param name: The desired name of the file. If blank, then the ID will be used. DO NOT ADD THE EXTENSION(.png)!
        :type name: str | None
        :param path: The desired path of the file. If blank, the current path will be used. DO NOT INCLUDE NAME IN PATH!
        :type path: str | None
        """

        #       Get the Playlist information.
        try:
            if uri != None:
                if type(uri) is list:
                    for i in uri:
                        ToPNG(sp, uri=i, image_size=image_size, name=name, path=path)
                playlist = sp.playlist(uri)
            elif url != None:
                if type(url) is list:
                    for i in url:
                        ToPNG(sp, url=i, image_size=image_size, name=name, path=path)
                playlist = sp.playlist(url)
            else:
                raise NoURI
        except:
            pass

        #       Get the name of the file
        if name == None:
            name = playlist['id']
        if path == None:
            path = name + '.png'
        else:
            if path[-1] == '/' or path[-2:] == '\\':
                pass
            else:
                path = path + '/'
            path = path + name + '.png'

        iio.imwrite(path, iio.imread(playlist['images'][0]['url'], index=None), extension='.png')
        if image_size != None:
            Image.open(path, 'r').resize((image_size, image_size)).save(path)

        self.name = path
        self.size = image_size


class User:

    def __init__(self):
        pass
