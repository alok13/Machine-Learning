Pearson correlation and cosine similarity are invariant to scaling, i.e. multiplying all elements by a nonzero constant. 
Pearson correlation is also invariant to adding any constant to all elements. 

For example, if you have two vectors X1 and X2, and your Pearson correlation function is called pearson(), pearson(X1, X2) == pearson(X1, 2 * X2 + 3). 
This is a pretty important property because you often don't care that two vectors are similar in absolute terms, 
only that they vary in the same way.
