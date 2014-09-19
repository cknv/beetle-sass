import sass
import os


def sass_to_css(path):
    __, destination = path.split(os.sep, 1)
    name, __ = os.path.splitext(destination)
    destination = name + '.css'
    with open(path, 'r') as fo:
        return destination, sass.compile(string=fo.read()).encode('utf-8')


def register(context, plugin_config):
    sass_extensions = ['sass', 'scss']
    context.includer.add(sass_extensions, sass_to_css)
