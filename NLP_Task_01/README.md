<h1 align="center">NLP Lab 01 — Bag of Words & Cosine Similarity</h1>

<p align="center">
  <b>Vector Space Modeling</b>
</p>

<hr>

<h2>1. Bag of Words (BoW)</h2>

<p>
The <b>Bag of Words (BoW)</b> model represents text as numerical vectors by
counting the occurrences of words in a document. It ignores grammar and
word order and focuses only on the frequency of terms.
</p>

<p>
For this lab, <code>CountVectorizer</code> from scikit-learn is used to
extract the vocabulary and generate the term-frequency matrix.
</p>

<h2>2. Cosine Similarity</h2>

<p>
<b>Cosine Similarity</b> measures how similar two document vectors are by
calculating the cosine of the angle between them in a multidimensional
vector space.
</p>

<p align="center">
  <b>Cosine Similarity(A, B) =
  (A · B) / (||A|| × ||B||)</b>
</p>

<p>
The value ranges from <b>0.0</b> to <b>1.0</b> for the non-negative
Bag of Words vectors used in this lab. A value closer to 1 means that
the documents have more similar term proportions, while a value of 0
means that there are no overlapping terms in the represented vocabulary.
</p>

<hr>

<h2>3. Viva & Reflection Questions</h2>

<h3>Q1. Word Order Invariance</h3>

<p>
<b>Why does the sentence "Dog bites man" have the exact same Bag of Words
representation as "Man bites dog"? How does this impact sentiment analysis?</b>
</p>

<p>
Bag of Words only counts the occurrences of individual words and ignores
their order. Both sentences contain exactly the same words:
<b>dog</b>, <b>bites</b>, and <b>man</b>, each occurring once.
Therefore, both sentences produce the same Bag of Words vector.
</p>

<p>
This can be a limitation for <b>sentiment analysis</b> because changing
word order can change the meaning of a sentence while the Bag of Words
representation remains unchanged. As a result, BoW may fail to capture
important contextual or semantic relationships between words.
</p>

<h3>Q2. Sparsity Issue</h3>

<p>
<b>What happens to the memory size and density of the BoW matrix when the
corpus contains 100,000 unique vocabulary words?</b>
</p>

<p>
When the vocabulary contains <b>100,000 unique words</b>, the BoW matrix
becomes very large because every document needs a position for every word
in the vocabulary. However, most documents contain only a small fraction
of those 100,000 words.
</p>

<p>
Therefore, most entries in the matrix will be <b>zero</b>, making the
matrix highly <b>sparse</b>. Storing the complete matrix as a normal
dense matrix can require a large amount of memory. This is why
<code>CountVectorizer</code> normally produces a <b>sparse matrix</b>,
which stores only the non-zero values and is more memory-efficient.
</p>

<h3>Q3. Zero Similarity</h3>

<p>
<b>Explain why Document 3 in Task 2 receives a Cosine Similarity score of
0.0000 when queried against "machine learning algorithms for data".</b>
</p>

<p>
The query is:
</p>

<pre><code>machine learning algorithms for data</code></pre>

<p>
Document 3 is:
</p>

<pre><code>Natural language processing helps computers understand human language</code></pre>

<p>
After the text is converted into Bag of Words vectors, Document 3 has
no terms in common with the query from the vocabulary used for the
comparison. Therefore, the dot product between the query vector and
Document 3's vector is <b>0</b>.
</p>

<p>
Since the numerator of the cosine similarity formula is zero, the
resulting similarity score is:
</p>

<p align="center">
  <b>Cosine Similarity = 0.0000</b>
</p>

<p>
This means that, according to the Bag of Words representation, Document 3
has no term overlap with the given search query.
</p>

<hr>

<h2>4. Conclusion</h2>

<p>
In this lab, the <b>Bag of Words</b> model was used to convert textual
documents into numerical vectors based on term frequency. 
<b>Cosine Similarity</b> was then used to measure the similarity between
documents and a search query. The exercise also demonstrated important
limitations of BoW, including its inability to capture word order and
the sparsity problem that occurs when the vocabulary becomes very large.
</p>
