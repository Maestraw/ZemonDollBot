import nltk

# nltk.download()
import matplotlib.pyplot as plt

from nltk.tokenize import sent_tokenize,word_tokenize

news_article="""

Ladies will slay in vintage style
at Mutare Sports
Club on April 6 alongside Freeman and Master H.Harare will be lightened by Intotal Band, Feli Nandi, Winky D and Iyasa on April 13.The last party of the edition will be at ZITF Main Arena, Bulawayo with Master H, The Travellers Band and Iyasa.

"""

extacted_words=word_tokenize(news_article)

# print(extacted_words)


from nltk.probability import FreqDist

fd=FreqDist(extacted_words)


# print(fd.most_common(3))

fd.plot(30,cumulative=False)

plt.show()