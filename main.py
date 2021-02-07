import playsound as ps
import numpy as np
import re
import importlib
import unit1database


class MainMenu:

  def display_welcome_message():
    print("Thank you so much for your willingness to test our program!! This is a beta build of the HowToStudyKorean Listening Program.")
    print("\nWhile a fancy interface undergoes development, we'll be utilizing the Python console for testing Lessons 7-25.")

class GetUserInput():
    print("\n-----------------------------------------\n")

    def choose_lesson():
      lesson = int(input("Which lesson would you like to practice? [From Lessons 7 to 25]"))
      while  lesson < 7 or lesson > 25 and lesson != 0:
        print("Only lessons Lessons 7 - 25 are available.")
        lesson = int(input("Which lesson would you like to practice?"))
      return(lesson)

    def limit_the_number_of_practice_questions(ProgrammedLesson):
      num_questions = len(ProgrammedLesson)
      txt = "There are {} possible questions to respond to."
      print(txt.format(num_questions))
      limitCond = str(input("Would you like to reduce the number of questions to answer? [Y/N]"))
      if limitCond in ['y', 'Y']:
        newnum_questions = int(0)
        while newnum_questions < 1 or newnum_questions > num_questions:
          newnum_questions = int(input(""))
      else:
        newnum_questions = num_questions
      return(newnum_questions)


      # There are currently {} amount of questions in Lesson X. Would you like to choose a smaller amount of questions for this session? num_questions = input("\nHow many questions would you like to answer?")
    def practice_type():
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

#    return(choose_lesson, num_questions, practice_type)

class PracticeFormat:
  def __init__(self, select_lesson, num_questions, practice_type):
    self.select_lesson = select_lesson
    self.num_questions = num_questions
    self.practice_type = practice_type


class LessonDetails:
  def __init__(cls, korean, english, conjugation):
    self.korean = korean
    self.english = english
    self.conjugation = conjugation

  def retrieve_lesson_from_database(num_lesson):
    str = "L{}arr"
    str = str.format(num_lesson)
    lesson_object =


def main():
  MainMenu.display_welcome_message()
  numLesson = GetUserInput.choose_lesson()
  lessonObject = LessonDetails.retrieve_lesson_from_database(numLesson)
  t = GetUserInput.practice_type()
  print(t)



main()
