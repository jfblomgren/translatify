from setuptools import setup

def get_readme():
    with open('README.rst', encoding='UTF-8') as readme:
        return readme.read()


setup(name='translatify',
      version='1.0.1',
      description='A fun tool to convert text into different languages using '
                  'Google Translate',
      long_description=get_readme(),
      license='MIT',
      author='Encrylize',
      author_email='encrylize@gmail.com',
      url='https://github.com/Encrylize/translatify',
      keywords=['translatify', 'google-translate', 'translate'],
      classifiers=['License :: OSI Approved :: MIT License',
                   'Topic :: Utilities',
                   'Topic :: Games/Entertainment',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Other Audience',
                   'Development Status :: 4 - Beta',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Natural Language :: English'],
      install_requires=['googletrans'],
      packages=['translatify'],
      entry_points='''
          [console_scripts]
          translatify=translatify.translatify:main
      ''')
