import os


def builder_inited(app):
    theme_dir = os.path.join(os.path.dirname(__file__), 'theme')
    app.info('Using openstack theme from %s' % theme_dir)
    # Insert our theme directory at the front of the search path and
    # force the theme setting to use the one in the package. This is
    # done here, instead of in setup(), because conf.py is read after
    # setup() runs, so if the conf contains these values the user
    # values overwrite these. That's not bad for the theme, but it
    # breaks the search path.
    app.config.html_theme_path.insert(0, theme_dir)
    # Set the theme name
    app.config.html_theme = 'openstack'
    # Re-initialize the builder, if it has the method for setting up
    # the templates and theme.
    if hasattr(app.builder, 'init_templates'):
        app.builder.init_templates()


def setup(app):
    app.connect('builder-inited', builder_inited)
