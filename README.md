# Tech stack
- [Python 3.7](https://www.python.org/downloads/)
- [Jenkins](http://mirrors.jenkins.io/war-stable/latest/jenkins.war)
- [SQLite 3](https://pypi.org/project/db-sqlite3/)
- [Selenium 3.141](https://pypi.org/project/selenium/)
# General info
Application simulates some kind of regression testing by checking the differences in exchange rates against PLN. Selenium gets data from [this](https://www.x-rates.com/table/?from=PLN&amount=1) site and application parsing it, compares to the last value from database and shows result in console output. Then new data is write to the database for historic results.  

Test can be automated with Jenkins by setting periodically run. It can be done by forking project or cloning to have it locally.
If you choose first case you must add GitHub credentials to Jenkins, configure new project with periodically running like this:
<p align="center">
<img src="https://i.imgur.com/i7IXwdc.png" width=100% />
</p>

And add *Execute Windows batch command* build step as follows:
```
$ python src/main.py
$ git checkout master
$ git add resources/currency_history.db
$ git commit -m "bla bla bla"
$ git push
```
It was supposed to be some kind of regression testing so in the console output you can see something like this:

```
...
CHANGE OCCURED | Currency Brazilian Real, old - 0.727723, new - 0.726066
CHANGE OCCURED | Currency Bruneian Dollar, old - 2.965174, new - 2.962291
CHANGE OCCURED | Currency Bulgarian Lev, old - 2.332242, new - 2.331249
NO CHANGE | Currency Chilean Peso, old - 0.005101, new - 0.005101
CHANGE OCCURED | Currency Chinese Yuan Renminbi, old - 0.592801, new - 0.592211
CHANGE OCCURED | Currency Colombian Peso, old - 0.001083, new - 0.001081
...
```
But basically it allows saving historical data to database.
