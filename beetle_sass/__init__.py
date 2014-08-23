import sass


def render_sass(raw_content):
    return sass.compile(string=raw_content)


def register(plugin_config, config, commander, builder, content_renderer):
    sass_extensions = ['sass', 'scss']
    content_renderer.add_renderer(sass_extensions, render_sass)
