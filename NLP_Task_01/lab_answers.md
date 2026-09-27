<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab Submission Report - Answers</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            background-color: #f6f8fa;
            margin: 0;
            padding: 40px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(27,31,35,0.12);
        }
        h1 {
            border-bottom: 1px solid #eaecef;
            padding-bottom: .3em;
            font-size: 24px;
            color: #24292e;
        }
        .question-block {
            margin-bottom: 30px;
        }
        h3 {
            font-size: 18px;
            color: #0366d6;
            margin-bottom: 8px;
        }
        p {
            margin-top: 0;
            margin-bottom: 16px;
            color: #444;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Lab Submission Report</h1>

        <div class="question-block">
            <h3>1. Word Order Invariance</h3>
            <p><strong>Ans.</strong> Basically, Bag of Words treats text like a literal bucket of words so it only counts what words are there and ignores the order completely. Because Dog bites man and Man bites dog have the exact same three words the computer counts them the exact same way and gives you identical representations.</p>
            <p>This ruins sentiment analysis because sequence and grammar matter a lot for tone. If a sentence says The food was not bad it was amazing a BoW model just sees a bunch of individual words floating around. It can completely miss how a word like not or the order of clauses changes the entire meaning of the sentence.</p>
        </div>

        <div class="question-block">
            <h3>2. Sparsity Issue</h3>
            <p><strong>Ans.</strong> If your vocabulary has 100000 words every single document gets turned into a massive vector with 100000 slots. But a normal sentence or paragraph only uses maybe 20 or 30 of those words.</p>
            <p>That means nearly every cell in your matrix is just a zero making the matrix insanely sparse with a density close to zero. If a computer tried to store all those millions of empty zeros as a normal dense matrix it would waste a ridiculous amount of RAM. That is why we use special sparse data structures that only remember the non-zero spots.</p>
        </div>

        <div class="question-block">
            <h3>3. Zero Similarity</h3>
            <p><strong>Ans.</strong> Document 3 got a 0.0000 because it shares literally zero words with the query machine learning algorithms for data. Cosine similarity measures how much two vectors overlap or point in the same direction. If there is not a single matching word between the query and the document there is no overlap at all which results in an angle of 90 degrees and a similarity score of dead-zero.</p>
        </div>
    </div>
</body>
</html>