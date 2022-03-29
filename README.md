# Author Recognition

# Basic Principle

Historically famous writers all have a unique literary style. Avid readers can quickly identify an author from a short sample of their writing. The use of specific words and most importantly **specific combinations of words** is what allows us to recognize an author’s work. For example, you can easily guess that the following lines were written by Shakespeare.

> Thou wilt be like a lover presently,
And tire the hearer with a book of words.
> 

The use of older English words like *thou* and *wilt* are a clear indication of that. Shakespeare is obviously not the only writer that does that. However, if I were to ask you whether the lines were written by Shakespeare or Twain, you’d most likely be able to give me a confident answer as Twain doesn’t really use this vocabulary. Therefore, we will focus on how to identify an author from an unseen text sample using a database of known authors.

Suppose our database consists of Shakespeare’s *Much Ado About Nothing* and *A Connecticut Yankee in King Arthur’s Court* by Mark Twain. Suppose we now want to identify the author of this very short sentence.

> I pray you, speak not
> 

Let’s first analyze the word *pray.* We have in our database 4600 lines written by Shakespeare. In those lines, this word appears 35 times meaning it is used once every 132 lines. In our Mark Twain database, it’s used 11 times over 13000 lines or once every 1200 lines. The word is used almost ten times more often by Shakespeare than by Twain. This is already a major clue helping us guess that Shakespeare wrote this sentence. But how can we make a more accurate guess? After all, Twain does use the word *pray* on a few occasions*,* there is a non-negligible chance that this sentence is one of those occasions. 

To make a more confident guess, we go back to our mention of **specific combinations of words**. On its own, *pray* does not contain enough information to identify the author with a considerable degree of certainty. However, when we study the combination of the words *pray* and *you,* we get a different story. In his 35 uses of the word *pray*, William Shakespeare follows it up with *you* on 16 different occasions. In *A Connecticut Yankee in King Arthur’s Court* this combination doesn’t appear once! 

We get a similar story when analyzing the word *speak*. Both authors use this word on numerous occasions. However, Mark Twain never writes it before the word *not* whereas Shakespeare wrote *speak not* on two different occasions in our database. We can now very confidently say that the sentence was written by William Shakespeare which would be correct since it was taken from *Macbeth*.

Full Article Here: https://simonkassab.com/#/author
