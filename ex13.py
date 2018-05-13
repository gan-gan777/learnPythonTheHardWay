# -*- coding:UTF-8 -*-

from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

script, name, age = argv

print "Your information is as follows: "

a = raw_input("What's your name? %s" % name)
b = raw_input("How old are you? %r" % age)

print "The %r will recode %s and %s" % (
	script, name, age)