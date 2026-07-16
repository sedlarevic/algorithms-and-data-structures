Use Divide & Conquer When:

The presence of a single element invalidates a section completely: 
You can easily identify "illegal" characters or elements that absolutely cannot be part of the final answer, allowing you to slice the data into independent fragments.

The condition is non-monotonic:
In standard window problems, adding an element makes a condition "more true" or "more false".
Here, adding a character can make a window invalid (e.g., adding a new unique character), but adding more of that same character later can make it valid again.
