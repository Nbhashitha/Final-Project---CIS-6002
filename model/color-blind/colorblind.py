# -*- coding: utf-8 -*-
"""ColorBlind.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U2jeyM2ZyzHULQfErFKcvmsmtcyOIIBu
"""

# Getting the training data
training_data = [
                 [0,0,0,0,1,0,'Carrier - Daughter'],[0,0,0,0,0,1,'Son (Carrier - Daughter)'],[0,0,0,0,1,1,'Son'],[0,0,0,0,1,1,'Daughters'],
                 [1,0,0,0,0,0,'None'], [1,1,0,0,1,0,'Carrier - Daughter'], [0,0,1,1,1,0,'Son (Carrier - Daughter)'], [1,0,0,0,0,1,'Son 50% (50% Daughter - Carrier)'],
                 [1,0,1,0,0,0,'Son 50% (50% Daughter - Carrier)'],[0,1,0,1,1,0, 'Son 50% & Daughter 50% (Carrier - 50% Daughter)'], [0,1,0,1,1,1,'50% Daughter / 50% Son (50% Daughter - Carrier)'],
                 [1,0,1,1,0,1,'50% Daughter / 50% Sons (50% Daughter - Carrier / 50% Sons Don\'t have)'],[1,1,1,1,1,1,'Sons & Daughters']
]

# Headers for the data
header = ['Father\'s Father', 'Father\'s Mother', 'Mother\'s Father', 'Mother\'s Mother', 'Father', 'Mother']

def unique_vals(rows, col):
  """Find the unique values for a column in a dataset"""
  return set([row[col] for row in rows])

def class_count(rows):
  """Counts the number of each type of example in a dataset"""
  counts = {}
  for row in rows:
    label = row[-1]
    if label not in counts:
      counts[label] = 0
    counts[label] += 1
  return counts

def is_numeric(value):
  """Test if a value is numeric"""
  return isinstance(value, int) or isinstance(value, float)

class Question:
  """A Question is used to partition a dataset

  This class just records a 'column number' (eg: 0 & 1 for inputs).
  The 'match' method is used to compare the feature value in an example to the feature values stored in the question"""

  def __init__(self, column, value):
      self.column = column
      self.value = value

  def match(self, example):
    val = example[self.column]
    if is_numeric(val):
      return val >= self.value
    else:
      return val == self.value
    
  def __repr__(self):
      condition = "=="
      if is_numeric(self.value):
        condition = ">="
      return "Is %s %s %s?" % (
          header[self.column], condition, str(self.value)
      )
    
  def partition(rows, question):
    """Partition a dataset.

    For each row in the dataset, check if it matches the question. If so, add it to 'true rows', otherwise, add it to 'false rows'."""
    true_rows, false_rows = [], []
    for row in rows:
      if question.match(row):
        true_rows.append(rows)
      else:
        false_rows.append(row)
    return true_rows, false_rows

  def gini(rows):
    """Calculate the Gini Impurity for a list of rows."""

    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
      prob_of_lbl = counts[lbl] / float(len(rows))
      impurity -= prob_of_lbl**2
    return impurity

  def info_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of two child nodes"""
    p = float(len(left) / (len(left)+len(right)))
    return (current_uncertainty - p * gini(left) - (1-p) * gini(right))

  def find_best_split(rows):
    """Find the best question to ask by iterating over every feature / value and calculating the information gain"""
    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1

    for col in range(n_features):
      values = set([row[col] for row in rows])
      for val in values:
        question = Question(col, val)
        true_rows, false_rows = partition(rows, question)

class Leaf:
  """A Leaf node classifies data.

  This holds a dictionary of class number of times it appears in the rows from the training data that reach this leaf."""
  def __init__(self, rows):
    self.predictions = class_counts(rows)

class Decision_Node:
  """A Decision Node asks a question.

  This holds a reference to the question, and to the two child nodes."""
  def __init__(self, question, true_branch, false_branch):
    self.question = question
    self.true_branch = true_branch
    self.false_branch = false_branch

def build_tree(rows):
  """Builds the tree."""

  gain, question = find_best_split(rows)
  if gain == 0:
    return Leaf(rows)
  
  true_rows, false_rows = partition(rows, question)
  true_branch = build_tree(true_rows)
  false_branch = build_tree(false_rows)
  return Decision_Node(question, true_branch, false_branch)

def print_tree(node, spacing=""):
  """World's most elegant tree printing function"""

  if isinstance(node, Leaf):
    print(spacing + "Predict", node.prediction)
    return

  print(spacing + str(node.question))
  print(spacing+'--> True:')
  print_tree(node.true_branch, spacing + " ")
  print(spacing+'--> False:')
  print_tree(node.false_branch, spacing + " ")

def classify(row, node):
  if isinstance(node, Leaf):
    return node.predictions

  if node.question.match(row):
    return classify(row, node.true_branch)
  else:
    return classify(row, node.false_branch)

if __name__ == '__main__':
  my_tree = build_tree(training_data)
  print_tree(my_tree)

  testing_data = [
                 [0,0,0,0,1,0,'Carrier - Daughter'],[0,0,0,0,0,1,'Son (Carrier - Daughter)'],[0,0,0,0,1,1,'Son'],[0,0,0,0,1,1,'Daughters'],
                 [1,0,0,0,0,0,'None'], [1,1,0,0,1,0,'Carrier - Daughter'], [0,0,1,1,1,0,'Son (Carrier - Daughter)'], [1,0,0,0,0,1,'Son 50% (50% Daughter - Carrier)'],
                 [1,0,1,0,0,0,'Son 50% (50% Daughter - Carrier)'],[0,1,0,1,1,0, 'Son 50% & Daughter 50% (Carrier - 50% Daughter)'], [0,1,0,1,1,1,'50% Daughter / 50% Son (50% Daughter - Carrier)'],
                 [1,0,1,1,0,1,'50% Daughter / 50% Sons (50% Daughter - Carrier / 50% Sons Don\'t have)'],[1,1,1,1,1,1,'Sons & Daughters']
]

for row in testing_data:
  print("Actual: %s. Predicted: %s" % (row[-1], print_leaf(classify(row, my_tree))))