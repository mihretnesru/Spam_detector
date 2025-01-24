# 📨 Spam Detection Tool Using Naive Bayes

This project implements a **Naive Bayes classifier** to detect whether a message is spam or ham (non-spam). The program processes a dataset of pre-labeled SMS messages, computes word probabilities, and classifies user-input messages as either spam or ham based on their likelihood.

---

## 📜 Features

- **Naive Bayes Classification**: Calculates probabilities for spam and ham messages based on word frequencies.
- **Preprocessing**: 
  - Removes punctuation and digits.
  - Converts all words to lowercase.
- **Customizable Dataset**: The tool uses a `SMSSpamCollection` file (pre-labeled dataset), which can be replaced with your dataset.
- **Interactive Input**: Accepts a user-input message, preprocesses it, and classifies it as spam or ham.

---

## 🛠 How It Works

1. **Dataset Loading**:
   - The dataset (`SMSSpamCollection`) contains labeled messages in the format:
     ```
     spam    Win $1000 now!
     ham     How are you today?
     ```
   - The program reads the file and splits it into spam and ham messages.

2. **Text Preprocessing**:
   - Removes punctuation and digits.
   - Converts text to lowercase and tokenizes it into words.

3. **Word Frequency Calculation**:
   - Counts the frequency of each word in spam and ham messages.

4. **Naive Bayes Classification**:
   - Computes the probability of the user-input message being spam or ham using:
     ```
     P(spam|message) ∝ P(message|spam) * P(spam)
     P(ham|message) ∝ P(message|ham) * P(ham)
     ```
   - Classifies the message based on which probability is higher.

5. **Interactive Output**:
   - Displays the probabilities for spam and ham.
   - Prints whether the message is spam or ham.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Files Needed
- `SMSSpamCollection`: A text file containing labeled messages in the format:

