#!/usr/bin/env python3.4
class duration:
  def __init__(self, *args, hours = None, minutes = None, seconds = None):
    self.hours = 0 
    self.minutes = 0
    self.seconds = 0
    if hours != None:
      self.hours = hours
    if minutes != None:
      self.minutes = minutes
    if seconds != None:
      self.seconds = seconds
    if len(args) > 0:
      self.hours = args[0]
  def __str__(self):
    return ('0' if self.hours < 10 else '') + str(self.hours) + ":" + ('0' if self.minutes < 10 else '') + str(self.minutes) + ":" + ('0' if self.seconds < 10 else '') + str(self.seconds)   
  def setDuration(self, *args, hours = None, minutes = None, seconds = None):
    if hours != None:
      self.hours = hours
    if minutes != None:
      self.minutes = minutes
    if seconds != None:
      self.seconds = seconds
    if len(args) > 0:
      self.hours = args[0]
  def getDuration(self):
    return (3600 * self.hours) + (60 * self.minutes) + (60 * self.seconds)

c=duration(4) 
