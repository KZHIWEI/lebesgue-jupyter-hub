from setuptools import setup


version = "1.3.3.dev"


with open("./lebesgueauthenticator/__init__.py", "a") as f:
    f.write("\n__version__ = '{}'\n".format(version))


setup(
    name="jupyterhub-lebesgueauthenticator",
    version=version,
    description="Lebesgue Authenticator for JupyterHub",
    author="Zhiwei Zhang",
    author_email="1010482029@qq.com",
    license="3 Clause BSD",
    packages=["lebesgueauthenticator"],
    install_requires=["jupyterhub", "tornado", "traitlets"],
)