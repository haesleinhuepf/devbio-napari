# Constructing an installer

Using [constructor](https://github.com/conda/constructor) we can build operating-system specific installers like this:

```
# make conda use libmamba to solve environments otherwise constructor takes hours
conda install -n base conda-libmamba-solver
conda config --set solver libmamba

# install constructor (preferrably into a new environment)
mamba install constructor
```

now clone this repository and from within the main directory of the repository

create the devbio-napari installer for windows (on a windows computer)

```
constructor installer\Win
```

alternatively, create the devbio-napari installer for Mac OS (on a Mac)

```
constructor installer/Mac
```