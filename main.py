import playsound as ps
import numpy as np
import re


class Main_Menu:

  def displayWelcomeMessage():
    print("Thank you so much for your willingness to test our program!! This is a beta build of the HowToStudyKorean Listening Program.")
    print("\nWhile a fancy interface undergoes development, we'll be utilizing the Python console for testing Lessons 7-25.")

class Get_User_Input():
    print("\n-----------------------------------------\n")

    def chooseLesson():
      lesson = int(input("Which lesson would you like to practice? [From Lessons 7 to 25]"))
      while  lesson < 7 or lesson > 25 and lesson != 0:
        print("Only lessons Lessons 7 - 25 are available.")
        lesson = int(input("Which lesson would you like to practice?"))
      return(lesson)

    def limitTheNumberOfPracticeQuestions(ProgrammedLesson):
      numQuestions = len(ProgrammedLesson)
      txt = "There are {} possible questions to respond to."
      print(txt.format(numQuestions))
      limitCond = str(input("Would you like to reduce the number of questions to answer? [Y/N]"))
      if limitCond in ['y', 'Y']:
        newNumQuestions = int(0)
        while newNumQuestions < 1 or newNumQuestions > numQuestions:
          newNumQuestions = int(input(""))
      else:
        newNumQuestions = numQuestions
      return(newNumQuestions)


      # There are currently {} amount of questions in Lesson X. Would you like to choose a smaller amount of questions for this session? numQuestions = input("\nHow many questions would you like to answer?")
    def typeOfQuestions():
      questionType = str("")
      print("\nFinally, what kind of lesson are you hoping to do? [A or B]\n")
      print("[A] KOR --> KOR -------- Type out the Korean from the audio")
      print("[B] KOR --> ENG -------- Translate the Korean audio into English")
      #[C] ENG --> KOR ===== From English Text to Korean Text (includes OPTIONAL Audio playback)
      while questionType != "a" or questionType != "b":
        questionType = str(input("Which lesson? [A or B]"))
        questionType.lower()
        if questionType in ["a", "b"]:
          break
        print("Only choose A or B")
      return(questionType)

#    return(chooseLesson, numQuestions, typeOfQuestions)

class Practice_Format:
  def __init__(self, selectLesson, numQuestions, typeOfQuestions):
    self.selectLesson = selectLesson
    self.numQuestions = numQuestions
    self.typeOfQuestions = typeOfQuestions

class Lesson_Dictionary:
  def __init__(self, korean, english, conjugation):
    self.korean = korean
    self.english = english
    self.conjugation = conjugation

def main():
  Main_Menu.displayWelcomeMessage()
  l = Get_User_Input.chooseLesson()
  print(l)
  t = Get_User_Input.typeOfQuestions()
  print(t)
main()
