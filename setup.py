from setuptools import setup


setup(name='translatify',
      version='1.0',
      description='A fun tool to convert text into different languages using '
                  'Google Translate',
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
