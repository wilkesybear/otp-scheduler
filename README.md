# otp-scheduler

**Python version: 3.8.0**

_I'll fill this out in much more detail when there's a bit more progress._

For setup, all you need to do is install the pip requirements
```sh
# manage your requirements however you want. I'm using pyenv-virtualenv
pip install -r requirements.txt
```

### Notebook
The more-interesting stuff is in the [notebooks folder](/src/notebooks/), if you want to play around there! To run this, install jupyter notebook (it's `notebook` in `requirements.txt`. At the **root** of the project, run

`➜  ~/src/otp-scheduler git:(master) ✗ jupyter notebook`

That should open up a browser console window. Navigate to the notebook file of your choosing, and go!

### Algorithms

The algorithms are in the notebooks folder

#### ortools-scheduler.ipynb
Main contact: @angelwong

Uses constaints-based approach with Google's OR-Tools to find a maximally optimal solution based on defined contraints.

#### greedy.ipynb
Main contact: @wilkesybear

Uses an iterative, "build up" greedy approach that mostly mimics how a human operator would build the schedule, but with no backtracking or adjustments. 
