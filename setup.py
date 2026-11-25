import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()

with open('requirements.txt', encoding='utf-8') as f:
    required = f.read().splitlines()

   
setuptools.setup(
    name='facelib',
    version='1.6.1',
    author="Sajjad Ayoubi",
    author_email="sadeveloper360@gmail.com",
    description="Face Detection & Age Gender & Expression & Recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maximedrn/facelib",
    install_requires=required,
    packages=setuptools.find_packages(),
    package_data={
        "facelib.Retinaface": ["weights/*.pth"],
        "facelib.AgeGender": ["weights/*.pth"],
        "facelib.FacialExpression": ["weights/*.pth"],
        "facelib.InsightFace.models": ["weights/*.pth"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
