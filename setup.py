from setuptools import setup


description = (
    "A django package that allows easy identification of visitors' "
    "browser, operating system and device information (mobile "
    "phone, tablet or has touch capabilities)."
)

setup(
    name="django-useragent",
    version="0.5.0",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    packages=["django_user_agents"],
    url="https://github.com/null-none/django-useragent",
    license="MIT",
    description=description,
    long_description=open("README.rst").read(),
    zip_safe=False,
    include_package_data=True,
    package_data={"": ["README.rst"]},
    install_requires=["django", "user-agents"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
