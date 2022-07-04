# Simple notification prompt
A simple js script which allows you to notify your users using notification prompts!

<p align="center">
  <img src="https://raw.githubusercontent.com/leothewolf/notifications/main/notify.gif" />
</p>


# How to use?

**First**, include the files : 

- **Method 1** is to download this repo and include ``notify.js`` and ``notify.css`` into your project file. <br><br>``<link rel="stylesheet" href="notify.css">``<br>``<script src="notify.js"></script>``

<br>

- **Method 2** is to use directly from github. Add following lines to your project : <br><br> ``<link rel="stylesheet" href="https://raw.githubusercontent.com/leothewolf/notifications/main/notify.css">``<br>``<script src="https://raw.githubusercontent.com/leothewolf/notifications/main/notify.js"></script>``

Don't forget to include to **jQuery**.

<br>

Once you have done all the above things create a div with class ``notify-container`` in the body of the HTML of your project.

```
<div class="notify-container"></div>
```
<br>

Next, to create a red notification prompt add following to ``<script></script>`` tag:
```
notifyAdd("red","content")
```
<br>
There you go! It will be added you can even use the same function to create prompts on button click or any other events!

<br><br>

# Prompt's options

General form of ``notifyAdd()`` is:<br><br>
```notifyAdd(type,content,[time])```

**Type** can be either red,green or yellow --> depecting the color of the prompt

**Content** can be either HTML or some text! (Take care there are no single quotes in the HTML)

**Time** (this is not compulsary and default is 3000ms) you can change by specifying it according to your needs!
