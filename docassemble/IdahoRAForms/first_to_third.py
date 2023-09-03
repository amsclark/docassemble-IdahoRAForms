def first_to_third(sentence):
  sentence = sentence.replace(" I ", " they ")
  sentence = sentence.replace("I ", "they ")
  sentence = sentence.replace(" me ", " them")
  sentence = sentence.replace(" me.", " them.")
  sentence = sentence.replace(" me?", " them?")
  sentence = sentence.replace(" my ", " their ")
  sentence = sentence.replace("I am", "they are")
  sentence = sentence.replace("I'm", "they are")
  sentence = sentence.replace("I was", "they were")                      
  sentence = sentence.replace("myself", "themself")
  return sentence