import os
import platform
try:
    import distro  # You might need to install this package using pip install distro
    linux_distribution = distro.id()
except ImportError:
    linux_distribution = None

__version__ = '0.0.1'

def select_binary():
    system = platform.system().lower()
    arch = platform.machine().lower()

    # Mapping for architecture
    arch_map = {
        'x86_64': 'x64',
        'amd64': 'x64',
        'arm64': 'aarch64',
        'aarch64': 'aarch64',
        'x86': 'x86'
    }

    # Determine the appropriate binary based on OS and architecture
    if system == 'linux':
        if 'ubuntu' in platform.version().lower():
            binary = "libsimple.so"
        else:
            binary = "libsimple_aarch64.so"
    elif system == 'darwin':
        return "libsimple.dylib"
    elif system == 'windows':
        arch_suffix = arch_map.get(arch, 'x64')
        binary = f"simple_{arch_suffix}.dll"
    else:
        raise Exception(f"Unsupported system: {system}")

    return binary


def binary_loadable_path():
  loadable_path = os.path.join(os.path.dirname(__file__), "binaries", select_binary())
  return os.path.normpath(loadable_path)

def load(conn):
  conn.enable_load_extension(True)
  extension_path = binary_loadable_path()
  # Load the extension
  conn.load_extension(extension_path)
  # disable extension loading
  conn.enable_load_extension(False)