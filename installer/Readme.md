# Constructing an installer

Using [constructor](https://github.com/conda/constructor) we can build operating-system specific installers like this:

```
# make conda use libmamba to solve environments otherwise constructor takes hours
conda install -n base conda-libmamba-solver
conda config --set solver libmamba

# install constructor (preferrably into a new environment)
mamba install constructor
```

create the devbio-napari installer for windows

```
constructor installer\Win
```

alternatively, create the devbio-napari installer for Mac OS

```
constructor installer/Mac
```