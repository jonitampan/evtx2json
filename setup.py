import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'evtx2json',
    packages = ['evtx2json'],
    version = '1.0',
    license='MIT',
    description = 'Import Windows EventLogs(.evtx files) to JSON File.',
    author = 'Sida Nala',
    author_email = 'rudukmada@gmail.com',
    url = 'https://github.com/jonitampan/evtx2json',
    download_url = 'https://github.com/jonitampan/evtx2json/archive/master.zip',
    keywords = ['evtx', 'import', 'json'],
    install_requires=[
          'evtx',
          'tqdm',
      ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
  ]
)
