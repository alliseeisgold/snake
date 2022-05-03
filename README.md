# [**Snake Game**](https://ru.wikipedia.org/wiki/Snake_(%D0%B8%D0%B3%D1%80%D0%B0))

<p align="center">
  <img width="460" height="300" src="imgs/legendary.jpg" сaption="Легендарная игра" alt="">
</p>





**Description Of the Game**
=====
*In [**wikipedia**](https://ru.wikipedia.org/wiki/Snake_ (%D0%B8%D0%B3%D1%80%D0%B0)) you can find the history and description of the game. 
The snake written by me is a modification of that game. There are several levels instead of one level. The game is divided into three levels: **Easy, Medium and Hard**. When you enter the game, a menu will open to select one of the levels.  
In addition to apples, the snake can eat some other fruit and, depending on what kind of fruit it ate, it gets points. (in my modification there are two kind of fruit: **apple and melon**).
The game will end if the snake bites its body or collides with fences.*

**Patterns**
====
1. **Abstract Factory** - этот паттерн был использован для создания фруктов. Потому что у меня два вида фруктов.

**RUN**
=====

### First download the necessary libraries
    pip install -r requirements.txt

### Run
    python3 main.py
