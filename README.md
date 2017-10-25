# Animation

[![Build Status](https://travis-ci.org/Caulidata/Animation.svg?branch=master)](https://travis-ci.org/Caulidata/Animation)

> This project is decoupled from the [Bangumi](https://github.com/wolther47/Bangumi) project by [@Wolther47](https://github.com/wolther47)

This README is also available in [简体中文](https://github.com/Caulidata/Animation/blob/master/README-zh_CN.md)

**All the JSON files are placed under the [Resources](https://github.com/Caulidata/Animation/tree/resources) branch.**

This is a simple project, aiming at scrabbling the bangumi info (since 2009) from Wikipedia and saving them as JSON files.

## TODO

- [ ] ~~Use Wikitables extracting tables~~
- [ ] ~~Convert traditional chinese to simplified one~~
- [ ] ~~Match template Regex~~
- [x] Finish the main function
  - [x] Extract the table
  - [x] Get every single row data
  - [x] Extract text out of each tag
- [x] Continuous intergration
- [ ] ~~Auto release~~
  - [ ] ~~Auto jump to the release page~~
- [x] Run as a routine

## Note

At first, I got into a wrong way. By using the API of MediaWiki, I found:

1. The API seems not to provide the simplified chinese, but only the traditional one;
2. After solving this problem by using OpenCC project, I found the table extracted sometimes has the templates nested into the text, which is used to tell the wikipedia which chinese character to use for different users. This part is pretty hard to match with regex or define it formally, since the maintainers didn't follow what template they should use on their guidelines.

So finally, on the second day, I turn to write a crawler directly parsing the wiki page with the bs4.

## License

All the stored JSON files, are licensed under the same license as they should be on the Wikipedia with [CC BY-SA 3.0 License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License).