# Installation instructions

## Anaconda
If you do not already have a Python installation, go to https://docs.anaconda.com/anaconda/install/ and follow their instructions. To run the Ku model notebooks, you will need a working Python 2 installation, along with a few other packages.

1. Create a new conda environment
    - In a Terminal window, type `conda create --name X python=2.7`, where `X` is a name you choose for the environment
    - Then, type `conda activate X` to activate the environment
    - Use `conda list` to check the packages installed in the active environment
    - Use `conda env list` to see all of your conda environments

2. Install a few required packages
    - Make sure to type `conda activate X` to activate your environment
    - To get packages, use `conda install PACKAGE`, where `PACKAGE` is the name of the package you would like to install
    - To run the Ku model notebooks, you will need:
        - `conda install jupyterlab`
        - `conda install matplotlib`
        - `conda install Basemap`
        - `conda install netcdf4`
        - `conda install -c conda-forge landlab`

3. To open a new instance of Jupyter:
    - `conda activate X`, where `X` is the environment you made in step 1
    - `jupyter lab`
    - This *should* open a browser window, unless you are running bash on Windows or haven't configured a default browser
        - You can always manually open a new browser tab and copy-paste the link from your terminal

## Sharing materials
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
