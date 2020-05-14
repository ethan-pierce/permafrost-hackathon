# Installation steps for Ku and Landlab
## Permamodel setup
1. Make a new directory for the hackthon
2. In this directory, clone the permamodel repository: https://github.com/permamodel/permamodel.
    - Open the link in a web browser
    - Click the green `Clone or download` button
    - Copy the link
    - Open a Terminal window
    - Navigate to your hackathon directory
    - Type `git clone X`, where `X` is the copied link
    - Press Enter
    - This should make a new subfolder called `permamodel`
3. Make three additional subfolders in the main directory:
    - data/
    - inputs/
    - outputs/

## Anaconda installation
The Ku model is developed for Python 2.x, while Landlab and the majority of the scientific computing ecosystem has moved to Python 3.x. Because of this, we will need two different Anaconda "environments": groups of packages, including Python itself, that are kept separately from one another. This will allow us to switch back and forth between major versions of Python as necessary.

If you do not already have an Anaconda installation, go to [this link](https://docs.anaconda.com/anaconda/install/) and follow the instructions. 

In addition to base Python, we will need a few extra packages. First, for Python 2:
1. Open a Terminal
2. Type `conda create --name MYENV python=2.7`, where `MYENV` is whatever you would like to name the new environment.
3. Press Enter
4. Type `y` and then Enter.
5. Type `conda activate MYENV` and press Enter
6. Type `conda install jupyter jupyterlab matplotlib netcdf4 Basemap`
7. Press Enter, then type `y` and press Enter
8. Type `jupyter-lab` to open a new Jupyter notebook!

Then, for Python 3:
1. Open a Terminal
2. Type `conda create --name MYENV2`, where `MYENV2` is a different name than whatever you used above. 
3. Press Enter
4. Type `y` and then Enter.
5. Type `conda activate MYENV2` and press Enter
6. Type `conda install jupyter jupyterlab matplotlib rasterio netcdf4`
7. Press Enter, then type `y` and press Enter
8. Type `conda install -c conda-forge landlab`
9. Press Enter, then type `y` and press Enter
10. Type `jupyter-lab` to open a new Jupyter notebook!

Important note: you can have two Jupyter lab instances running simultaneously. Just use a new Terminal window for each one, and activate the appropriate conda environment before launching Jupyter.

Depending on how your default browser is configured, Jupyter might not launch automatically. If this happens to you, copy & paste the link from your Terminal window into a new browser tab. (The link will start with http://localhost ...)

If you are new to using Anaconda, I highly recommend [this cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).

## Check that things work
There are two Python scripts in the setup/ folder in this repository. Download both to your main hackathon folder. There is also a configuration file, called `ku-hackathon-test.cfg`. Download this to your inputs/ directory. 

To test your Ku installation:
1. Open a Terminal window and navigate to your hackathon folder
2. Type `conda activate X`, where `X` is the name of your Python 2 environment.
3. Press Enter.
4. Type `python `test-ku-for-hackathon.py`
5. Press Enter

To test your Python 3 installation:
1. Open a Terminal window and navigate to your hackathon folder
2. Type `conda activate X`, where `X` is the name of your Python 3 environment.
3. Press Enter.
4. Type `python `test-packages-for-hackathon.py`
5. Press Enter

If everything runs without errors, you are good to go! If you run into problems, send an email to ethan.pierce@colorado.edu and I'll do my best to help troubleshoot.

## Sharing materials with GitHub
Feel free to use this repository to host presentations, Jupyter notebooks, notes, or anything else you would like to share. To do so:

1. Fork the repository:
   - Navigate to https://github.com/ethan-pierce/permafrost-hackathon
   - In the top-right corner, click `Fork`

2. Set up a local clone:
    - Navigate to your forked repository
    - Click the green `Clone or download` button
    - Copy the link
    - Open a Terminal window
    - Navigate to a folder where you would like to create a local copy of the repo
    - Type `git clone X`, where `X` is the link
    - Press Enter

3.  Sync your cloned repository
    - Navigate to your local copy of the repo
    - Type `git remote add upstream X`, where `X` is the link from step 2

4. Keep the repositories in sync with these commands:
    - `git fetch upstream` grabs the most up-to-date copy of the parent repo
    - `git checkout master` switches to your local `master` branch
    - `git merge upstream/master` merges any changes in the parent repo to your local copy

5. Add materials
    - Add anything to your local repository
    - In a web browser, go to https://github.com/ethan-pierce/permafrost-hackathon
    - On the left, click `New pull request`
    - Select your repo as the source, and the parent repo as the destination
    - Add ethan.pierce@colorado.edu to the "Reviewers" list (this will send me an email notification)

Alternatively, feel free to email materials to ethan.pierce@colorado.edu, and I will be happy to add them for you.
