# otp-scheduler


I'll fill this out in much more detail when there's a bit more progress.


For now, 
```sh
# manage your requirements however you want. I'm using pyenv-virtualenv
pip install -r requirements.txt

# this only prints out dataframes of your CSV files for now
python main.py --c 1000 --restaurants examples/boston/20200405/restaurants.csv --hospitals examples/boston/20200405/hospitals.csv
```

The more-interesting stuff is in the [notebook](/src/notebooks/Sandbox.ipynb), if you want to play around there!
