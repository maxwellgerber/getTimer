# getTimer
#### Alpha Version
Python utilities library for getting time inputs from users in CLI Apps as datetime objects.

#### Installation
```
$ pip install getTimer
```
#### Examples
```
>>> date = getTimer.getUserDate()
>>> date 
datetime.date(2016, 2, 12)
>>> date.day
12
```   
getTimer makes it easy to get properly formatted date, time, and datetime python objects from your users in Command Line Interface applications. Users may use either the arrow keys or their numeric keypad to enter data.  
![basic_usage](https://raw.githubusercontent.com/maxwellgerber/getTimer/master/gifs/basic_usage.gif)    
developers using the module can edit the top string, bottom string, and initial time shown to the user   
![customizable](https://raw.githubusercontent.com/maxwellgerber/getTimer/master/gifs/customizable.gif)  
rollover mode can be enabled or disabled as necessary   
![rollover](https://raw.githubusercontent.com/maxwellgerber/getTimer/master/gifs/rollover.gif)  
#### Usage
The module currently contains three functions:  
`getTimer.getUserDate(topString = 'Input your Date', bottomString = 'Press Enter when done', rollover = False, start = None)`  
  * returns a python datetime.date object containing the user's input  
  * topString and bottomString controll text displayed to user  
  * rollover controlls behavior of widget
  * start must be a datetime.date object. Defaults to datetime.date.today()  
 
`getTimer.getUserTime(topString = 'Input your Date', bottomString = 'Press Enter when done', rollover = False, start = None)`   
  * returns a python datetime.time object containing the user's input  
  * topString and bottomString controll text displayed to user  
  * rollover controlls behavior of widget
  * start must be a datetime.time object. Defaults to datetime.time()  
 
`getTimer.getUserDateTime(topString = 'Input your Date', bottomString = 'Press Enter when done', rollover = False, start = None)`   
  * returns a python datetime.datetime object containing the user's input  
  * topString and bottomString controll text displayed to user  
  * rollover controlls behavior of widget
  * start must be a datetime.datetime object. Defaults to datetime.datetime.now()   
 
#### Todo
- [ ] Nicer gifs/documentation
- [ ] 12 hour AM/PM timestamp
- [ ] verbose option (e.g. print month names instead of int)
- [ ] Integration testing?
- [ ] Enable rollover between date and time in getUserDateTime
