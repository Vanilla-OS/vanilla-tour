pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'vanilla_tour'
gnome = import('gnome')

blueprints = custom_target('blueprints',
  input: files(
    'blp/slide.blp',
    'blp/window.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)


python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'vanilla-tour.in',
  output: 'vanilla-tour',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

configure_file(
  input: 'window.in',
  output: 'window.py',
  configuration: conf,
  install: true,
  install_dir: moduledir,
)

gnome.compile_resources('vanilla-tour',
  'vanilla-tour.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  dependencies: [blueprints],
)


vanilla_tour_sources = [
  '__init__.py',
  'main.py',
  'slide.py',
]

install_data(vanilla_tour_sources, install_dir: moduledir)
