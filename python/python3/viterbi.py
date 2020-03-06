def decode(input_length, tagset, score):
   """
   Compute the highest scoring sequence according to the scoring function.
   :param input_length: int. number of tokens in the input including <START> and <STOP>
   :param tagset: Array of strings, which are the possible tags.  Does not have <START>, <STOP>
   :param score: function from current_tag (string), previous_tag (string), i (int) to the score.  i=0 points to
    <START> and i=1 points to the first token. i=input_length-1 points to <STOP>
   :return: Array strings of length input_length, which is the highest scoring tag sequence including <START> and <STOP>
   """
   # Look at the function compute_score for an example of how the tag sequence should be scored

   len_of_tag = len(tagset)
   token_list = list(list())
   result_list = list()
   score_list = list()
   current_score = 0     # initialize score
   max_s = 0
   max_arg = ''
   word_pair = ['']

   for i in range(0, len_of_tag):
      current_score = compute_score(['<START>', i], input_length, score)
      score_list.append(current_score)                 # add the current score of each token
      token_list.append(['<START>', i])                 # append a path containing only the first word and '<START>'
      if(max_s < current_score):
         max_s = current_score
         max_arg = i

   result_list.append(max_arg)              # argmax of the first token scores
   max_s = 0     # reset max score

   for m in range(2, input_length):         # for each token afterwards
      score_dic = dict()                             # clear the score_dic
      for path in token_list:                       # for each possible path
         for k in range(0, len_of_tag):         # for each tag of the current token
            path.append(k)                            # append k to each path
            current_score = compute_score(path, input_length, score)
            if(max_s < current_score):
               max_s = current_score
               max_arg = k
            path.pop()           # pop the last elem out

         path.append(max_arg)
         score_dic[max_s] = max_arg
         max_arg = ''          # reset max_arg
         max_s = 0             # reset max_s

      result_list.append(max(score_dic))

   return result_list
