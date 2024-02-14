import io
import re
import platform
from setuptools import setup

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('simple_fts5/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

system = platform.system()
machine = platform.machine()

print(system, machine)

if system == 'Darwin':
  if machine not in ['x86_64', 'arm64']:
    raise Exception("unsupported platform")  
elif system == 'Linux':
  if machine not in ['x86_64']:
    raise Exception("unsupported platform")
#elif system == 'Windows':
else: 
  raise Exception("unsupported platform")

setup(
    name="simple_fts5",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    author="Ray Tam",
    url="https://github.com/theblackcat102/simple-fts5-py",
    project_urls={
        "Issues": "https://github.com/theblackcat102/simple-fts5-py/issues",
        "Changelog": "https://github.com/theblackcat102/simple-fts5-py/releases",
    },
    license="MIT License, Apache License, Version 2.0",
    version=__version__,
    packages=["simple_fts5"],
    package_data={"simple_fts5": ['*.so', '*.dylib', '*.dll', 'binaries/*', 'dict/*']},
    install_requires=[],
    # Adding an Extension makes `pip wheel` believe that this isn't a
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)