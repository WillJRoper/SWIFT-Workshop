# SWIFT-Workshop

This repo contains everything you need to work through the workshop. In this workshop, you will:

- Generate toy initial conditions.
- Run full cosmological simulations with gravity, hydrodynamics, star formation, stellar feedback, and black holes (and more).
- Analyse and visualise the simulations.

Below is some initial setup needed to run the notebooks and simulations that make up this workshop. If you have access to an HPC I recommend using it for this workshop but your laptop can definitely be used! If you have any issues with the installation we will be able to sort these out in the workshop so do not fret!

# Set up

Before we can start making galaxies and building universes in your computer we need to get some software and set up an environment. This environment will ensure everything remains self-contained without messing with any of your existing Python installations. Note that we highly recommend using a UNIX-based system (OSX/Linux), Windows users may have a harder time.

## Necessary Software

For this workshop you will need:

- *Git*, you should already have this but if not there are plenty of guides (e.g https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- *Python*, version >3.10 preferable but not necessary but nothing lower than 3.8. If you are still using Python 2 I recommend a good long look in the mirror before righting your wrongs and installing an up-to-date version.
- A suite of Python packages we will cover shortly.
- A *C compiler*, you may already have one (you can check with `which clang` on OSX, `which gcc` on Linux and `where gcc` on Windows) but if not: 
    - On OSX the default compiler is `clang`: this can be installed by running `xcode-select --install` in the terminal after installing Xcode if you don't already have it.
    - On Linux: GCC can be installed by following the guidance for your distro on installing gcc (e.g. https://www.makeuseof.com/how-to-install-c-compiler-linux/).
    - On Windows: I have little experience but it appears the accepted method is installing via MinGW-w64 (e.g. https://www.scaler.com/topics/c/c-compiler-for-windows/).
- *wget*, to download ICs. 

## Installing SWIFT

In addition to the above, to run SWIFT you will need some extra dependencies. These are listed here: https://swift.dur.ac.uk/docs/GettingStarted/compiling_code.html. All can easily be installed via package managers (on OSX I recommend using Homebrew to get them, https://brew.sh/). 

To install SWIFT run `git clone https://github.com/SWIFTSIM/SWIFT` in the terminal in the directory where you want to have SWIFT. Then enter the cloned repo and run (NOTE: see the caveats below for mac users):
```
./autogen.sh
./configure --disable-mpi
make
```
If everything has run successfully you should find an executable has been created in the repo called `swift`. If it has not run smoothly (it quite probably won't have) try running `./configure --help` to see the possible options and review the output of `./configure` if any of the software listed in the dependencies hasn't been found (has `no` next to it in the table) you may need to point to it directly. Again don't worry if this doesn't work flawlessly we can help get things ironed out in the workshop. If this has worked you now have an executable for running gravity simulations!

Note, if this hasn't worked you can still continue with the next steps to setup your Python environment.

### Mac caveats

Due to some issues with clang if you are using OSX you will need some extra configuration arguments. Instead of the above run:
```
./autogen.sh
./configure --disable-mpi --disable-compiler-warnings --disable-doxygen-doc --disable-hand-vec
make
```

## Setting up the Python environment

First off let us collect together all the Python packages we will need in an environment. There are multiple ways to make a Python environment, you may have come across the `conda` method but here we will use `venv`. Don't let this confuse you they are both correct ways but `venv` comes packaged with all Python distributions regardless of how you installed Python.

First, open the terminal and navigate to where you would like to create an environment. It will be stored in a directory when created, it doesn't matter where this directory is.

Next let's make the environment itself by running
```
python -m venv swift-workshop-env
```
in the terminal. This command will create a blank Python environment with no packages inside a directory called `swift-workshop-env`. The name of the environment doesn't matter but it's best to keep it informative.

With the environment made we now need to activate it. This can be done by running
```
source swift-workshop-env/bin/activate
```
in the terminal. You may want to make an alias for this so you don't always have to know this path but it shouldn't matter given the length of this workshop.

Now that the environment is active we need to install the packages we need. There aren't many and all can be installed via the Python package manager `pip`.

First off let's install some simple Python packages for working with arrays, making plots, and working with HDF5 format data. To install there run the following:
```
pip install numpy matplotlib h5py unyt
```

We will also need a SWIFT helper package for interacting with the data and making intial conditions called `swiftsimio` written by Dr Josh Borrow. As before we can install this via pip:
```
pip install swiftsimio
```

Finally, we will need Jupyter Notebooks to interact with the notebooks that make up this workshop.
```
pip install notebook
```

## Cloning this repo

The vast majority of this workshop will be conducted via notebooks in a public GitHub repo. You will need to clone this repo. Navigate to where you want to store the directory and run the following.
```
git clone https://github.com/WillJRoper/SWIFT-Workshop.git
cd SWIFT-Workshop
```

Now we have the repo and are inside it we can start a `jupyter notebook` session and get to work. To begin simply run
```
jupyter notebook
```
on the command line and open `notebooks/Initial_Conditions.ipynb`.
