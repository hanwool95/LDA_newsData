from wordcloud import WordCloud
import matplotlib.pyplot as plt

#출처 https://frhyme.github.io/python-lib/wordcloud/

text = "coffee phone phone phone phone phone phone phone phone phone cat dog dog"

# Generate a word cloud image
wordcloud = WordCloud(max_font_size=100).generate(text)

# Display the generated image:
# the matplotlib way:

fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/wordcloud_ex1.svg')